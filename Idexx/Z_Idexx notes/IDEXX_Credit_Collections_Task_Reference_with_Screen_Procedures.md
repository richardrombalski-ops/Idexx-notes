# IDEXX Credit / Collections Task Reference

This organizes the scattered training notes into a practical workflow for a Credit / Collections support role. Some handwriting was unclear, so uncertain items are marked **Needs confirmation** instead of treated as final procedure.

---

## 1. Role Summary

The role appears to sit between **collections follow-up**, **customer payment processing**, **account/contact research**, and **account restrictions**. The main job is to determine where the customer account stands, contact or notify the right parties, process or document payment activity, and make sure holds/suspensions are handled consistently across the correct systems.

The overall process is:

1. Identify the customer/account correctly.
2. Review balance, invoices, payment status, and collection stage.
3. Confirm the right contact information.
4. Send customer communication or internal notification based on stage.
5. Process payment, payment plan, check-by-phone, credit card, ACH, or points request when applicable.
6. Document the action in GetPaid and related systems.
7. If a hold/suspension is removed, make sure all connected restrictions are also cleared.

---

## 2. Systems and What Each One Is For

### SAP

Use SAP as the accounting / A/R source of record. The notes connect SAP to invoices, accounting records, credit card payment entry, account blocks, and customer account numbers.

Likely SAP uses in this role:

- View or confirm customer account number.
- Review invoices and A/R status.
- Enter or process credit card payments through **ZOR / ZOAR**.
- Place or remove credit hold / order block.
- Final accounting record of payments and invoices.

Important note: **Credit Hold = SAP entry**. A credit hold blocks online orders by the practice and blocks IDEXX from changing or updating services, Care Plus, or standing orders.

### GetPaid / GP

Use GetPaid as the collections workbench. The notes repeatedly show GetPaid as the place to search account number, manage follow-up, use contacts, paste payment details, record comments, and stage collection activity.

Likely GetPaid uses:

- Search account by customer/account number.
- Review notes, history, previous transaction types, and collection stage.
- Manage collection follow-up.
- Store pasted payment confirmation details from Billtrust or SAP.
- Record phone calls, messages, dial attempts, and comments.
- Send or manage correspondence.

Key reminder: after processing a payment or customer contact, copy the payment/contact details into **GetPaid comments/notes**.

### Billtrust / BT / Client Connect

Use Billtrust for invoice delivery and customer payments. The notes say invoices are delivered through Billtrust and customer payments may be made through Billtrust.

Likely Billtrust uses:

- Accept ACH payments.
- Accept credit card payments, depending on workflow.
- Look up account/customer number.
- Add or update customer email address.
- Pay down oldest invoices.
- Authorize payments and get confirmation number.
- Use Client Connect to accept payment and copy details back into GetPaid.

The notes say **BT is more reliable than SF** for certain contact/email information, but Salesforce may be needed when Billtrust has no email on file.

### Salesforce / SF

Use Salesforce for customer/contact lookup and for connecting LIMS account information to SAP account information. It also appears to be used for loyalty points / DTS requests.

Likely Salesforce uses:

- Look up customer email and phone number.
- Use LIMS account number to find SAP account number for GetPaid.
- Create or apply DTS / loyalty points requests. **Needs confirmation.**

### LIMS

LIMS means **Laboratory Information Management System**. It appears to be the lab-side account number structure.

Account number pattern from notes:

- USA LIMS: smaller number, no leading zeros.
- CAD LIMS: letters plus numbers, example like **M6Q**. **Needs confirmation.**

Practice staff may know LIMS. Practice managers and AP may know SAP account numbers.

### LYNXX / LYNX

Used for lab blocks. Spelling needs confirmation.

A lab block in LYNXX means the lab work may still be tested, but results are **not released**.

### Transportation Liaison

Used for lab/courier suspension. Emailing Transportation stops courier pickups. They may reply that the account is **DIRECT**, meaning the practice mails samples using FedEx prepaid envelope rather than courier pickup.

### Telemedicine Accounts / Sales Team

At later delinquency stages, field sales and telemedicine teams may need to be notified before or during suspension. Notes reference RM, VDC, VDS, DR, VSS, and VSS Manager.

---

## 3. Account Number Reference

### SAP Account Numbers

Examples from notes:

- Older format: **0000001965** — E2VET. **Needs confirmation.**
- Newer format: **0000400000** — PTS.NART. **Needs confirmation.**

SAP numbers may include leading zeros.

### LIMS Account Numbers

- USA: smaller number, no leading zeros.
- Canada: letters and numbers, example like **M6Q**. **Needs confirmation.**

### How to Find the Right Number

If the practice gives a LIMS number, use Salesforce to locate the SAP account number, then use the SAP number in GetPaid/Billtrust as needed.

---

## 4. Standard Start-of-Task Workflow

Use this sequence when assigned an account or payment task.

### Step 1 — Identify the Customer

Confirm the account using whichever identifier is available:

- SAP customer/account number.
- LIMS account number.
- Billtrust account number.
- Customer name / practice name.
- Salesforce contact record.

If the customer gives a LIMS number, search Salesforce to find the SAP number for GetPaid.

### Step 2 — Open the Account in GetPaid

In GetPaid:

- Enter the customer number.
- Review balance, aging, notes, history, and stage.
- Check prior communications and payment activity.
- Use Notes → History → Print icon when you need transaction-type detail.

### Step 3 — Verify Contact Information

Check Billtrust first when looking for billing/email information. If no email is found:

1. Look up the customer in Salesforce.
2. Copy the customer/contact information.
3. Open the invoice/customer card area in Billtrust.
4. Uncheck **Use A/R Address For This Contact** or similar checkbox. **Exact label needs confirmation.**
5. Enter the email address.
6. Save.

Also update phone number in Salesforce when needed.

### Step 4 — Determine the Collection Stage

Use days past due and total balance to decide what action is required. For accounts under $50,000, use the stage table below.

### Step 5 — Take the Required Action

Actions may include:

- Reminder / rollover communication.
- Solve-problem communication.
- Serious delinquency warning.
- Order hold.
- Sales notification.
- Lab / telemed suspension.
- Final demand letter.
- Third-party collection referral.
- Payment plan or payment processing.

### Step 6 — Document Everything

After every action, update GetPaid with:

- What was done.
- Who was contacted.
- Date/time.
- Payment amount, method, confirmation number, and reference.
- Any customer promise or payment plan.
- Any internal notification sent.
- Any hold/suspension placed or removed.


---

## 5. Screen Procedure Checklists From Handwritten Notes

Use these when you are sitting in front of the system and need the actual screen order. These are organized from the notes as written. Anything unclear is marked **Needs confirmation** so you do not accidentally treat a half-readable note as a final rule.

### A. GetPaid — Account Lookup / Starting the Task

Use this first when assigned a customer/account task.

1. Open **GetPaid**.
2. Enter the **Customer No. / Account #**.
3. Review the account balance, aging, stage, notes, and previous activity.
4. Open **Notes → History** when you need previous payment or transaction detail.
5. Use the **Print icon** in History to bring up more detail on previous transaction types.
6. If the task involves a payment, contact, promise, hold, or unblock, plan to finish by adding a GetPaid comment.

### B. Billtrust / Client Connect — Accept Payment

Use this when the payment is being handled through **Billtrust / Client Connect**, especially ACH or Billtrust payment entry.

1. Enter the **Customer No. / Account Number**.
2. Select the correct **Customer**.
3. Choose the **first listing** if there are multiple listings and the trainer confirms this is the standard choice.
4. Select **Accept Payment**.
5. Enter the **Pay Amount / Amount**.
6. Enter the **Agent Amount** if that field is required. **Needs confirmation.**
7. Set **Reference** to **Other**.
8. Select **Pay Down Oldest**.
9. Select or enter **Pay Via**. One note says **DSMN Name**. **Needs confirmation.**
10. Add the two required checkmarks. **Needs confirmation which two boxes.**
11. Select **Authorize / Auth**.
12. Select **Save**.
13. Copy all payment/authorization information, including confirmation number.
14. Paste the information into **GetPaid**.
15. In GetPaid, add the note/comment and save.

Screen memory phrase: **Cust # → Customer → Accept Payment → Amount → Ref Other → Pay Down Oldest → Pay Via → Checkmarks → Auth/Save → Copy → Paste in GetPaid.**

### C. Billtrust / Client Connect — Basic Payment From Notes

Some notes reduce the Billtrust payment process to the short version below:

1. Enter **Account Number**.
2. Enter **Amount**.
3. Select **Accept**.
4. Copy all payment information.
5. Paste the information into **GP / GetPaid**.

Use the longer version above when you need the detailed steps.

### D. SAP — Credit Card Payment Through ZOR / ZOAR

Use this when the task specifically says the credit-card payment goes through **SAP** instead of Billtrust.

1. Open **SAP**.
2. Go to **ZOR / ZOAR** as directed.
3. Confirm the account/customer number.
4. Enter or process the credit-card payment details.
5. Copy the credit-card expiration detail if required by the process. **Needs confirmation.**
6. Copy the **confirmation number**.
7. Return to **GetPaid**.
8. Paste the payment details and confirmation into comments/notes.
9. Save the GetPaid note.

Important distinction from the notes: **Billtrust handles ACH and some CC payments; SAP ZOAR is specifically called out for CC payments. Confirm with trainer which path applies before entering the payment.**

### E. GetPaid — After Payment Documentation

Use this immediately after a payment, promise, or customer contact.

1. Go back to the account in **GetPaid**.
2. Left-click or open the action area used for notes. The notes say **Left CLK → Dial, Message, Paste in Comments**.
3. Choose the correct activity type, such as **Dial**, **Message**, or comment entry. **Exact menu names need confirmation.**
4. Paste the Billtrust/SAP payment details.
5. Include payment amount, method, confirmation number, and any reference used.
6. Add any customer promise or follow-up date.
7. Save.

Do not consider the payment task complete until the confirmation details are in GetPaid.

### F. Payment Plan Spreadsheet / Transaction Review

Use this when working from a payment-plan list or spreadsheet.

1. Get the **Account #**.
2. Get the **Payment Amount**.
3. Get the **Type**.
4. Open the account in **GetPaid**.
5. Go to **Notes → History**.
6. Select the **Print icon** to bring up detail of previous transaction types.
7. Use the history detail to confirm what kind of payment/transaction was previously used.
8. Process the current payment through Billtrust or SAP, depending on method.
9. Paste payment details back into GetPaid.

The notes contain example figures such as “32 entries × $404.00,” “32 items / $504.00,” or “32-something / $1,504.00.” Treat those as examples or unclear training notes, not a rule.

### G. Send Transactions / Change Due Date

The notes mention a screen action called **Send → Transactions**. The system appears likely to be GetPaid, but this needs confirmation.

1. Open **Send**.
2. Go to **Transactions**.
3. Change the **due date** to **7 days ahead** or **+1 week**.
4. Change the **Explanation** field.
5. Select or enter **Cash at Install / Cash on Install** if that is the required reason/type. **Needs confirmation.**
6. Send or save the transaction as directed.

Trainer question: confirm whether this changes the next follow-up date, transaction due date, or payment-plan due date.

### H. Send Correspondence to Customer / Sales Rep

Use this for fax/email correspondence, customer notifications, or sales notification. The notes mention **Right Click → SAD** and **Send Correspondence**.

1. Confirm the account is assigned to a territory, such as **VDC** or **DR**.
2. Right-click the account or action line.
3. Choose **SAD**. **Needs confirmation what SAD stands for and which screen it appears in.**
4. Select **Send Correspondence**.
5. Choose **Email** or **Fax**.
6. Select the correct template/reason, possibly **Cash at Install** where applicable. **Needs confirmation.**
7. Edit the correspondence if required.
8. Select **Send**.
9. If using **Black Book** / distribution list, set:
   - **To:** DR or assigned sales rep.
   - **CC:** yourself.
10. Return to GetPaid and document the correspondence sent.

Use this especially around collection stages where the account needs fax/email notice, sales notification, or territory rep awareness.

### I. Billtrust / Salesforce — Add or Fix Customer Email

Use this when Billtrust has no email or the billing contact needs correction.

1. Get the **Customer #**.
2. Pull up **GP Contacts**.
3. Save if the screen requires it.
4. Open **Billtrust**.
5. Look up the **Customer #**.
6. If there is no email on file, open **Salesforce**.
7. Search the customer in Salesforce.
8. Copy the customer/contact email or customer number as needed.
9. Return to Billtrust.
10. Open the **INV / Invoice** area.
11. Pull up the **Customer Card** from the upper-right area. **Screen location needs confirmation.**
12. Uncheck **Use A/R Address For This Contact** or similar checkbox.
13. Enter the email address.
14. Save.
15. If the missing email affected a collections action, note the update in GetPaid.

Reminder from notes: **BT is more reliable than SF** for some contact/payment information, but Salesforce is used when Billtrust is missing the email.

### J. Salesforce — Find SAP Number From LIMS

Use this when the practice gives a lab-side number instead of the SAP account number.

1. Take the **LIMS** account number from the practice/customer.
2. Open **Salesforce**.
3. Search the LIMS number.
4. Locate the matching customer/account.
5. Identify the **SAP account number**.
6. Use the SAP account number in **GetPaid**, **Billtrust**, or **SAP** as needed.

Account-number reminder:

- **SAP** numbers may include leading zeros.
- **USA LIMS** numbers are smaller and usually no leading zeros.
- **Canada LIMS** may be letters plus numbers, such as the unclear example **M6Q**.

### K. Check by Phone / ACH Through Billtrust

The notes connect **Check by Phone** with **ACH** and **Billtrust**.

1. Confirm the customer/account number.
2. Confirm the payment amount.
3. Open **Billtrust**.
4. Use the **ACH / Check by Phone** payment option.
5. Enter required account/payment authorization details.
6. Authorize the payment.
7. Get the confirmation number.
8. Copy all confirmation/payment information.
9. Paste into **GetPaid**.
10. Note any deadline, promise date, or “check has to get here before ___” rule if provided.

Unclear notes tied to this procedure: **LK #**, **Check In**, **10771**, and **Email**. Ask trainer before relying on those.

### L. Apply Points / Loyalty Points / DTS Request

The notes are incomplete, but this appears to be a Salesforce-based points or DTS request process.

1. Open **Salesforce**.
2. Create or apply a **DTS Request**. **Needs confirmation.**
3. Choose **Use Loyalty Points**.
4. Enter or confirm the contact/requester.
5. Apply the points to the correct invoice/account.
6. Use **CON** and **Apply** if those are the actual screen buttons. **Needs confirmation.**
7. Note the result in GetPaid if it affects payment, balance, or collections follow-up.

### M. Credit Hold / Block / Local Blocked Report

Use this around 30+ days past due or when a hold/block task is assigned.

1. Confirm the account in **GetPaid**.
2. Confirm the stage and days past due.
3. If the account reaches the order-hold stage, process or verify the **SAP credit hold/order block** as directed.
4. Send required faxes/emails/customer notifications.
5. If working from a **Local Blocked Report**, check whether the report is **WKLY** or **BKMY**. **Needs confirmation.**
6. Paste the **Order #** where required. **Needs confirmation which system/field.**
7. Document the block/hold in GetPaid.

Notes say **Block = 30** and **SAP Block after 30**, which matches the 30+ day order-hold stage.

### N. Lab Block / Lab Suspension / Reinstatement

Use this when the account action affects lab/courier or telemedicine access.

1. Confirm the account has reached the correct stage for lab/telemed action.
2. Confirm it is not Friday or the last business day of the week if suspending courier/reference lab service.
3. If blocking lab results, update **LYNXX / LYNX**. **Spelling/system path needs confirmation.**
4. Note in GetPaid: **Blocked in LYNXX — DATE**.
5. If suspending courier service, email **Transportation Liaison**.
6. Watch for Transportation’s email response.
7. If they reply that the account is **DIRECT**, note that samples are mailed by FedEx prepaid envelope rather than courier pickup.
8. Notify telemedicine accounts/team if telemed services are affected.
9. Document suspension or reinstatement in GetPaid.
10. When an account is taken off credit hold, check and fix lab/telemed restrictions too.

Critical memory phrase: **Off credit hold does not automatically mean labs are fixed. Check SAP, LYNXX, Transportation, and Telemed.**


---

## 6. Collections Aging Strategy for Accounts Under $50,000

| Days Past Due | Stage | Contact Type | Action |
|---:|---|---|---|
| 0 | Due Date | None | CAG invoices are due on the 25th day of the following month. |
| 4+ | Rollover / Reminder | Fax / Email / Call if no fax | Tell customer payment was due on the prior due date and ask them to contact IDEXX to make payment. |
| 12+ | Solve Problem | Fax / Email / Call if no fax | Tell customer payment is overdue and ask them to contact IDEXX to resolve. |
| 19+ | Serious | Fax / Email / Call if no fax | Tell customer account is delinquent. Warn that order hold may be placed if account reaches 30 days overdue. |
| 30+ | Order Hold | Fax / Email / Call if no fax | Tell customer order hold has been placed. Explain what it means and how to resolve. Consumable orders may still be placed with credit card. Warn lab/telemed may be impacted if not resolved. |
| 40+ | Lab / Telemed Suspension Pending | Email Sales | Notify field sales that suspension is pending if no resolution. Send to RM, VDC, VDS, DR, VSS, and VSS Manager. Give Sales chance to provide better contact info or extenuating circumstances. |
| 42+ | Lab / Telemed Suspension | Call customer + notify internal teams | Do not suspend reference lab/courier service on Fridays or the last business day of a week. Call customer to explain services are going on hold until overdue balance is resolved or a reasonable payment plan is in place. Notify Transportation and telemedicine teams to block in applicable systems. |
| 54+ | Request Final Demand | Physical letter | Send final demand letter giving a deadline, generally 14 days from letter date, before agency/attorney placement. |
| 69+ | Third-Party Collections | A/R form and email | Credit Specialist writes off balance and sends to third-party collection agency. |

Last updated in the source note: **05/29/2024**.

---

## 7. Payment Processing / Payment Plan Workflow

### Big Picture Flow

1. Invoice generated in SAP.
2. Invoice delivered through Billtrust.
3. Customer payment made through Billtrust or SAP, depending on method.
4. Payment/remittance processed.
5. Follow-up managed in GetPaid.
6. Accounting records finalized in SAP.

### Payment Plan Spreadsheet

Use the spreadsheet to capture or review:

- Account number.
- Payment amount.
- Type.
- Prior transaction detail via Notes → History → Print icon.

Unclear note: “32 entries × $404.00,” “32 items / $504.00,” or “32-something / $1,504.00” appears in several notes. Treat as an example, not a rule, until confirmed.

### Billtrust / Client Connect Payment Steps

Common notes show this sequence:

1. Enter customer/account number.
2. Select customer.
3. Choose first listing.
4. Select **Accept Payment**.
5. Enter payment amount.
6. Enter agent amount if required. **Needs confirmation.**
7. Set reference to **Other**.
8. Choose **Pay Down Oldest**.
9. Select payment method / Pay Via. One note says **DSMN Name**. **Needs confirmation.**
10. Check required boxes.
11. Authorize payment.
12. Save.
13. Copy all payment information / confirmation details.
14. Paste into GetPaid notes/comments.

### SAP Payment Steps

Notes reference SAP credit card payment through:

- **ZOR / ZOAR**.
- SAP → ZOAR.
- Copy credit card expiration and confirmation number. **Needs confirmation.**

Use SAP/ZOAR when the task specifically requires SAP credit card payment entry or account action.

### GetPaid Documentation After Payment

After payment:

- Paste confirmation information into GetPaid.
- Add call/message note if customer was contacted.
- Save.
- If there was a promise/payment plan, update the due date or next follow-up date.

Some notes say change due date to **7 days ahead** or **+1 week**. Confirm whether this is for follow-up date, payment-plan date, or correspondence due date.

---

## 8. Check by Phone / ACH

The notes connect “Check by Phone” with ACH and Billtrust.

Use this when a customer offers payment by phone/check/ACH.

Likely process:

1. Confirm account.
2. Confirm payment amount.
3. Use Billtrust / ACH option.
4. Enter required authorization information.
5. Get confirmation number.
6. Copy payment details to GetPaid.
7. Note whether payment/check must arrive before a specific deadline. **Deadline rule needs confirmation.**

Unclear references: “LK #,” “10771,” “Check In,” and “Email.” Treat as incomplete until clarified.

---

## 9. Contact Maintenance Workflow

Use this when customer billing/contact info is missing or wrong.

### Billtrust / Salesforce Contact Update

1. Get customer number.
2. Open GP Contacts and save if required.
3. Open Billtrust and look up customer number.
4. If no email exists, look up customer in Salesforce.
5. Copy the customer/contact info from Salesforce.
6. Open the invoice/customer card section in Billtrust.
7. Uncheck **Use A/R Address For This Contact** or similar option.
8. Enter email address.
9. Save.

Phone number appears to be updated in Salesforce.

Reminder from notes: **BT is more reliable than SF** for certain billing/contact information.

---

## 10. Credit Holds, Lab Blocks, and Lab Suspensions

### Credit Hold

A credit hold is entered in SAP. It blocks:

- Practice from placing orders online.
- IDEXX from changing/updating services, Care Plus, or standing orders.

### Lab Block

A lab block is handled in LYNXX / LYNX. Even if samples are mailed in, testing may be done, but results are not released.

### Lab Suspension

A lab/courier suspension is handled by emailing Transportation Liaison.

Effects:

- Stops courier pickup.
- Transportation replies by email.
- They may say the account is **DIRECT**, meaning samples come through FedEx prepaid envelope / mail rather than courier.

### Critical Reinstatement Rule

When an account comes off credit hold, check whether lab and telemed restrictions also need to be fixed.

Important rule from notes:

**If taken off credit hold, make sure to fix labs too.**

In GetPaid, document:

- Blocked in LYNXX + date.
- Transportation email / suspension / reinstatement.
- Any lab or telemed action taken.

---

## 11. Correspondence / Sales Notification

Some notes reference right-click → SAD and Send Correspondence. Exact system/menu needs confirmation, but this appears tied to GetPaid correspondence.

Likely correspondence options:

- Email.
- Fax.
- Cash at Install. **Needs confirmation.**
- Edit and Send.
- Black Book / distribution list. **Needs confirmation.**
- To: DR.
- CC: yourself.

Sales notification appears required when the account is assigned to territory such as VDC or DR, especially before lab/telemed suspension or certain install/cash cases.

---

## 12. Apply Credits / Loyalty Points / DTS Request

Some notes reference applying credits, Salesforce points, and loyalty points.

Possible workflow from notes:

1. In Salesforce, create or apply DTS request. **Needs confirmation.**
2. Use loyalty points.
3. Request type: use loyalty points.
4. Contact person / requester.
5. Apply to specific invoice.
6. Amount for part or parts requested by VDC. **Needs confirmation.**

This section should be verified with a trainer before use because the handwritten notes are incomplete.

---

## 13. Acronyms and Terms to Confirm

These appeared in the notes but need official definitions:

- **CAG**
- **NAFBO**
- **VDC** — notes say Sales Rep in field / sales by infield.
- **DR**
- **RM**
- **VDS**
- **VSS**
- **CGU / CAG @ Install**
- **Digital VR**
- **SAD**
- **DTS**
- **DSMN Name**
- **LYNXX vs LYNX**
- **Black Book**
- **Cash at Install**
- **STP / Stop**
- **Local Blocked Report — WKLY / BKMY**
- **BP** — possibly Business Partner in SAP.

---

## 14. Quick Reference by Task

### If assigned a past-due account

1. Search customer/account in GetPaid.
2. Review balance, aging, stage, notes, history.
3. Confirm contact info in Billtrust/Salesforce.
4. Match days past due to collection stage.
5. Send required communication.
6. Update GetPaid comments.
7. Set next follow-up date if required.

### If assigned a payment plan

1. Get account number, amount, and type from spreadsheet/task.
2. Review history in GetPaid.
3. Process payment in Billtrust or SAP/ZOAR depending on method.
4. Use reference **Other** and **Pay Down Oldest** where applicable.
5. Authorize and save.
6. Copy confirmation details.
7. Paste into GetPaid.
8. Update follow-up date or payment-plan note.

### If assigned an ACH / check-by-phone payment

1. Confirm customer/account and amount.
2. Use Billtrust ACH/check-by-phone workflow.
3. Authorize payment.
4. Get confirmation.
5. Paste all details into GetPaid.
6. Note any deadline or promise date.

### If assigned a credit card payment

1. Confirm whether payment is through Billtrust or SAP.
2. If SAP, use ZOR / ZOAR as directed.
3. Enter payment details.
4. Copy expiration/confirmation info as required.
5. Paste confirmation into GetPaid.

### If assigned missing customer email/contact update

1. Search Billtrust by customer number.
2. If email missing, search Salesforce.
3. Update Billtrust contact/email.
4. Uncheck A/R address option if required.
5. Save.
6. Note update in GetPaid if tied to collection action.

### If assigned order hold / credit hold

1. Confirm account and stage.
2. Confirm 30+ days past due / hold criteria.
3. Place or verify SAP credit hold/order block as directed.
4. Notify customer by fax/email/call.
5. Document in GetPaid.
6. Watch for related lab/telemed impact.

### If assigned lab/telemed suspension

1. Confirm account is at the correct stage, usually 42+ days past due.
2. Confirm it is not Friday or last business day of the week.
3. Call customer.
4. Notify Transportation Liaison and telemedicine team.
5. If Transportation says account is DIRECT, note direct/FedEx workflow.
6. Document suspension in GetPaid.

### If assigned reinstatement / unblock

1. Confirm payment/resolution or approved payment plan.
2. Remove SAP credit hold/order block if authorized.
3. Check lab block in LYNXX/LYNX.
4. Email Transportation / telemed teams for reinstatement if they were suspended.
5. Document all reinstatement actions in GetPaid.

---

## 15. Trainer Questions to Ask

1. What is the official spelling and login path for **LYNXX / LYNX**?
2. Which system owns final contact updates: Billtrust, Salesforce, or both?
3. What exactly does **Use A/R Address For This Contact** control?
4. When do we use Billtrust credit card payment vs SAP ZOAR credit card payment?
5. What are the exact required GetPaid comment formats after payment?
6. What is **DSMN Name** in the Pay Via field?
7. What does **SAD** stand for, and which system uses it?
8. What does **Cash at Install** mean in correspondence?
9. What are the official definitions for CAG, NAFBO, VDC, DR, VDS, VSS, RM, and CGU?
10. What are the exact rules for changing dates by +7 days or +1 week?
11. What is the proper process for check-by-phone / ACH authorization?
12. What are the exact steps for applying loyalty points / DTS requests?
13. Where is the local blocked report, and what do WKLY / BKMY mean?
14. What is the process to remove all restrictions after payment: SAP, LYNXX, Transportation, and Telemed?

---

## 16. Best Working Habit

For every assigned task, think in this order:

**Account → Stage → Contact → Payment/Hold Action → Documentation → Follow-up.**

The biggest risk in these notes is not the payment entry itself. The biggest risk is doing one part of the action and forgetting the connected system. For example, removing a SAP credit hold but forgetting lab/telemed restrictions, or taking a payment but not pasting the confirmation into GetPaid.
