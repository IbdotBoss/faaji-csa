#!/usr/bin/env python3
from pathlib import Path
import re, json

md_path = Path('/home/ubuntu/hermes-workspace/Faajaa-Share/ServiceNow/CSA-questions/CSA-Master-Question-Bank.md')
text = md_path.read_text()

# Parse questions
questions = []
current_domain = ''
q_pattern = re.compile(r'\*\*Q(\d+)\.\*\*\s*(.*?)(?=\*\*Q\d+\.\*\*|### Domain|$)', re.S)
for m in q_pattern.finditer(text):
    num = int(m.group(1))
    body = m.group(2).strip()
    # Extract question text (first line)
    lines = body.splitlines()
    q_text = lines[0].strip()
    # Check for choose-all-that-apply marker
    choose_match = re.search(r'\(Choose\s+\d+\)', q_text)
    is_multi = bool(choose_match)
    # Extract options
    opts = []
    opt_pattern = re.compile(r'^- [A-Z]\.\s+(.*)$', re.MULTILINE)
    for opt_m in opt_pattern.finditer(body):
        opts.append(opt_m.group(1).strip())
    # Determine correct indices from answer section (parse later)
    questions.append({
        'num': num,
        'domain': current_domain,
        'text': q_text,
        'type': 'mul' if is_multi else 'sng',
        'opts': opts,
        'c': [],  # fill later
        'e': ''
    })

# Parse answer table
answer_map = {}
answer_pattern = re.compile(r'^\|\s*Q(\d+)\s*\|\s*([A-Z, ]+)\s*\|\s*(.*?)\s*\|$', re.MULTILINE)
# Also handle "Q1-D" style or multi-answer "Q10-A,C"
for m in answer_pattern.finditer(text):
    num = int(m.group(1))
    ans = m.group(2).strip()
    expl = m.group(3).strip()
    # Parse answer letters to indices (0-based)
    answer_letters = [x.strip() for x in ans.replace(',',' ').split() if x.strip()]
    # Build letter->index mapping from options in question
    q = next((q for q in questions if q['num'] == num), None)
    if q:
        letter_to_idx = {chr(65+i): i for i in range(len(q['opts']))}
        indices = [letter_to_idx[l] for l in answer_letters if l in letter_to_idx]
        q['c'] = indices
        q['e'] = expl

# Extract domain names from section headers
domain_names = re.findall(r'^## Domain \d+ — (.+?)(?:\s*\(|$)', text, re.MULTILINE)
print('domains found', len(domain_names), domain_names)

# Need to map each question to its domain based on position in text
q_starts = [(m.start(), int(m.group(1))) for m in re.finditer(r'\*\*Q(\d+)\.\*\*', text)]
domain_starts = [(m.start(), m.group(1).strip()) for m in re.finditer(r'^## Domain \d+ — (.+)', text, re.MULTILINE)]
# Simplified: reassign by iterating through text sections
questions_by_num = {q['num']: q for q in questions}
q_list_sorted = sorted(q_starts, key=lambda x: x[0])
dom_list_sorted = sorted(domain_starts, key=lambda x: x[0])
for i, (qs_start, q_num) in enumerate(q_list_sorted):
    # Find the domain section that precedes this question
    domain = ''
    for ds_start, dname in dom_list_sorted:
        if ds_start <= qs_start:
            domain = dname
        else:
            break
    if q_num in questions_by_num:
        questions_by_num[q_num]['domain'] = domain

# Build ordered questions array
ordered = [questions_by_num[i] for i in sorted(questions_by_num.keys()) if i in questions_by_num]
# Filter out any with empty options (non-question sections)
ordered = [q for q in ordered if q['opts']]
print('final question count', len(ordered))
if ordered:
    print('first', ordered[0]['num'], ordered[0]['domain'], ordered[0]['text'][:60])
    print('last', ordered[-1]['num'], ordered[-1]['domain'], ordered[-1]['text'][:60])

# Existing HTML structure
html_prefix = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>ServiceNow CSA Practice</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Berkeley+Mono:ital,wght@0,400;0,500;0,700;1,400&family=Geist:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<style>
  :root{--bg:#f5f2ed;--surface:#ffffff;--ink:#141311;--muted:#6b6560;--border:#e6e1da;--accent:#b45309;--accent-soft:#fff7ed;--ok:#166534;--ok-bg:#f0fdf4;--bad:#991b1b;--bad-bg:#fef2f2;--rule:#ece8e1;--shadow:0 1px 2px rgba(20,19,17,.04),0 6px 18px rgba(20,19,17,.06);--shadow-hover:0 4px 12px rgba(20,19,17,.08),0 12px 30px rgba(20,19,17,.10)}
  *{box-sizing:border-box}
  html,body{margin:0;background:var(--bg);color:var(--ink);font-family:'Geist',system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial;font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
  header{position:sticky;top:0;z-index:50;background:rgba(245,242,237,.78);backdrop-filter:blur(14px) saturate(140%);border-bottom:1px solid var(--border);padding:14px 22px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
  .brand{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
  h1{font-family:'Berkeley Mono',monospace;font-size:15px;font-weight:500;letter-spacing:-.2px;margin:0;color:var(--ink)}
  .pill{font-family:'Berkeley Mono',monospace;font-size:12px;color:var(--muted);background:var(--surface);border:1px solid var(--border);padding:4px 10px;border-radius:999px}
  .controls{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
  button{font-family:'Geist',system-ui,sans-serif;font-size:14px;font-weight:500;background:var(--surface);color:var(--ink);border:1px solid var(--border);padding:8px 14px;border-radius:10px;cursor:pointer;transition:transform .08s ease,border-color .15s ease,box-shadow .15s ease}
  button:hover{border-color:#cbc5bd;box-shadow:var(--shadow)}
  button:active{transform:translateY(1px)}
  button.primary{background:var(--ink);color:#fff;border-color:var(--ink)}
  button.primary:hover{background:#2a2723}
  main{max-width:980px;margin:24px auto;padding:0 18px 110px}
  .domain{margin:34px 0 10px;display:flex;align-items:center;gap:12px;position:sticky;top:62px;z-index:20;background:rgba(245,242,237,.68);backdrop-filter:blur(10px);padding:10px 2px}
  .domain-title{font-family:'Berkeley Mono',monospace;font-size:12px;font-weight:500;letter-spacing:.18px;text-transform:uppercase;color:var(--muted);white-space:nowrap}
  .domain::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,var(--rule),transparent 90%)}
  .q{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:18px 22px 18px;margin:14px 0;box-shadow:var(--shadow);transition:box-shadow .18s ease,border-color .18s ease}
  .q:hover{box-shadow:var(--shadow-hover);border-color:#d8d3ca}
  .q-head{display:flex;justify-content:space-between;gap:10px;align-items:flex-start;margin-bottom:10px;flex-wrap:wrap}
  .q h3{font-size:16px;font-weight:500;margin:0;line-height:1.45;letter-spacing:-.1px}
  .badge{font-family:'Berkeley Mono',monospace;font-size:11px;background:var(--accent-soft);color:var(--accent);border:1px solid #fed7aa;padding:4px 10px;border-radius:999px;white-space:nowrap;font-weight:500}
  .badge.pass{background:var(--ok-bg);color:var(--ok);border-color:#bbf7d0}
  .badge.fail{background:var(--bad-bg);color:var(--bad);border-color:#fecaca}
  .opts{display:grid;gap:8px}
  label.choice{display:flex;gap:12px;align-items:flex-start;background:#faf9f7;border:1px solid var(--border);padding:11px 14px;border-radius:12px;cursor:pointer;transition:background .12s ease,border-color .12s ease}
  label.choice:hover{border-color:#cbc5bd;background:#fff}
  input[type=checkbox],input[type=radio]{margin-top:3px;accent-color:var(--accent);width:17px;height:17px}
  .explain{margin-top:14px;padding:14px 16px;border-radius:12px;background:linear-gradient(180deg,#fff,#faf9f7);border:1px solid var(--border);color:#3f3b37;display:none;font-size:14.5px;line-height:1.6}
  .explain.show{display:block}
  .explain.ok{border-color:#bbf7d0;background:linear-gradient(180deg,#f0fdf4,#ecfdf5)}
  .explain.bad{border-color:#fecaca;background:linear-gradient(180deg,#fef2f2,#fff5f5);color:#7f1d1d}
  #sticky{position:fixed;left:0;right:0;bottom:0;background:rgba(245,242,237,.78);backdrop-filter:blur(14px) saturate(140%);border-top:1px solid var(--border);padding:12px 18px;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;z-index:40}
  .stat{font-family:'Berkeley Mono',monospace;font-size:13px;color:var(--muted);background:var(--surface);border:1px solid var(--border);padding:6px 12px;border-radius:10px}
  .stat strong{color:var(--ink);font-weight:600}
  .done #sticky{background:rgba(245,242,237,.92)}
  @media (max-width:640px){.q{padding:14px 16px} header{flex-direction:column;align-items:flex-start} .q-head{flex-direction:column;gap:6px} .badge{width:max-content}}
</style>
</head>
<body>
<header>
  <div class="brand">
    <h1>ServiceNow CSA Practice — Master Bank</h1>
    <span class="pill" id="totalPill">loading…</span>
  </div>
  <div class="controls">
    <button onclick="shuffle()">Shuffle</button>
    <button onclick="resetAll()">Reset</button>
    <button class="primary" onclick="submitAll()">Submit all</button>
  </div>
</header>

<main id="qwrap"></main>

<div id="sticky">
  <div class="stat">Progress <strong id="prog">0 / 0</strong></div>
  <div class="stat">Score <strong id="score">0%</strong></div>
  <div style="display:flex;gap:8px">
    <button onclick="submitAll()">Submit all</button>
    <button onclick="resetAll()">Reset</button>
  </div>
</div>

<script>
const questions = 
'''

questions_json = json.dumps(ordered, ensure_ascii=False, indent=None)
# Replace escaped quotes properly
questions_json = questions_json.replace('\\"', '"')

html_suffix = ''';
let order = questions.map((_,i)=>i);
function upd(){const answered=document.querySelectorAll('.q input:checked').length;prog.textContent=answered + ' / ' + questions.length;totalPill.textContent=questions.length + ' questions';let sc=0,att=0;document.querySelectorAll('.q').forEach(box=>{const i=+box.dataset.i;const q=questions[order[i]];const checked=[];box.querySelectorAll('input:checked').forEach(c=>checked.push(+c.value));if(!checked.length) return;att++;if(checked.join(',')===q.c.join(',')) sc++;});score.textContent=att?Math.round((sc/att)*100)+'%':'0%';}
function render(){qwrap.innerHTML='';const seen=new Set();order.forEach((oi,idx)=>{const q=questions[oi];if(seen.has(q.t)) return;seen.add(q.t);const box=document.createElement('div');box.className='q';box.dataset.i=idx;box.dataset.idx=oi;const head=document.createElement('div');head.className='q-head';const title=document.createElement('h3');title.textContent=(idx+1)+'. '+q.t;head.appendChild(title);const badge=document.createElement('span');badge.className='badge';badge.textContent=q.type==='mul'?'Select all that apply':'Select one';head.appendChild(badge);box.appendChild(head);const opts=document.createElement('div');opts.className='opts';q.opts.forEach((o,oi2)=>{const lbl=document.createElement('label');lbl.className='choice';const inp=document.createElement('input');inp.type=q.type==='mul'?'checkbox':'radio';inp.name='q'+idx;inp.value=oi2;inp.addEventListener('change',()=>{upd();});lbl.appendChild(inp);const span=document.createElement('span');span.textContent=(String.fromCharCode(65+oi2))+'. '+o;lbl.appendChild(span);opts.appendChild(lbl);});box.appendChild(opts);const expl=document.createElement('div');expl.className='explain';expl.innerHTML='<strong>Answer:</strong> ' + ((q.c.map(i=>String.fromCharCode(65+i)).join(', ')) || '—') + '<br/><strong>Explanation:</strong> ' + (q.e||'—');box.appendChild(expl);qwrap.appendChild(box);});upd();}
function submitAll(){document.body.classList.add('done');let sc=0;document.querySelectorAll('.q').forEach(box=>{const i=+box.dataset.i;const q=questions[order[i]];const checked=[];box.querySelectorAll('input:checked').forEach(c=>checked.push(+c.value));const correct=checked.join(',')===q.c.join(',');if(correct) sc++;const badge=box.querySelector('.badge');badge.className='badge '+(correct?'pass':'fail');badge.textContent=correct?'Correct':'Incorrect';const expl=box.querySelector('.explain');expl.classList.add('show',correct?'ok':'bad');});const totalPillEl=document.getElementById('totalPill');totalPillEl.textContent=sc+' / '+questions.length + ' passed';let txt=sc+' / '+questions.length+'\\n';document.querySelectorAll('.q').forEach((box,idx)=>{const i=+box.dataset.i;const q=questions[order[i]];const checked=[];box.querySelectorAll('input:checked').forEach(c=>checked.push(+c.value));const correct=checked.join(',')===q.c.join(',');txt+=(idx+1)+'. ' + (correct?'✔':'✖') + '\\n';});try{const t=document.createElement('textarea');t.value=txt;document.body.appendChild(t);t.select();document.execCommand('copy');document.body.removeChild(t);alert('Score copied to clipboard');}catch(e){alert('Score: '+sc+'/'+questions.length);}}
function resetAll(){document.querySelectorAll('.q').forEach(box=>{box.querySelectorAll('input:checked').forEach(c=>c.checked=false);const expl=box.querySelector('.explain');expl.className='explain';box.querySelectorAll('.badge').forEach(b=>b.remove());const i=+box.dataset.i;const badge=document.createElement('span');badge.className='badge';badge.textContent=questions[order[i]].type==='mul'?'Select all that apply':'Select one';box.querySelector('.q-head').appendChild(badge);box.querySelectorAll('label.choice').forEach(lb=>{lb.style.borderColor='';lb.style.background='';});});document.body.classList.remove('done');upd();}
function shuffle(){order=order.map(x=>({x,r:Math.random()})).sort((a,b)=>a.r-b.r).map(o=>o.x);render();}
render();
</script>
</body>
</html>'''

html = html_prefix + questions_json + html_suffix
out = Path('/home/ubuntu/hermes-workspace/ServiceNow/docs/index.html')
out.write_text(html)
print('wrote', out, 'size', len(html), 'questions', len(ordered))
