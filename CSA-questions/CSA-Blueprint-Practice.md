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
