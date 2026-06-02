# ServiceNow CSA — Practice Question Bank

> Based on the **Official CSA Mainline Exam Blueprint (Updated January 2026)**
> 60 questions on the real exam | 90 minutes | Passing score not publicly disclosed
> The 14 Update Set questions from your friend's renewal exam are in a separate file.

---

## Exam Domain Summary

| # | Domain | Weight | ~Questions |
|---|--------|--------|-----------|
| 1 | Platform Overview and Navigation | 7% | ~4 |
| 2 | Instance Configuration | 10% | ~6 |
| 3 | Configuring Applications for Collaboration | 20% | ~12 |
| 4 | Self-Service & Automation | 20% | ~12 |
| 5 | Database Management and Platform Security | **30%** | ~18 |
| 6 | Data Migration and Integration | 13% | ~8 |

---

## Domain 1 — Platform Overview and Navigation (7%)
> Topics: ServiceNow platform overview, platform capabilities, the ServiceNow instance, Next Experience Unified Navigation

**Q1.** Which of the following applications is available to ALL users by default in ServiceNow?
- A. Change
- B. Incident
- C. Facilities
- D. Self Service

**Q2.** Which module displays a list of tasks assigned to a user's group, but not yet assigned to an individual user?
- A. My Teams Work
- B. My Groups Work
- C. My Groups Tasks
- D. My Teams Tasks

**Q3.** What is the "Application Navigator" used for in ServiceNow?
- A. Tracking the history of record changes
- B. Accessing all installed applications and their modules
- C. Defining workflow routing logic
- D. Managing database table schemas

**Q4.** A user wants to quickly return to a frequently used module. Which feature should they use?
- A. System Properties
- B. Favorites (starred items)
- C. Update Sets
- D. The Search bar only

**Q5.** In Next Experience (Unified Navigation), where does a user go to set personal preferences such as time zone, language, and theme?
- A. System Properties > User Preferences
- B. User Administration > User Profile
- C. The Profile menu (avatar/name in the top-right)
- D. System Settings > Global

**Q6.** What is the "Service Portal" in ServiceNow?
- A. A consumer-friendly web interface for end users to submit requests, search knowledge, and track tickets — separate from the backend admin UI
- B. An admin portal for managing MID Servers and plugins
- C. A reporting portal for generating compliance reports
- D. A portal used only for change management approvals

---
### Domain 1 — Answers

| Q | Answer | Explanation |
|---|--------|-------------|
| Q1 | D | Self Service is the only app available to all users by default |
| Q2 | B | "My Groups Work" = group queue not yet assigned to an individual |
| Q3 | B | Application Navigator = left sidebar with all apps/modules |
| Q4 | B | Favorites (star icon) = bookmarks for quick navigation |
| Q5 | C | Personal preferences live in the user profile menu |
| Q6 | A | Service Portal = self-service front end for non-admin users |

---

## Domain 2 — Instance Configuration (10%)
> Topics: Installing applications and plugins, personalizing/customizing the instance, common user interfaces in the Platform

**Q7.** What is a "Plugin" in ServiceNow?
- A. An optional feature or application that can be activated via the Plugin Manager to extend platform functionality
- B. A third-party JavaScript library embedded in a client script
- C. A MID Server extension for protocol translation
- D. A widget added to the Service Portal

**Q8.** What is the purpose of "System Properties" (sys_properties)?
- A. Read-only metadata about the current platform version
- B. Global key-value configuration settings that control platform and application behavior without code changes
- C. A log of all system events for audit purposes
- D. The definition of field types in the database dictionary

**Q9.** What is "Instance Scan" used for?
- A. Scanning the CMDB for stale CI records
- B. Automatically analyzing instance configurations to detect risk patterns and best practice violations
- C. Auditing user login sessions and IP addresses
- D. Scanning Update Set XML for conflicts before committing

**Q10.** A ServiceNow admin wants to copy the production instance's data and configuration onto a development instance. What process does this describe?
- A. Export/Import via Update Sets
- B. Instance Cloning
- C. Data Migration via Import Sets
- D. Plugin synchronization

**Q11.** What is a "MID Server"?
- A. A secondary ServiceNow instance used for load balancing
- B. A Java application installed on a customer's on-premises network that allows the cloud instance to communicate with resources behind the firewall
- C. A caching layer between the browser and the ServiceNow instance
- D. A middleware that converts REST calls to SOAP for legacy integrations

**Q12.** A ServiceNow admin wants to personalize a list by changing which columns are displayed. What feature allows this?
- A. Form Designer
- B. List Personalization (gear icon or right-click column header)
- C. Dictionary Override
- D. System Properties

---
### Domain 2 — Answers

| Q | Answer | Explanation |
|---|--------|-------------|
| Q7 | A | Plugin = optional feature activated via Plugin Manager |
| Q8 | B | System Properties = global key-value config settings |
| Q9 | B | Instance Scan = finds risk patterns and best practice violations |
| Q10 | B | Cloning = copy prod to sub-prod instance |
| Q11 | B | MID Server = on-prem Java agent bridging cloud to LAN |
| Q12 | B | List Personalization = personal column display customization |

---

## Domain 3 — Configuring Applications for Collaboration (20%)
> Topics: Lists, Filters, and Tags; List and Form anatomy; Form Configuration; Form templates and saving options; Advanced Form Configuration; Task Management; Visual Task Boards (VTBs); Visualizations, Dashboards, and Platform Analytics; Notifications

**Q13.** In a ServiceNow list, what is the purpose of the "breadcrumb" filter at the top?
- A. It shows the navigation path (application > module) for quick back-navigation
- B. It displays the active filter conditions applied to the list and allows quick removal
- C. It defines which columns are shown in the list
- D. It indicates the update set that last modified the records

**Q14.** What does "grouping" records in a list do?
- A. Merges duplicate records into one
- B. Organizes list rows into collapsible sections based on a chosen field value
- C. Applies a mandatory permanent filter
- D. Exports records grouped by field to a CSV

**Q15.** Which of the following correctly describes a "View" on a ServiceNow form?
- A. A saved condition that filters which records are shown in a list
- B. A specific arrangement of fields on a form designed for a particular role or context
- C. A dashboard tab combining multiple reports
- D. A read-only snapshot of a record at a specific point in time

**Q16.** What is a "Form Template" in ServiceNow used for?
- A. Designing the visual layout of a dashboard
- B. Pre-populating a new record's fields with saved default values to speed up data entry
- C. Creating a reusable workflow stage
- D. Defining required fields for import sets

**Q17.** What is the purpose of "Tags" in ServiceNow?
- A. Labels that can be applied to records to help users organize and find related records across different tables
- B. Labels applied to fields to mark them as mandatory
- C. System-defined categories used in the Service Catalog
- D. Metadata markers on Update Set records

**Q18.** Which of the following best describes a Visual Task Board (VTB) in ServiceNow?
- A. A Kanban-style board interface for visualizing and managing tasks across lanes/stages
- B. A reporting dashboard that aggregates task metrics
- C. A form layout editor for task records
- D. A workflow diagram showing approval stages

**Q19.** What are the three types of Visual Task Boards (VTBs)? *(Choose 3)*
- A. Freeform boards — display any task records; members can manually add/remove cards and define lanes
- B. Flexible boards — filter-driven cards removed automatically when tasks no longer match; custom lanes allowed
- C. Guided boards — lanes correspond to field values (e.g., State) and cannot be manually edited
- D. Static boards — read-only snapshots of task states
- E. Report boards — generated from a PA indicator

**Q20.** What is the difference between a "Report" and a "Dashboard" in ServiceNow?
- A. A report is a single data visualization; a dashboard aggregates multiple reports and widgets onto one page
- B. Reports are admin-only; dashboards are for all users
- C. Reports use PA indicators; dashboards use table data only
- D. Reports run on-demand; dashboards update automatically only

**Q21.** By default, who can see a report after it has been created?
- A. All users on the instance
- B. Only the report creator — it must be explicitly shared
- C. All users with the itil role
- D. All members of the creator's assignment group

**Q22.** Which report type is best for showing the proportion of open incidents by category?
- A. Time Series
- B. Gauge
- C. Pie/Donut chart
- D. Single Score

**Q23.** What does "Performance Analytics" add beyond basic table reports?
- A. The ability to collect indicator data over time and track KPI trends historically; standard reports only show a point-in-time snapshot
- B. Real-time streaming from external BI tools
- C. AI-powered narrative summaries of trend data
- D. Automated export to PowerPoint

**Q24.** What is an "Email Notification" in ServiceNow?
- A. An automated email triggered by a defined record event or condition and sent to specified recipients
- B. An inbound action that converts incoming emails into records
- C. A scheduled batch email report sent to all admins
- D. A notification sent only when a record is manually flagged

**Q25.** What are "Work Notes" vs "Additional Comments" on a task record?
- A. Both are visible to all users including customers
- B. Work Notes are internal (visible to agents/groups); Additional Comments are customer-facing
- C. Work Notes require approval to add; Additional Comments do not
- D. Work Notes are sent by email automatically; Additional Comments are not

**Q26.** What is the purpose of an SLA (Service Level Agreement) on a task?
- A. A commitment that defines time targets for response and/or resolution of a task; triggers escalations when breached
- B. A role required to close an incident
- C. A catalog item for requesting service agreements
- D. A business rule that runs when a task is assigned

---
### Domain 3 — Answers

| Q | Answer | Explanation |
|---|--------|-------------|
| Q13 | B | Breadcrumb filter = shows active filter conditions, easy to remove |
| Q14 | B | Grouping = collapses list into sections by a field value |
| Q15 | B | View = form field arrangement for a role/context |
| Q16 | B | Form Template = saved field defaults to speed up record creation |
| Q17 | A | Tags = labels to organize/find records across tables |
| Q18 | A | VTB = Kanban-style board for task visualization |
| Q19 | A, B, C | Three types: Freeform, Flexible, Guided |
| Q20 | A | Report = single viz; Dashboard = collection of reports/widgets |
| Q21 | B | Reports are private by default; creator must share |
| Q22 | C | Pie/Donut = proportion/distribution chart |
| Q23 | A | PA = historical trend collection; reports are point-in-time only |
| Q24 | A | Email Notification = event-driven automated email |
| Q25 | B | Work Notes = internal; Additional Comments = customer-visible |
| Q26 | A | SLA = time target + escalation on breach |

---

## Domain 4 — Self-Service & Automation (20%)
> Topics: Knowledge Management, Service Catalog, Workflow Studio, Virtual Agent

**Q27.** What is a "Knowledge Base" in ServiceNow used for? *(Choose 2)*
- A. Storing articles that help users and agents find solutions and answers without opening tickets
- B. Storing CI configuration data for the CMDB
- C. Reducing repeat incidents by deflecting users to self-service answers
- D. Automating approval routing for change requests

**Q28.** Which role is typically required to publish a knowledge article in ServiceNow?
- A. admin
- B. knowledge or knowledge_admin
- C. itil
- D. catalog_admin

**Q29.** What controls which users can see a specific Knowledge Base or Service Catalog item?
- A. ACL rules on the kb_knowledge table
- B. User Criteria
- C. Business Rules with role conditions
- D. System Properties

**Q30.** In the Service Catalog, what is a "Catalog Item"?
- A. A predefined offering (e.g., new laptop, software access) that end users can request
- B. A configuration record containing workflow routing logic
- C. A report showing pending service request fulfillment status
- D. A role granting access to submit service requests

**Q31.** What record is created when a user submits a Service Catalog request?
- A. An Incident (inc)
- B. A Request (sc_request) containing one or more Requested Items (sc_req_item)
- C. A Task (task) and a Change Request (change_request)
- D. A Problem (problem) and a Service Request (sc_task)

**Q32.** Multiple Choice, Single Line Text, and Select Box are what type of elements in ServiceNow?
- A. Order Guides
- B. Request Types
- C. Variable Types
- D. Related Lists

**Q33.** What is an "Order Guide" in the Service Catalog?
- A. A bundle of related catalog items ordered together as a package
- B. The step-by-step help text shown when a user opens a catalog item
- C. The SLA definition for service fulfillment times
- D. The approval chain for a catalog request

**Q34.** In Flow Designer (Workflow Studio), what is the difference between a "Flow" and a "Subflow"?
- A. A Flow is triggered by an event, schedule, or service catalog item; a Subflow is a reusable logic component called from within a flow or other subflows
- B. Flows run client-side; Subflows run server-side
- C. Flows are limited to one application scope; Subflows can be global
- D. Flows require scripting; Subflows are no-code only

**Q35.** Which of the following can trigger a Flow Designer flow? *(Choose 2)*
- A. A record being created or updated
- B. A scheduled date/time or recurring interval
- C. A MID Server heartbeat event
- D. A plugin being activated

**Q36.** What is Virtual Agent in ServiceNow?
- A. An AI-powered chatbot platform that provides user assistance through automated conversations, helping users get information and complete tasks without agent involvement
- B. A background automation that runs scripts on a schedule
- C. An agent desktop tool that suggests answers to live agents
- D. A testing framework for validating workflow automations

**Q37.** Virtual Agent topics can be authored using which of the following? *(Choose 2)*
- A. Virtual Agent Designer (drag-and-drop graphical canvas)
- B. NLU (Natural Language Understanding) for intent recognition
- C. Import Sets to load conversation scripts from Excel
- D. Transform Maps to define conversation branching rules

**Q38.** What does Virtual Agent "deflection" mean?
- A. Routing a ticket to a different assignment group
- B. Resolving a user's issue through the chatbot so that no human agent ticket is created
- C. Redirecting a user from the Service Portal to the backend UI
- D. Moving a conversation from Virtual Agent to email

---
### Domain 4 — Answers

| Q | Answer | Explanation |
|---|--------|-------------|
| Q27 | A & C | KB = self-service answers + incident deflection |
| Q28 | B | knowledge or knowledge_admin role required to publish |
| Q29 | B | User Criteria = visibility rules for KB and catalog items |
| Q30 | A | Catalog Item = requestable offering in the service catalog |
| Q31 | B | sc_request = parent; sc_req_item = one per catalog item ordered |
| Q32 | C | Variable Types = field types on catalog item request forms |
| Q33 | A | Order Guide = bundled catalog items ordered as a package |
| Q34 | A | Flow = triggered automation; Subflow = reusable component |
| Q35 | A & B | Record triggers and scheduled triggers are the core types |
| Q36 | A | Virtual Agent = AI chatbot for user self-service |
| Q37 | A & B | VA Designer + NLU are the two authoring mechanisms |
| Q38 | B | Deflection = user resolved by bot, no ticket needed |

---

## Domain 5 — Database Management and Platform Security (30%)
> Topics: Data Schema, Application/Access Control, Importing Data, CMDB and CSDM, Security Center, Shared Responsibility Model

**Q39.** In ServiceNow, what is a "Table"?
- A. A collection of records where each row is a record and each column is a field
- B. A grouping of workflow stages for a process
- C. A container for Update Set configuration changes
- D. A form layout template

**Q40.** Which table is the parent (base) for Incident, Problem, and Change Request?
- A. sys_metadata
- B. cmdb_ci
- C. task
- D. sys_user

**Q41.** What does it mean for one table to "extend" another?
- A. The child table inherits all fields from the parent and can add its own unique fields
- B. The child table copies the parent's records on a nightly schedule
- C. The child table's records replace the parent's records when deployed
- D. The child table holds a foreign key reference to the parent's primary key only

**Q42.** What is the "sys_id" of a record?
- A. The display name field shown in reference dropdowns
- B. A globally unique identifier (GUID) automatically assigned to every record in every table
- C. The internal name of a table
- D. The primary key used only on the task table

**Q43.** Which field type stores a link to a record in another table and displays that record's display value?
- A. String
- B. Integer
- C. Reference
- D. Choice

**Q44.** What is a "Dictionary Override" used for?
- A. Changing the attributes of a field (e.g., making it mandatory) on an extended/child table without modifying the parent table's field definition
- B. Overriding an ACL rule for a specific application scope
- C. Renaming a table in a specific language
- D. Replacing a field's display value with a calculated value

**Q45.** What is an Access Control (ACL) rule used for?
- A. Defining which roles can read, write, create, or delete records and fields in a table
- B. Encrypting data as it moves between instances
- C. Scheduling which users can log in during specific hours
- D. Controlling which fields are exported in an Update Set

**Q46.** Which of the following correctly describes an ACL rule's evaluation order?
- A. Field-level ACLs are checked first, then record-level ACLs, then table-level ACLs
- B. Table-level ACLs first, then record-level, then field-level — the most specific level wins
- C. All ACL types are evaluated simultaneously and the first match applies
- D. Only one level (table, record, or field) can exist per table at a time

**Q47.** What does the "admin" role grant in ServiceNow?
- A. Full unrestricted access to all platform features, tables, and configuration; admins can override ACLs
- B. Read-only access to all tables for auditing purposes
- C. Permission to manage user accounts and groups only
- D. Access limited to the Service Portal and self-service modules

**Q48.** How are roles typically granted to users? *(Choose 2)*
- A. Assigned directly on the user's record
- B. Inherited through membership in a group that has the role assigned
- C. Automatically assigned based on the user's department field value
- D. Deployed by running an Update Set on the production instance

**Q49.** What is the purpose of an "Import Set" in ServiceNow?
- A. A staging table that holds data imported from an external source before it is transformed into a target ServiceNow table
- B. A container for moving configuration changes between instances
- C. A scheduled job extracting CMDB data nightly
- D. A method for exporting records to an external system

**Q50.** What is a "Transform Map" used for?
- A. Defining how each field in an Import Set table maps to a field in the target ServiceNow table
- B. Converting Update Set XML from one format to another
- C. Translating UI labels into different languages
- D. Mapping CI relationships between CMDB classes

**Q51.** What is the definition of Transform Maps in ServiceNow?
- A. A map used to store the history of incident records
- B. A map used to add data to encrypted fields
- C. A map used to trigger Business Rules before data is queued in an outbound web service
- D. A map to determine relationships between fields in an Import Set and fields in an existing table

**Q52.** What is a "Coalesce" field in a Transform Map?
- A. A field that prevents duplicate records by matching incoming import data against existing records
- B. A required field that must be present for a transform to execute
- C. A field that combines multiple source columns into one target field
- D. A field that triggers a post-transform business rule

**Q53.** What is the CMDB (Configuration Management Database) used for in ServiceNow?
- A. Storing and managing configuration items (CIs) and their relationships to support IT service management
- B. Staging imported data before transformation
- C. Archiving closed incident records for compliance
- D. Storing Update Set deployment history

**Q54.** Which of the following are examples of CI classes in the CMDB? *(Choose 2)*
- A. cmdb_ci_server (Server)
- B. sys_user (User)
- C. cmdb_ci_appl (Application)
- D. sc_request (Service Catalog Request)

**Q55.** What is the "Common Service Data Model" (CSDM) in ServiceNow?
- A. A standard framework and data model that defines how business services, technical services, and CIs relate to each other across the CMDB
- B. A plugin for importing external customer data into the CMDB
- C. A reporting model for service desk KPIs
- D. A data schema for the Service Catalog variables

**Q56.** What is the "Security Center" (formerly Instance Security Center) used for?
- A. A consolidated dashboard for monitoring instance security compliance, viewing security events, configuring hardening settings, and managing user sessions
- B. A marketplace for approved security plugins
- C. A tool for scanning Update Sets for malicious scripts before commit
- D. A report generator for PCI audit evidence

**Q57.** What is the "Daily Compliance Score" in the Security Center?
- A. A percentage score indicating how compliant the instance's security property settings are with recommended hardening guidelines
- B. A count of failed login attempts in the last 24 hours
- C. The percentage of incidents resolved within SLA in the past day
- D. A daily export of the instance's ACL configuration to a compliance team

**Q58.** What does the "Shared Responsibility Model" mean in the context of ServiceNow cloud security?
- A. ServiceNow is responsible for the security of the cloud infrastructure; the customer is responsible for configuring and securing their instance (data, access controls, integrations, customizations)
- B. ServiceNow and the customer share equal responsibility for all security decisions
- C. The customer is fully responsible for all security, including the underlying cloud infrastructure
- D. ServiceNow handles all instance security automatically; no customer action is required

---
### Domain 5 — Answers

| Q | Answer | Explanation |
|---|--------|-------------|
| Q39 | A | Table = rows (records) and columns (fields) in the database |
| Q40 | C | `task` is the parent of incident, problem, change, request |
| Q41 | A | Extending = inheritance; child gets all parent fields + its own |
| Q42 | B | sys_id = GUID assigned to every record in every table |
| Q43 | C | Reference field = pointer to a record in another table |
| Q44 | A | Dictionary Override = modify inherited field on child table only |
| Q45 | A | ACL = who can read/write/create/delete on tables or fields |
| Q46 | B | Most specific wins: table → record → field |
| Q47 | A | admin = full platform access, can override ACLs |
| Q48 | A & B | Direct assignment or inherited via group |
| Q49 | A | Import Set = staging table before transform |
| Q50 | A | Transform Map = field mapping from staging to target table |
| Q51 | D | Official blueprint sample answer: field relationships Import Set → target |
| Q52 | A | Coalesce = match key to prevent duplicate imports |
| Q53 | A | CMDB = authoritative CI inventory + relationships |
| Q54 | A & C | cmdb_ci_server and cmdb_ci_appl are CI classes |
| Q55 | A | CSDM = standard model defining how services and CIs relate |
| Q56 | A | Security Center = compliance + events + hardening + sessions |
| Q57 | A | Daily Compliance Score = % of hardening properties correctly configured |
| Q58 | A | ServiceNow secures the platform; customer secures their instance |

---

## Domain 6 — Data Migration and Integration (13%)
> Topics: UI Policies, Business Rules, System Update Sets, Scripting in ServiceNow

**Q59.** What is the scripting language used in ServiceNow?
- A. Java
- B. AngularJS
- C. JavaScript
- D. Jelly

**Q60.** What is a "Business Rule" in ServiceNow?
- A. A server-side script that runs when a record is displayed, inserted, updated, or deleted, or when a table is queried
- B. A client-side script that validates fields before form submission
- C. A scheduled job that runs on a defined interval
- D. A configuration record that defines escalation paths

**Q61.** A Business Rule is configured with "When = before" and "Insert = true". When does this rule execute?
- A. Before the form is displayed to the user
- B. After the user submits the form and after the record is saved to the database
- C. After the user submits the form but before the record is saved to the database
- D. Only when triggered manually by a script

**Q62.** Which of the following are valid "When" settings for a Business Rule? *(Choose 2)*
- A. Before
- B. Inline
- C. After
- D. On Submit

**Q63.** What global variable in a Business Rule refers to the current state of the record being acted upon?
- A. `g_form`
- B. `gs`
- C. `current`
- D. `previous`

**Q64.** What does the global variable `previous` refer to in a Business Rule?
- A. The state of the record before any updates made in the current transaction — available on update and delete operations only
- B. The record that was last saved by any user
- C. The parent record of the current record
- D. The prior version of the business rule script

**Q65.** What is a "UI Policy" in ServiceNow?
- A. A server-side rule that enforces mandatory fields at the database level regardless of access method
- B. A no-code configuration that dynamically controls form field behavior (mandatory, read-only, hidden) based on conditions in the browser
- C. A policy that defines which users can access a specific module
- D. A visual theme setting for the Service Portal

**Q66.** What is the key difference between a "UI Policy" and a "Data Policy"?
- A. UI Policies apply only in the browser (forms); Data Policies enforce field rules at the database level and apply regardless of access method (forms, APIs, imports)
- B. UI Policies are server-side; Data Policies are client-side
- C. UI Policies apply to all tables; Data Policies apply only to custom tables
- D. UI Policies set field visibility; Data Policies set record-level security

**Q67.** In which state must an Update Set be before it can be exported from a source instance?
- A. In Progress
- B. Ignored
- C. Complete
- D. Committed

**Q68.** What is the correct order of steps for moving a completed Update Set from Instance A to Instance B?
- A. Export from A → Preview in B → Commit in B → Import into B
- B. Export from A → Import (or Retrieve) into B → Preview in B → Commit in B
- C. Commit in A → Export from A → Import into B → Preview in B
- D. Import into B → Export from A → Preview in B → Commit in B

**Q69.** Which of the following record types are automatically captured by an Update Set? *(Choose 2)*
- A. Business Rules
- B. Incident records (actual ticket data)
- C. UI Policies
- D. User password records

**Q70.** What is a "Script Include" in ServiceNow?
- A. A reusable server-side JavaScript library that can be called from business rules, client scripts (via GlideAjax), and other server-side scripts
- B. A tag that embeds an external JavaScript file into a form
- C. A client-side script that runs on every page load
- D. A scheduled script that executes daily

---
### Domain 6 — Answers

| Q | Answer | Explanation |
|---|--------|-------------|
| Q59 | C | JavaScript is the scripting language in ServiceNow (official blueprint sample Q5) |
| Q60 | A | Business Rule = server-side script on record events |
| Q61 | C | "Before" = after form submit but BEFORE database write |
| Q62 | A & C | Valid: Before, After, Async, Display — not "Inline" or "On Submit" |
| Q63 | C | `current` = the record being processed right now |
| Q64 | A | `previous` = state before the current transaction (update/delete only) |
| Q65 | B | UI Policy = no-code, browser-side field behavior control |
| Q66 | A | UI Policy = browser only; Data Policy = database-level, all access methods |
| Q67 | C | Must be "Complete" before export/retrieve |
| Q68 | B | Export → Import → **Preview** → Commit (never skip Preview) |
| Q69 | A & C | Update Sets capture config (business rules, UI policies) — NOT data |
| Q70 | A | Script Include = reusable server-side JS library |

---

## Quick Reference: Key Tables

| Table | Contents |
|-------|----------|
| `task` | Parent of all task records |
| `incident` | Incident records |
| `change_request` | Change requests |
| `sc_request` | Service Catalog request (parent) |
| `sc_req_item` | Requested Item (one per catalog line item) |
| `sc_task` | Catalog fulfillment tasks |
| `sys_user` | User records |
| `sys_user_group` | Groups |
| `sys_choice` | Choice list values |
| `cmdb_ci` | Base CI class |
| `sys_update_xml` | Individual changes inside an Update Set |
| `sys_update_set` | Update Set header records |
| `sys_trigger` | Scheduled Jobs |
| `sys_properties` | System Properties |
| `kb_knowledge` | Knowledge articles |

---

## Quick Reference: Key Roles

| Role | What it grants |
|------|----------------|
| `admin` | Full platform access; can override ACLs |
| `itil` | Core ITSM — incidents, problems, changes |
| `catalog_admin` | Manage service catalog |
| `knowledge_admin` | Manage knowledge bases |
| `report_admin` | Manage all reports |
| `security_admin` | Elevated security — must be manually activated per session |
| `user_admin` | Manage users, groups, roles |
| `import_admin` | Manage import sets and transform maps |
| `virtual_agent_admin` | Configure Virtual Agent and topics |

---

## Sample Questions from Official Blueprint (for reference)

| # | Question | Answer |
|---|----------|--------|
| 1 | Which app is available to ALL users? | D. Self Service |
| 2 | Module showing group tasks not yet assigned to an individual? | B. My Groups Work |
| 3 | What are Transform Maps? | D. Map fields from Import Set to an existing table |
| 4 | Multiple Choice, Single Line Text, Select Box are what type of elements? | C. Variable Types |
| 5 | What language is used for scripting in ServiceNow? | C. JavaScript |

---

*Total: 70 questions across all 6 official domains + the 14 Update Set renewal questions = 84 questions total.*
*Focus most study time on Domain 5 (30%) and Domains 3 & 4 (20% each).*


---

# ServiceNow CSA Practice — Blueprint-Aligned Questions
Purpose: Generate practice items mapped to the official CSA Mainline Exam Blueprint domains and weighting.
Documentation basis: `Faajaa-Share\ServiceNow\ServiceNowDocs\llms.txt`, `Faajaa-Share\ServiceNow\ServiceNowDocs\README.md`

---

## Domain 1 — Platform Overview and Navigation (7%)

### Item 1-1
**What type of URL is associated with a ServiceNow instance in Next Experience Unified Navigation?**

- A. `/login.do`
- B. A branded instance URL pointing to the customer instance
- C. `/nav_to.do`
- D. `/index.jsp`

**Answer:** B  
**Explanation:** An instance URL identifies the customer’s specific instance and is the base for unified navigation.

---

## Domain 2 — Instance Configuration (10%)

### Item 2-1
**Why would an administrator install an application or plugin on a ServiceNow instance?**

- A. To patch the operating system image
- B. To add new platform capabilities such as HR、ITSM or SecOps functionality
- C. To connect to third-party email providers only
- D. To delete system properties safely

**Answer:** B  
**Explanation:** Applications/plugins extend the instance with new tables, logic, and UX.

---

## Domain 3 — Configuring Applications for Collaboration (20%)

### Item 3-1
**List anatomy and form configuration**
**A best practice for improving list performance is to:**

- A. Increase list size to 500 rows by default
- B. Add as many reference columns as possible
- C. Use list layouts and avoid returning unnecessary columns
- D. Disable all client-side filtering

**Answer:** C  
**Explanation:** Efficient lists are built with filtered columns and minimal returned fields.

---

## Domain 4 — Self Service & Automation (20%)

### Item 4-1
**Knowledge Management**
**Why is a Knowledge article lifecycle important?**

- A. It prevents authors from ever retiring old articles
- B. It ensures users see accurate, current content reflected by review and expiry states
- C. It guarantees every article gets 10k views
- D. It removes article attachments automatically

**Answer:** B  
**Explanation:** Lifecycle workflows maintain trusted publication states for knowledge content.

---

## Domain 5 — Database Management and Platform Security (30%)

### Item 5-1
**Security Center and Shared Responsibility Model**
**In the ServiceNow Shared Responsibility Model, who manages the physical infrastructure hosting ServiceNow instances?**

- A. Customer
- B. ServiceNow
- C. Third-party cloud integrator
- D. Customer’s IT department only

**Answer:** B  
**Explanation:** ServiceNow manages platform infrastructure; customers manage instance configuration and data.

---

## Domain 6 — Data Migration and Integration (13%)

### Item 6-1
**System Update Sets**
**The primary reason to use Update Sets instead of manual UI changes in each instance is to:**

- A. Speed up browser rendering
- B. Provide repeatable, auditable configuration deployment
- C. Change user passwords automatically
- D. Build integrations to cloud vendors

**Answer:** B  
**Explanation:** Update Sets capture config metadata for portable, repeatable deployment.

---

## Practice Generation Notes
- Question count is intentionally lower than 60 so the set can be expanded iteratively.
- Next additions should preserve: 1 question per domain snapshot, 1 multiselect, 1 scenario-based debugging question.


---

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
