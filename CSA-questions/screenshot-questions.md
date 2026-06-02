# ServiceNow CSA Practice — Extracted from Former Exam Screenshots
Source screenshots: `Faajaa-Share\ServiceNow\CSA-questions\Screenshot 2026-03-23 *.png`
Cleaned from raw OCR; some wording is normalized for accuracy.

---

## Screenshot Set (14 questions)

### Q1
**Topic:** Update Sets  
**Which record types are automatically captured by the current Update Set?**  
> Choose 2 answers.

- A. Business rules
- B. User password records
- C. Incident task data
- D. UI policies

**Answers:** Business rules, UI policies  
**Explanation:** Update Sets capture metadata/configuration records, not transactional data like incident records or sensitive user credential data meant to remain instance-isolated.

---

### Q2
**Topic:** Update Sets — Compare Tools  
**Which capabilities are associated with compare tools for conflict resolution?**  
> Choose 2 answers.

- A. Rollback update set
- B. Show update history
- C. Identify duplicate or competing records
- D. Preview local and remote sets
- E. Scan Update Set

**Answers:** Identify duplicate or competing records, Preview local and remote sets  
**Explanation:** Compare tools mainly support conflict identification and previewing diffs between source/target before commit.

---

### Q3
**Topic:** Update Sets  
**What is an Update Set?**

- A. Containers for configuration changes that track changes to tables
- B. A data archival utility for CMDB records
- C. A mechanism for cloning entire instances
- D. A runtime engine for Workflow Studio executions

**Answer:** A  
**Explanation:** Update Sets capture configuration metadata changes so they can be moved between instances.

---

### Q4
**Topic:** Update Sets  
**Which tasks does a user perform when inspecting and reporting on Update Sets?**  
> Choose 2 answers.

- A. Export Update Sets to CSV
- B. Compare content with the target instance to spot conflicts
- C. Review the Update set Logs table
- D. Browse included updates and drill into individual records

**Answers:** Compare content with the target instance to spot conflicts, Browse included updates and drill into individual records  
**Explanation:** Inspecting Update Sets is about review and comparison workflows.

---

### Q5
**Topic:** Instance Scan  
**What does Instance Scan evaluate?**  
> Choose 2 answers.

- A. License consumption tiers
- B. User login frequency
- C. Data breach counts
- D. Risk patterns
- E. Best practice violations

**Answers:** Risk patterns, Best practice violations  
**Explanation:** Instance Scan is focused on operations risk and platform/code best-practice checks, not built-in license telemetry or login metrics.

---

### Q6
**Topic:** Update Sets — Components  
**Which components does an Update Set contain?**  
> Choose 2 answers.

- A. Status and metadata for retrieval, preview, and commit
- B. MID Server connection details
- C. Plugin activation history
- D. The configuration deltas
- E. User session audit logs

**Answers:** Status and metadata for retrieval, preview, and commit, The configuration deltas  
**Explanation:** An Update Set is the configured change package plus lifecycle metadata; it does not store runtime secrets or session logs.

---

### Q7
**Topic:** Update Sets  
**What is the purpose of merging Update Sets in ServiceNow?**

- A. Convert XML to JSON before import
- B. Create a parent with scoped children for a release
- C. Combine records from several sets into a single set
- D. Link Update Sets across instances for real-time sync

**Answer:** C  
**Explanation:** Merge consolidates multiple Update Sets into one managed release unit.

---

### Q8
**Topic:** Update Sets  
**What action do administrators perform when inspecting an Update Set?**

- A. View differences against current versions
- B. Export user roles to CSV
- C. Run a full instance clone
- D. Trigger discovery schedules

**Answer:** A  
**Explanation:** Inspecting an Update Set is about comparing changes against the target instance’s current state.

---

### Q9
**Topic:** Update Sets  
**Which action is explicitly warned against because it can damage the system?**

- A. Exporting an Update Set to XML
- B. Setting an Update Set to Complete
- C. Rolling back from the Default Update Set
- D. Viewing differences against current versions

**Answer:** C  
**Explanation:** The Default Update Set is special; rolling it back can break expected configuration history behavior.

---

### Q10
**Topic:** Update Sets  
**Which format is used to represent Update Sets?**

- A. XML
- B. CSV
- C. JSON
- D. YAML

**Answer:** A  
**Explanation:** Update Sets are transported via XML payloads.

---

### Q11
**Topic:** Update Sets  
**What is the correct order of steps for moving Completed Update Sets between instances?**

- A. Export from instance A, Import/Retrieve into instance B, Preview in instance B, Commit in instance B
- B. Export/Retrieve from instance A, Commit in instance B, Preview in instance B, Import into instance B
- C. Import into instance A, Commit in instance B, Preview in instance B, Export in instance B
- D. Retrieve from instance A, Commit in instance B, Preview in instance B, Import in instance B

**Answer:** A  
**Explanation:** Standard move is source extraction/reference capture, target retrieval, then preview, then commit.

---

### Q12
**Topic:** Update Sets  
**Which activity is identified as an ideal use of Update Sets?**

- A. Migrating incident data between instances
- B. Storing and applying specific versions of applications
- C. Managing user passwords across instances
- D. Scheduling discovery scans

**Answer:** B  
**Explanation:** Update Sets version configuration changes, not transactional business data.

---

### Q13
**Topic:** Update Sets  
**Which is listed as a component contained within an Update Set?**

- A. Attachment binaries embedded in records
- B. User session tokens
- C. The records changed as update records
- D. MID Server credentials

**Answer:** C  
**Explanation:** An Update Set contains the changed configuration records, not embedded attachments, session tokens, or secrets.

---

### Q14
**Topic:** Update Sets  
**What is the purpose of marking an Update Set as “Ignore” in production after committing?**

- A. To remove it from the history of changes
- B. To automatically rollback changes
- C. To prevent reapplication during a future retrieve
- D. To compress its XML for storage

**Answer:** C  
**Explanation:** Ignore prevents the set from being reapplied if it’s retrieved again later.

---

## Screenshot Coverage Notes
- Focus: Update Sets and Instance Scan
- Missing from screenshots: Platform navigation, Knowledge Mgmt, CMDB/CSDM, UI Policies, Business Rules, Notifications, Service Catalog, Virtual Agent, Scripting, ACLs
