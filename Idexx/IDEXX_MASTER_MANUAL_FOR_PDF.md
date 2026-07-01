# IDEXX Credit Specialist Complete Reference Manual

**Version 1.0 | July 1, 2026**

---

## TABLE OF CONTENTS

### 📋 Quick Reference
1. [Quick Start Guide](#quick-start-guide)
2. [Key Systems Summary](#key-systems-summary)
3. [Account Numbers at a Glance](#account-numbers-at-a-glance)

### 🎯 Core Processes
4. [Daily Workflows](#daily-workflows)
5. [Payment Processing](#payment-processing)
6. [Collections & Follow-Up](#collections--follow-up)
7. [Collections Call Script (Over 60 Days)](#collections-call-script-over-60-days)

### ⚙️ Detailed Procedures
8. [Account Management in SAP](#account-management-in-sap)
9. [Credit Hold & Lab Suspension](#credit-hold--lab-suspension)
10. [Payment Methods & Systems](#payment-methods--systems)
11. [Bank Memo Notices](#bank-memo-notices)
12. [Statement Management](#statement-management)
13. [Interest Reversal](#interest-reversal)

### 📞 Communication Templates
14. [Call Scripts](#call-scripts)
15. [Email/Fax Templates](#emailfax-templates)

### 📖 Reference Materials
16. [System Navigation Guide](#system-navigation-guide)
17. [Troubleshooting](#troubleshooting)
18. [Glossary & Definitions](#glossary--definitions)

---

## QUICK START GUIDE

### First Steps with Any Account

When you receive an account to work on:

1. **Identify the Account** 
   - Locate using: SAP#, LIMS#, practice name, or Billtrust#
   
2. **Find the SAP Number** 
   - If only LIMS#: Search Salesforce → note SAP#
   - Use SAP# in GetPaid
   
3. **Open in GetPaid** 
   - Search by SAP account number
   - Review: balance, aging, collection stage, all notes
   
4. **Verify Contact Info** 
   - Primary: Billtrust (most reliable)
   - Fallback: Salesforce
   - Last resort: Practice manager or AP staff
   
5. **Determine Next Action** 
   - Reference: Days Past Due strategy below
   
6. **Document Everything** 
   - Who, what, when, contact info
   - Payment details and confirmation numbers
   - Next follow-up date

---

## KEY SYSTEMS SUMMARY

### The Five Core Systems

| System | Purpose | Primary Uses |
|--------|---------|--------------|
| **GetPaid** | Collections workbench | Account lookup, follow-up, payment documentation, notes |
| **SAP** | Accounting & AR system | Invoices, holds, ZOAR (CC payments), accounting records |
| **Billtrust** | Invoice delivery & payments | ACH processing, CC payments, customer contact info |
| **Salesforce** | Customer research & lookup | LIMS → SAP connection, emails/phones, loyalty points |
| **LIMS** | Lab account numbers | Practice-side account identifiers |

### System Connections Map

```
Practice has: LIMS number
     ↓ (Search in Salesforce)
Find: SAP number
     ↓ (Use in GetPaid)
Work with: Account balance, notes, contacts
     ↓ (Update in)
Document: Payment details in GetPaid
```

---

## ACCOUNT NUMBERS AT A GLANCE

### SAP Account Numbers
Used in: GetPaid, SAP, Billtrust (always use this format)
- **Older format**: `0000001965` (E2VET)
- **Newer format**: `0000400000` (PTS.NART)
- Always includes leading zeros

### LIMS Account Numbers
Laboratory Information Management System (used by practice's lab)
- **USA format**: Small number, no leading zeros (e.g., `1965`)
- **Canada format**: Letters + numbers (e.g., `M5Q`)

### How to Match Them
1. Get LIMS from customer → Search Salesforce
2. Salesforce shows corresponding SAP#
3. Use SAP# in GetPaid and other IDEXX systems

---

## DAILY WORKFLOWS

### Workflow 1: Account Check-In

**When:** You're assigned an account to review

**Step 1: Identify & Open**
- Locate SAP account number (use Salesforce if needed)
- Search GetPaid for the account
- Open the account record

**Step 2: Review Status**
- Current balance
- Aging buckets (days past due)
- All prior notes
- Collection stage

**Step 3: Assess**
- Recent payment pending?
- Holds in place?
- Collection history?
- Recently contacted?

**Step 4: Next Action**
- Refer to [Collections & Follow-Up](#collections--follow-up) table
- Follow stage-based contact strategy

---

### Workflow 2: Processing a Payment

**When:** Customer submits payment (ACH, CC, or check)

**Step 1: Receive & Confirm**
- Get payment details from Billtrust or customer
- Confirm method: ACH → Billtrust | CC → SAP/Billtrust | Check → Note details

**Step 2: Document in GetPaid**
- Open account in GetPaid
- Copy all confirmation details into notes:
  - Payment method
  - Amount
  - Confirmation number
  - Payment date
  - Bank/processor reference (if ACH)

**Step 3: Verify Posting**
- Check GetPaid balance reflects payment
- CC payments: 1-2 days to post
- ACH payments: 1-2 business days

**Step 4: Follow-Up if Needed**
- If payment promised but not received, escalate per collection strategy
- If partial: note which invoices were cleared

---

### Workflow 3: Setting Up a Payment Plan

**Step 1: Gather Information**
- Account number
- Total outstanding balance
- Proposed payment amount & frequency
- Customer contact

**Step 2: Review Payment History**
- Check GetPaid notes and history
- Use Print icon to view transaction types
- Confirm account hasn't missed plans before

**Step 3: Enter Payment Plan**
- Use Billtrust or SAP (ZOAR screen)
- Schedule payments with dates
- Get confirmation number

**Step 4: Document & Confirm**
- Paste all details in GetPaid notes
- Send written confirmation to customer
- Reference plan in all communications

**Step 5: Monitor**
- Note due dates in GetPaid
- Set reminders for follow-up
- Update as payments post

---

### Workflow 4: Removing Holds & Suspensions

**Important:** Credit Hold in SAP blocks online orders and prevents service updates.

**Step 1: Verify Payment Current**
- Confirm past-due amount is paid
- Check GetPaid balance is $0 or acceptable
- Verify SAP shows account current

**Step 2: Remove Credit Hold in SAP**
- Open SAP → Account
- Remove credit hold flag
- Save changes

**Step 3: If Lab/Telemedicine Suspended**
- Notify Transportation Liaison (courier can resume)
- Notify Telemedicine Accounts team (services can resume)
- Document in GetPaid

**Step 4: Document**
- Log hold removal date
- Note systems updated
- Update GetPaid comments

**⭐ CRITICAL:** If removing credit hold, always check for lab blocks too!

---

## PAYMENT PROCESSING

### Credit Card Payments

**System:** SAP → ZOAR screen
**Used for:** One-time payments or CC payment plans

**Process:**
1. Get from customer: Card#, Exp, CVV, Name, Billing ZIP
2. In SAP, open ZOAR transaction
3. Enter payment details
4. Verify amount & account
5. Submit payment
6. Get confirmation# and verify posting
7. Paste confirmation in GetPaid notes

---

### ACH / Check-by-Phone Payments

**System:** Billtrust / Client Connect
**Used for:** Direct bank transfers, recurring, or customer preference

**Process:**
1. Go to Billtrust or Client Connect
2. Search customer/account number
3. If no email: look up in Salesforce and add
4. Confirm outstanding balance
5. Accept ACH details from customer
6. Process payment
7. Get confirmation# (posting in 1-2 business days)
8. Paste in GetPaid notes with expected posting date

---

### Credit Card Maintenance

**System:** SAP → ZICN or BP (Maintain Business Partner)

**To Update a Credit Card on File:**
1. Open SAP → ZICN or BP transaction
2. Enter SAP account number
3. Go to Payment Cards section
4. Click card to edit
5. Press F4 (lookup/enrich)
6. Update: Card#, Type, Exp Date, Name on Card
7. Save
8. Note card update in GetPaid

---

### Maintaining Card Information in BP

**SAP BP (Business Partner) - Credit Segment:**
1. In SAP, open BP transaction
2. Under Purchase Dept line select CUST NO
3. Navigate to Credit Segment data
4. Update card information as needed
5. Save changes

---

## COLLECTIONS & FOLLOW-UP

### Collection Stages by Days Past Due

| Days | Stage | Action | Method |
|------|-------|--------|--------|
| **0** | Reminder | Invoices due on 25th of following month | None |
| **>4** | Reminder | Send reminder notice | Fax/Email (call if no fax) |
| **2-7** | Escalated Serious | Send escalation notice (past due alert) | Fax/Email (call if no fax) |
| **2-8** | Problem Serious | Send delinquency notice + warn of 30-day hold | Fax/Email (call if no fax) |
| **≥30** | Order Hold | Place order hold in SAP + explain impact | Fax/Email (call if no fax) |
| **≥40** | Lab/Telemed Suspension Pending | Email sales team (RM, VDC, VDS, DR, VSS, VSS Manager) | Email |
| **≥42** | Lab/Telemed Suspension | Call customer + notify transportation & telemedicine | Phone call + email |
| **≥54** | Final Demand Letter | Mail physical letter with collections threat | Physical letter |
| **≥69** | 3rd Party Collections | Write off balance + send to agency | Email to agency |

**Special Note:** DO NOT SUSPEND on Fridays or last business day of week (prevents account resolution over weekends).

---

### Typical Contact Strategy

**For Accounts with Balance < $50,000:**

- **Early stage** (0-30 days): Fax/Email communication
- **Mid stage** (30-42 days): Fax/Email + phone calls
- **Late stage** (42+ days): Phone calls to customer, emails to internal teams
- **Final stage** (69+ days): Write off and send to collections agency

---

## COLLECTIONS CALL SCRIPT (Over 60 Days)

Use this script for accounts significantly past due.

### Opening
"Hi, may I speak with [Practice Manager or AP contact] please?

Hi, this is [your name] calling from IDEXX Laboratories. I'm reaching out regarding your account — I wanted to let you know that a recent credit card payment came back as unsuccessful and we weren't able to process it.

The outstanding balance on the account is [amount]. I wanted to reach out today to see how you'd like to take care of that.

We do have a few options available — we can retry a credit card, process an ACH payment, or if needed, we can look at setting up a payment arrangement. Whatever works best for you.

How would you like to handle this?"

---

### Talk Track for Over 60 Days Past Due

**I. Normal Intro**
- Confirm speaking with person responsible for payment
- If voicemail: Leave details of past-due balance and due date
- If general voicemail: Say calling about open/unpaid invoices, request callback by end of week

**II. Contact Verification**
"We have been reaching out for the past few weeks regarding unpaid invoices. I have been sending emails/faxes to {insert address here}. Is this the best email/fax to send to? Have you been receiving your statements?"
- Update if necessary
- Check Billtrust for delivery method

**III. Payment Discussion**
"The total overdue is $XX,XXX.XX. How would you like to process payment for that today?"

- **If they can pay full:** Process via preferred method (CC or check)
- **If partial payment:** Ask "How much CAN you pay today?" Try for half now, half in 1-2 weeks, clearing oldest month in full. Discuss payment plan if needed.
- **If unable to commit:** Ask when they CAN pay. Try to schedule for next week.

**IV. Overcome Objections**
- "The account is significantly past due—it's important we see payment today/near future"
- Ask open-ended questions: Who, What, Where, When, How much, Why?
- For checks: "I can process this and save you postage." If they don't have check info, look up previous check in Wells Fargo CEO and process from routing/account number.

**V. Verbally Abusive Customers**
- First: "If you continue speaking that way, I'll need to disconnect this call"
- If continues: "I don't feel this call is productive. I'll call you back tomorrow/Tuesday"

---

## ACCOUNT MANAGEMENT IN SAP

### Viewing Account Information
1. Open SAP
2. Use account lookup tool
3. Review: invoices, balance, credit holds
4. For CC payments: Navigate to ZOAR screen

### Placing a Credit Hold

**What it does:** Blocks online orders placed by practice, blocks IDEXX from updating services/Care Plus/standing orders

**To place:**
1. Open SAP
2. Go to account
3. Set credit hold flag
4. Save changes
5. Allow 2-4 hours for propagation

**To remove:**
1. Verify account is current (or on payment plan)
2. Open SAP
3. Remove credit hold flag
4. Save
5. Also check for lab blocks (see below)

---

## CREDIT HOLD & LAB SUSPENSION

### Understanding the System

**Credit Hold** = SAP entry that blocks customer orders and IDEXX service updates

**Lab Blocks & Suspensions** = System to control lab work processing

### Lab Block in LYNXX
- Lab work is still **tested**
- But results are **NOT RELEASED** to the practice
- Practice can't see results until hold is lifted

### Lab Suspension / Courier Pickup
- **Courier pickup** = Transportation physically picks up samples
- **Direct/FedEx** = Practice mails samples in prepaid envelope
- Email Transportation Liaison to suspend courier pickups
- They respond with status (may say "account is DIRECT")

### When Removing Credit Hold

**CRITICAL:** If you remove a credit hold, ALSO check for lab blocks!

**Checklist:**
- [ ] Remove credit hold in SAP
- [ ] Check if lab block exists in LYNXX
- [ ] If lab block exists, get it removed
- [ ] Notify Transportation Liaison if courier was suspended
- [ ] Notify Telemedicine team if services were suspended
- [ ] Document everything in GetPaid with date

### Documentation in GetPaid
- Note: "Blocked in LYNXX [DATE]"
- Note: "Suspended & Reinstated [DATE]"
- Can see lab transaction emails in Comments field

---

## PAYMENT METHODS & SYSTEMS

### Method Comparison

| Method | System | Speed | Best For |
|--------|--------|-------|----------|
| **Credit Card** | SAP ZOAR or Billtrust | Immediate (posts 1-2 days) | One-time payments, recurring plans |
| **ACH/Check-by-Phone** | Billtrust / Client Connect | 1-2 business days | Direct bank transfers, customer preference |
| **Physical Check** | Mail-in | 3-5 days | Customers without bank access |
| **Payment Plan** | SAP ZOAR or Billtrust | Scheduled | Accounts that can't pay in full |

### Processing Priority
1. **ACH** = Preferred (least fees)
2. **Credit Card** = Second choice
3. **Check** = Last resort (fees, processing time)

---

## BANK MEMO NOTICES

**When:** ACH payments failed or didn't clear

**System:** GetPaid

**Procedure:**
1. Enter account number in GetPaid
2. Check notes to understand why ACH failed
3. Highlight account row → Copy
4. Right-click → Send
5. Select "Bank Memo Notice" from dropdown
6. Click "Edit and Send"
7. Paste bank memo in email template
8. If account shows RED: Look up contact in Salesforce first
9. Send notice

---

## STATEMENT MANAGEMENT

### Viewing a Statement

**System:** Billtrust

**Steps:**
1. Go to Billtrust
2. Check "Statement" checkbox
3. Download statement

### Typical Statement Contents
- Invoice dates
- Amounts
- Payment history
- Aging buckets

---

## INTEREST REVERSAL

### When Needed
- Customer requested interest waiver
- IDEXX policy allows removal
- Calculation error

### SAP Procedure

**Query:** SQ01 (Interest Reversal Query)

**Steps:**
1. Open SAP → SQ01
2. Use "Default" variant
3. Enter customer number
4. Execute query
5. Double-click to open record
6. Set **Posting Interest Date = Today**
7. Save changes

---

## CALL SCRIPTS

### Standard Collections Call Script

**Opening:**
"Hi, may I speak with [Practice Manager or AP contact] please?

Hi, this is [your name] calling from IDEXX Laboratories. I'm reaching out regarding your account regarding your account [account number]. Your account currently has an outstanding balance of [amount] that is [X days] past due.

I wanted to reach out today to see how you'd like to take care of this.

We have several options available:
- Retry a credit card
- Process an ACH payment
- Set up a payment plan if needed

What works best for you?"

**After Call - Always Document:**
- Name & title of person spoken with
- Date & time of call
- Topics discussed
- Payment method agreed upon
- Promise date or follow-up date
- Any special circumstances

---

### Credit Card Payment Failed Script

"Hi, may I speak with [Practice Manager or AP contact] please?

Hi, this is [your name] from IDEXX Laboratories. I'm reaching out regarding your account. A recent payment we attempted didn't go through successfully, and we need to try a different approach.

The outstanding balance is [amount]. Would you prefer to:
- Retry the credit card with updated information?
- Process an ACH payment instead?
- Set up a payment plan?

What works best for you?"

---

### Over-60-Day Account Script

(See section [Collections Call Script (Over 60 Days)](#collections-call-script-over-60-days) for full talk track)

---

## EMAIL/FAX TEMPLATES

### Template 1: Reminder Notice (>4 days past due)

Subject: Outstanding Invoice Reminder — Action Needed

Dear [Practice Name],

We wanted to reach out regarding your account with IDEXX Laboratories. You have an outstanding balance of **$[amount]** that was due on **[date]**.

To keep your account in good standing, please remit payment at your earliest convenience.

**Payment Options:**
- Credit Card: [contact info]
- ACH: [contact info]
- Check: [address]

If payment has already been sent, please disregard this notice and accept our thanks.

Best regards,
IDEXX Credit Specialist

---

### Template 2: Past Due Notice (2-8 days past due, "19" stage)

Subject: Past Due Notice — Account [Account #]

Dear [Practice Name],

Your account with IDEXX Laboratories is now **past due** with an outstanding balance of **$[amount]**.

We request immediate payment to avoid further collection action. Service restrictions may be placed on your account if payment is not received within 30 days.

**Please contact us immediately at [phone number] or [email] to arrange payment.**

Thank you,
IDEXX Credit Specialist

---

### Template 3: Order Hold Notice (≥30 days past due)

Subject: Order Hold Placed — Account [Account #]

Dear [Practice Name],

Due to an outstanding balance of **$[amount]** that is **significantly past due**, we have placed a hold on your account effective immediately.

**Impact:**
- Online orders are blocked
- Standing orders are suspended
- Service updates are restricted

**To Lift the Hold:**
Contact us immediately to arrange payment or a payment plan.

**Payment Options:**
- Full payment
- Payment plan
- Partial payment with committed schedule

Reference lab and telemedicine services may also be impacted if payment is not resolved.

Contact us today: [phone] | [email]

IDEXX Credit Specialist

---

### Template 4: Lab/Telemedicine Suspension Notice (≥42 days past due)

Subject: URGENT — Reference Lab & Telemedicine Suspension

Dear [Practice Name],

Your account is **delinquent by [X] days** with an outstanding balance of **$[amount]**.

Effective immediately, we are suspending:
- Reference laboratory services
- Telemedicine services
- Courier pickups

**To Restore Services:**
Call immediately: [phone number]

Payment options:
- Full payment
- Payment plan

Services will resume upon payment or approval of a reasonable payment plan.

IDEXX Credit Specialist

---

### Template 5: Final Demand Letter (≥54 days past due)

*This is mailed as a physical letter*

---

[Date]

[Practice Name & Address]

**RE: FINAL DEMAND FOR PAYMENT — Account [Account #]**

Dear [Practice Name],

This notice will serve as a **FINAL DEMAND**.

To date, all attempts to collect this debt have been unsuccessful.

**Outstanding Balance: $[amount]**
**Delinquent Since: [date]**

Unless we receive **$[amount] by [date - 14 days from letter date]**, we will be forced to place your account with a collection agency and/or attorney for collection.

If you do not wish this action, please contact me directly.

**This will be our last request for your cooperation.**

It is our sincere hope that you will respond promptly to avoid further collection action.

If payment has already been made since [date of letter], please accept our sincere thanks and disregard this notice.

Respectfully,

[Your Name]
IDEXX Laboratories
Credit Specialist

---

## SYSTEM NAVIGATION GUIDE

### GetPaid
- Primary: Account search by number or name
- Secondary: Note all actions and payments
- Document: All communication and decisions

**Key Fields:**
- Balance
- Aging buckets
- Notes & History
- Transaction types

---

### SAP
- Use for: Invoices, account holds, credit card payments
- Main transaction: ZOAR (for credit card payments)
- Hold management: Credit hold flag in account

**Key Screens:**
- Account lookup
- Invoice view
- ZOAR (payment)
- ZICN or BP (card maintenance)

---

### Billtrust
- Use for: Invoice delivery, ACH payments, contact info
- Reliable for: Email and phone numbers
- Primary action: Process ACH and CC payments

**Key Actions:**
- Search account
- View invoices
- Accept payments
- Update contact info

---

### Salesforce
- Use for: LIMS → SAP account lookup
- Source for: Emails and phone numbers
- Reference for: Customer information

**Key Search:**
- By practice name
- By LIMS number
- By account number

---

### LIMS
- Lab-side account numbers
- USA format: Small numbers
- Canada format: Letters + numbers

---

## TROUBLESHOOTING

**Q: I have LIMS but no SAP number**
A: Search Salesforce for LIMS → Find SAP# → Use in GetPaid

**Q: Can't find customer email**
A: Try Billtrust first (most reliable) → Then Salesforce → Then call practice main line

**Q: CC payment shows in SAP but not GetPaid**
A: Typically 1-2 day delay. Check SAP ZOAR screen. If still pending after 2 days, call customer to verify card was processed.

**Q: Customer says they already paid**
A: Check Billtrust payment history → Check SAP → Get confirmation# from customer → Trace through system → Verify posting date

**Q: Order hold still active after removal**
A: May take 2-4 hours to propagate. Verify hold flag is actually removed in SAP. If persists, contact SAP support.

**Q: Payment posted but balance still shows past due**
A: May need manual adjustment. Check which invoices were cleared. Document in GetPaid. May require AP intervention.

**Q: Lab block won't clear**
A: Contact LYNXX support or Transportation Liaison. Confirm block was actually removed. Document attempt date.

---

## GLOSSARY & DEFINITIONS

**ACH** — Automated Clearing House (direct bank transfer)

**AP** — Accounts Payable staff at the practice

**Billing Zip** — Billing address ZIP code (required for CC verification)

**BP** — Business Partner (SAP transaction for customer account management)

**Care Plus** — IDEXX service/subscription offering

**CVV** — Card Verification Value (3-4 digit security code on back of CC)

**DTS** — Loyalty points/rewards system in Salesforce

**E2VET** — Older SAP account number format

**GetPaid** — Collections management system (primary workbench)

**IDEXX** — Idexx Laboratories (employer)

**LIMS** — Laboratory Information Management System (practice-side account #)

**LYNXX** — System for lab blocks and result release control

**PTS.NART** — Newer SAP account number format

**Posting Date** — Date a payment actually clears in the system

**Promise Date** — Date customer commits to making a payment

**SAP** — Systems, Applications, Products (accounting & AR system)

**ZOAR** — SAP screen for processing credit card payments

**Telemedicine** — Remote veterinary consultation services

**Transportation Liaison** — IDEXX staff managing lab courier pickups

**RM, VDC, VDS, DR, VSS** — Sales/Territory titles (notified for pending suspensions)

---

## APPENDIX: STANDARD OPERATING PROCEDURES

### Daily Routine Checklist

- [ ] Check GetPaid for new accounts/tasks
- [ ] Review accounts in "Reminder" stage
- [ ] Send required communications (fax/email)
- [ ] Process any received payments
- [ ] Follow up on promised payments
- [ ] Update all GetPaid notes
- [ ] Check for accounts reaching escalation thresholds
- [ ] Document all actions with confirmation numbers

### Weekly Tasks

- [ ] Review all accounts ≥40 days past due
- [ ] Email field sales team for pending suspensions
- [ ] Process payment plans
- [ ] Follow up on promised but not received payments
- [ ] Review account hold status

### Monthly Tasks

- [ ] Generate collections report
- [ ] Review suspension/hold log
- [ ] Process final demand letters for ≥54 day accounts
- [ ] Write off aged accounts and send to collections
- [ ] Reconcile payment documentation

---

## CONTACT INFORMATION TEMPLATE

**Internal Contacts to Keep Handy:**

| Role | Use For | Contact |
|------|---------|---------|
| Transportation Liaison | Lab suspensions | [Email/Phone] |
| Telemedicine Accounts | Telemedicine suspensions | [Email/Phone] |
| Sales Management | Pending suspensions | [Email/Phone] |
| AP/Accounting | Account questions | [Email/Phone] |
| Collections Agency | 69+ day write-offs | [Email/Phone] |
| Your Manager | Escalations | [Email/Phone] |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | July 1, 2026 | Initial consolidated manual |

---

## DOCUMENT USAGE

This manual consolidates training materials, call scripts, procedures, and collection strategies into one comprehensive reference.

**For** updates, clarifications, or additional information, refer to your manager or the original source documents in the archive.

**Last Updated:** July 1, 2026

---

**END OF MANUAL**
