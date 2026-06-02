# ServiceNow CSA Practice — Blueprint-Aligned Expanded Set (60 Questions)
Purpose: Match the official CSA Mainline Exam Blueprint domains and weighting.
Source: official blueprint KB0011554, candidate study bulk material, and screenshot-derived items.
Format: single-answer MCQ and select-all-that-apply; no partial credit on multi-select.

## How this packet was built
- Use the official blueprint for scope and emphasis.
- Write items in official platform language rather than exam-secret guesses.
- Distractors follow typical multi-select style: one or more obviously wrong, one or more plausible, and the requested number of correct answers.
- Keep every item actionable and verifiable from official docs or courses.

## Exam Simulation Notes
- No partial credit is awarded on multi-select questions.
- Prioritise review of Domain 5 and Domain 3/4 where weighting is highest.

## Domain 1 — Platform Overview and Navigation (7%) | Q1–Q4

### Q1
What type of URL is associated with a customer instance in Next Experience Unified Navigation?
- A. `/login.do`
- B. A branded instance URL pointing to the customer instance
- C. `/nav_to.do?uri=` page only
- D. `/index.jsp`
Answer: B

### Q2
Which of the following are typical starting points for navigation in the Next Experience UI? Choose 2.
- A. Type a table name in the Application Navigator filter
- B. A direct instance URL with a `/nav_to.do?uri=` reference
- C. Edit `global.js` in the customer instance
- D. SSH into the instance and edit `index.html`
Answers: A, B

### Q3
Where can a user find recently viewed records in the Next Experience UI?
- A. Application menu
- B. Favorites
- C. Recent module
- D. System Log
Answer: C

### Q4
What is the shared responsibility boundary in the ServiceNow business model? Choose 2.
- A. Customer manages instance configuration and data
- B. Customer manages physical data center operations and hardware
- C. ServiceNow manages platform infrastructure
- D. Customer patches the ISP router on the instance uplink
Answers: A, C

## Domain 2 — Instance Configuration (10%) | Q5–Q10

### Q5
Why would an administrator install an application or plugin on a ServiceNow instance?
- A. To patch the operating system image
- B. To add new platform capabilities such as ITSM, HR, or SecOps
- C. To connect to third-party email providers only
- D. To delete system properties safely
Answer: B

### Q6
What interface type is best for adding UI text and widgets without code changes?
- A. Scripted REST API
- B. UI Scripts only
- C. UI Builder / low-code interface
- D. MID Server terminal
Answer: C

### Q7
Which plugin or application would enable HR Service Delivery capabilities?
- A. Customer Service Management
- B. HR Service Delivery
- C. Financial Services Operations
- D. IT Asset Management
Answer: B

### Q8
Which of the following can be personalized for a user in the platform? Choose 2.
- A. Homepage dashboard
- B. Browser network stack
- C. Time zone and language on My Profile
- D. Linux kernel parameters
Answers: A, C

### Q9
A business needs simple asset tracking for laptops in one location without a full CMDB model. Which is the most lightweight path?
- A. Deploy full CSDM and CI classes
- B. Use a custom application or table extension
- C. Install an unrelated full-suite plugin just for tracking
- D. Replace the instance with a spreadsheet
Answer: B

### Q10
Which setting path is used when configuring application-specific instance behavior?
- A. Version Control menu on the form header
- B. Application Properties or System Properties
- C. Browser developer console
- D. Command-line launcher only
Answer: B

## Domain 3 — Configuring Applications for Collaboration (20%) | Q11–Q22

### Q11
Which list setting should be configured to improve performance?
- A. Always return all columns
- B. Use list layouts and avoid returning unnecessary columns
- C. Remove all filters
- D. Increase the default row limit without index support
Answer: B

### Q12
What is a reference qualifier used for?
- A. Changing database collation
- B. Restricting the values returned in a reference field
- C. Increasing plugin memory
- D. Adding page headers
Answer: B

### Q13
Which form section behavior hides content but keeps it on the record?
- A. Collapsible section
- B. Dictionary delete action
- C. Table truncation
- D. Audit field removal
Answer: A

### Q14
Why should an administrator avoid too many mandatory fields on high-volume forms? Choose 2.
- A. Better performance
- B. Reduced agent load when staging cases
- C. Higher completion and satisfaction for agents
- D. Increased context switching and slower intake
Answers: C, D

### Q15
What is the role of a form template in ServiceNow?
- A. Define network routing for MID Servers
- B. Standardize section structure and field placement across users
- C. Replace database backup schedules
- D. Disable subscriptions for a table
Answer: B

### Q16
Which feature allows advanced field behavior such as visibility and read-only conditions?
- A. Dictionary overrides only
- B. UI policies
- C. MID Server packet inspection
- D. Email templates
Answer: B

### Q17
What is a Visual Task Board primarily used to visualize?
- A. Kernel thread states
- B. Work items by status, assignment, or sprint columns
- C. Hard drive temperatures
- D. API connection pools only
Answer: B

### Q18
Which dashboard type in the Now Platform is best for executive KPI review?
- A. Terminal shell view
- B. Performance Analytics dashboard or Platform Analytics dashboard
- C. MID Server console dashboard
- D. Source code dashboard
Answer: B

### Q19
Which best supports rota-based assignment for a task queue?
- A. Visual Task Board delegation rules
- B. Assignment rules / workload management / assignment groups
- C. Update Set merge on weekends
- D. Plugin disable/enable cycles
Answer: B

### Q20
Where are notification definitions configured for a given table?
- A. MID Server network map
- B. System Notification > Email > Notifications
- C. Linux cron table
- D. Web server log rotation
Answer: B

### Q21
When should a notification template be avoided for high-volume alerts?
- A. When event management is preferred over email
- B. Only when the table contains no email field
- C. When webhook-only routing is blocked by the browser
- D. MID Server offline
Answer: A

### Q22
A report shows duplicate rows for the same user. Which simplest cause should an admin check first?
- A. Required user login
- B. Duplicate active user or reference field entries
- C. Plugin license expiration
- D. Kernel lock wait timeout
Answer: B

## Domain 4 — Self Service & Automation (20%) | Q23–Q32

### Q23
Why is a Knowledge article lifecycle important?
- A. It prevents authors from ever retiring old articles
- B. It ensures accurate current content through review and expiry states
- C. It guarantees every article gets 10,000 views
- D. It removes article attachments automatically
Answer: B

### Q24
Which knowledge state usually allows end-user search and consumption?
- A. Draft
- B. Published
- C. Retired
- D. Obsolete
Answer: B

### Q25
Which data structure supports nested categorization of knowledge articles?
- A. Knowledge article text body only
- B. Knowledge categories hierarchy
- C. Virtual Agent intents on cmd.exe
- D. Update Set lineage
Answer: B

### Q26
In the Service Catalog, how is the request workflow triggered?
- A. Browser cron schedule
- B. Record producer / catalog item workflow or flow
- C. MID Server scheduler
- D. Linux cron
Answer: B

### Q27
What is the difference between a record producer and a catalog item?
- A. Both create only email templates
- B. Record producers create task records; catalog items create general records or requests
- C. Record producers disable workflows
- D. Catalog items are limited to Read ACLs only
Answer: B

### Q28
When should Virtual Agent be preferred over a static knowledge article? Choose 2.
- A. When conversational intent routing helps users faster
- B. When the content should never update
- C. When guided form completion reduces errors
- D. When the file must be named cmd.exe
Answers: A, C

### Q29
Which engine is used to create guided conversational experiences in ServiceNow?
- A. Workflow Studio for chat only
- B. Virtual Agent Designer
- C. Linux desktop environment
- D. MID Server UI
Answer: B

### Q30
In Flow Designer, what is a common trigger pattern for catalog fulfillment?
- A. Webhook ping to cron only
- B. Record created or catalog item requested
- C. Memory dump on crash
- D. MID Server heartbeat only
Answer: B

### Q31
A self-service flow needs to pause for approval. Which pattern is standard?
- A. Busy-wait loop in `gs.info`
- B. Approval action / human approval activity in the flow
- C. SQL sleep on the transaction table
- D. Client-side blocking script
Answer: B

### Q32
Which is an expected benefit of low-code automation in ServiceNow?
- A. Increased manual ticket duplicates
- B. Faster delivery and reduced reliance on custom scripts
- C. Higher cabling complexity on MID Servers
- D. Mandatory kernel updates
Answer: B

## Domain 5 — Database Management and Platform Security (30%) | Q33–Q50

### Q33
Which object defines the schema of a table in ServiceNow?
- A. Dictionary entry
- B. Browser cache
- C. MID Server config
- D. Linux random pool
Answer: A

### Q34
What does an access control rule ACL protect?
- A. Network packets only
- B. Table or record-level operations: read, write, create, delete
- C. Linux logins only
- D. Printer spool queue
Answer: B

### Q35
Which operation should be evaluated first when a user cannot see a record?
- A. Reset browser zoom
- B. Read ACL, roles, and record-level conditions
- C. Replace router firmware
- D. Restart MID Server only
Answer: B

### Q36
Why is separating user roles a security principle in ServiceNow?
- A. It increases database size
- B. It follows least privilege and separation of duties
- C. It increases network latency
- D. It disables catalog widgets
Answer: B

### Q37
In an import set, what is a transform map used for?
- A. Define disk partitions
- B. Map fields from the staging table to the target table
- C. Replace kernel scheduler policies
- D. Set MID Server firewall rules
Answer: B

### Q38
Before importing data, which requirement helps avoid bulk failure?
- A. Convert CSV to JPEG
- B. Define required fields and validate format and values
- C. Disable logging on Linux
- D. Rename database to cmd.exe
Answer: B

### Q39
Which application supports populating the CMDB and tracking CIs?
- A. Browser developer console
- B. Discovery and Service Mapping
- C. Linux package manager
- D. Virtual Agent browser extension
Answer: B

### Q40
What does CSDM stand for?
- A. Cloud Service Delivery Manager
- B. Common Service Data Model
- C. Control Server Device Mode
- D. Client-side Data Mirror
Answer: B

### Q41
Which CMDB base class typically represents an installed application?
- A. cmdb_software_instance
- B. cmdb_ci_linux_server
- C. cmdb_ci_network_gear
- D. cmdb_ci_service
Answer: A

### Q42
What is the recommended update-set discipline? Choose 2.
- A. Capture config changes in one traced update set
- B. Mix user bug reports and passwords in update sets
- C. Preview and validate before commit
- D. Commit unverified updates in production
Answers: A, C

### Q43
What does Instance Scan review focus on?
- A. Password security only
- B. Risk patterns and best practice violations
- C. Cable color on MID Servers
- D. Linux thread stacks
Answer: B

### Q44
Which capability helps identify excess privileges?
- A. MID Server connectivity test
- B. User access review and access control rule assessment
- C. DNS cache flush
- D. Linux uptime report
Answer: B

### Q45
What is a safe change-management step in production?
- A. Commit untested update set changes immediately
- B. Follow preview, peer review, and change management approval before commit
- C. Reset root account passwords in browsers only
- D. Disable ACLs fully before commit
Answer: B

### Q46
Which method is preferred for loading reference data without custom code?
- A. Import set with transform map
- B. SSH into Linux and run sed on files
- C. Edit kernel threads
- D. Rename MID Server executable to cmd.exe
Answer: A

### Q47
When migration fails with duplicate keys, what is the first check?
- A. Browser extension list
- B. Unique constraints and existing duplicate records
- C. Linux memory mismatch
- D. MID Server power cycle
Answer: B

### Q48
How does CMDB reconciliation help?
- A. It deletes all CI records
- B. It identifies duplicate and conflicting CI records across sources
- C. It increases network packet volume
- D. It controls Linux logs only
Answer: B

### Q49
Which control should be reviewed first if a standard user sees sensitive HR cases?
- A. Browser extension list
- B. Business rule and ACL interaction including elevated privileges
- C. MID Server Wi-Fi router settings
- D. Virtual Agent intents only
Answer: B

### Q50
A support engineer cannot enter incidents but can view them. Which is the most likely cause?
- A. Read ACL is allowed, but write/create ACL is missing or denied
- B. Browser zoom is too low
- C. Linux file permission error
- D. MID Server is offline
Answer: A

## Domain 6 — Data Migration and Integration (13%) | Q51–Q60

### Q51
Which record types should be avoided from update sets due to security isolation?
- A. Business rules and UI policies
- B. User password records
- C. Format controls
- D. Choice lists
Answer: B

### Q52
What is a reference qualifier commonly applied to?
- A. Noise reduction on MID Server logs
- B. Reference field options limiting returned values
- C. Linux thread heap management
- D. Web server log rotation
Answer: B

### Q53
When should an update set be marked Ignore?
- A. To remove it from history entirely
- B. To prevent future reapplication on a later retrieve
- C. To compress its XML by half
- D. To encrypt browser cookies
Answer: B

### Q54
What format are completed update sets transported in?
- A. Binary cabinet file
- B. XML
- C. JSON only
- D. YAML only
Answer: B

### Q55
Which step comes first when moving update sets between instances?
- A. Retrieve/import from the target instance
- B. Export from source, then retrieve in target
- C. Commit in source before export
- D. Scan Linux logs only
Answer: B

### Q56
Which scripting language is used in ServiceNow business rules, UI policies, and script includes?
- A. JSON
- B. Server-side JavaScript
- C. Python
- D. Bash
Answer: B

### Q57
What is a common use of a business rule?
- A. Setting field values automatically on insert or update
- B. Printing paper labels by default
- C. Controlling MID Server USB devices
- D. Scheduling browser zoom events
Answer: A

### Q58
Which approach keeps data migration safe and auditable? Choose 2.
- A. Import sets with transform maps and validation
- B. Embed user passwords in transform scripts
- C. Load data in small batches with error review
- D. Direct database writes through Linux CLI
Answers: A, C

### Q59
When would an admin create a script include?
- A. To host reusable server-side logic accessible from business rules and other scripts
- B. To store website CSS only
- C. To control MID Servers via bash
- D. To render Linux terminal UI
Answer: A

### Q60
A scheduled integration fails only on large payloads. Which first-step approach is best?
- A. Increase browser zoom
- B. Review timeout, batch size, and transform map performance
- C. Replace network cables
- D. Schedule Linux defrag
Answer: B
