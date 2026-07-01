# IDEXX Credit Specialist Complete Guide

**Welcome!** This is your comprehensive reference for working as a Credit Specialist at IDEXX. Use the table of contents below to navigate to the information you need.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Systems Overview](#systems-overview)
3. [Account Numbers & Lookup](#account-numbers--lookup)
4. [Daily Workflows](#daily-workflows)
5. [Payment Processing](#payment-processing)
6. [Collections & Follow-Up](#collections--follow-up)
7. [Quick Reference Procedures](#quick-reference-procedures)
8. [Key Contacts](#key-contacts)

---

## Quick Start

### Your First Steps

When you receive an account to work on, follow this sequence:

1. **Identify the Account** — Locate it using any available identifier:
   - SAP account number
   - LIMS account number
   - Customer/practice name
   - Billtrust account number

2. **Find the SAP Number** — If you only have a LIMS number:
   - Search Salesforce for the LIMS number
   - Note the SAP account number
   - Use the SAP number in GetPaid

3. **Open in GetPaid** — Search for the customer
   - Review balance, aging, and collection stage
   - Check all prior notes and history
   - Print icon shows previous transaction types

4. **Confirm Contact Info** — Verify how to reach the customer:
   - Check Billtrust first (most reliable for email/phone)
   - Fall back to Salesforce if Billtrust has no contact
   - Use practice manager or AP staff contact if needed

5. **Take Action** — Based on the account stage (see [Collections & Follow-Up](#collections--follow-up))

6. **Document Everything** — Always note in GetPaid:
   - What you did and when
   - Who you spoke with (if applicable)
   - Payment details and confirmation numbers
   - Next follow-up date

---

## Systems Overview

You'll use **five main systems** every day. Here's what each does:

| System | Purpose | Key Uses |
|--------|---------|----------|
| **GetPaid** | Collections & account management | Search accounts, manage follow-up, store payment details, document all actions |
| **SAP** | Accounting & A/R system | View invoices, generate invoices, process CC payments (ZOAR screen), place/remove holds |
| **Billtrust (BT)** | Invoice delivery & payment processing | Send invoices to customers, accept ACH payments, update customer contact info |
| **Salesforce (SF)** | Customer & contact lookup | Find LIMS → SAP connections, look up emails/phones, manage loyalty points (DTS) |
| **LIMS** | Lab account information | Lab-side account numbers used by practices |

### Key System Connections

```
GetPaid ← SAP (account balance, holds)
GetPaid ← Billtrust (payment confirmations, contact info)
GetPaid ← Salesforce (LIMS → SAP lookup)
```

**💡 Golden Rule:** Salesforce finds LIMS → SAP, then use SAP number in GetPaid.

---

## Account Numbers & Lookup

### Understanding Account Number Formats

Your system has **three different account numbering schemes**. You need to know which one you're looking at:

#### SAP Account Numbers
Used in GetPaid, SAP, and Billtrust. Always includes leading zeros.

- **Older format (E2VET):** `0000001965`
- **Newer format (PTS.NART):** `0000400000`

#### LIMS Account Numbers
Laboratory Information Management System numbers used by the practice's lab. Format varies by country.

- **USA:** Small number without leading zeros (e.g., `1965`)
- **Canada:** Letters and numbers (e.g., `M5Q`)

#### Billtrust Account Numbers
Used within the Billtrust system for invoice delivery and payment processing.

### How to Find the Right Account Number

**Scenario 1: You have a LIMS number**
1. Go to Salesforce
2. Search for the LIMS number
3. Note the SAP account number shown
4. Use that SAP number in GetPaid / Billtrust

**Scenario 2: You have a SAP number**
- Use it directly in GetPaid and Billtrust

**Scenario 3: You have a practice name**
1. Search GetPaid by practice name
2. Or search Salesforce for the practice
3. Get the SAP number from GetPaid or Salesforce

### Who to Ask for Account Numbers

- **Practice Manager** — Knows LIMS number
- **Accounts Payable (AP) staff** — Knows both LIMS and SAP
- **Billtrust** — Can look up by email or phone

---

## Daily Workflows

### Workflow 1: Account Check-In

Use this when you're assigned an account to review or when a customer contacts you.

**Step 1: Identify & Open**
- Locate the SAP account number (use Salesforce if needed)
- Search GetPaid for that account
- Open the account record

**Step 2: Review Status**
- Check current balance
- Review aging buckets (how many days past due)
- Read all prior notes
- Check collection stage

**Step 3: Assess the Situation**
- Is there a recent payment pending?
- Are there holds in place?
- What's the collection history?
- Has this account been contacted recently?

**Step 4: Determine Next Action**
- Refer to [Collections & Follow-Up](#collections--follow-up) for your next step
- Follow the stage-based contact strategy

---

### Workflow 2: Processing a Payment

When a customer makes a payment, here's how to handle it.

**Step 1: Receive & Confirm Payment**
- Get payment details from Billtrust or the customer
- Confirm payment method:
  - **ACH** → Check Billtrust
  - **Credit Card** → Check SAP (ZOAR screen) or Billtrust
  - **Check** → Note details

**Step 2: Document in GetPaid**
- Open the account in GetPaid
- Copy all payment confirmation details
- Paste into the account notes/comments
- Include:
  - Payment method (ACH, CC, check)
  - Amount
  - Confirmation number
  - Payment date
  - Bank/processor reference (if ACH)

**Step 3: Verify Posting**
- Check GetPaid balance — does it reflect the payment?
- For credit card: Allow 1-2 days for posting
- For ACH: Typically posts within 1-2 business days

**Step 4: Follow-Up if Needed**
- If payment was promised but not received, follow up per [Collections & Follow-Up](#collections--follow-up)
- If payment partially clears balances, note which invoices were paid

---

### Workflow 3: Setting Up a Payment Plan

When a customer cannot pay the full balance immediately.

**Step 1: Gather Information**
- Open the payment plan spreadsheet
- Get from the customer:
  - Account number
  - Total outstanding balance
  - Proposed payment amount
  - Proposed payment frequency (weekly, monthly, etc.)

**Step 2: Review Payment History**
- Check GetPaid notes and history
- Use the Print icon to view previous transaction types
- Confirm the account hasn't missed payment plans before

**Step 3: Enter the Payment Plan**
- Use Billtrust or SAP (ZOAR) to set up the plan
- Schedule payments (e.g., $1,000 on the 15th, $1,000 on the 30th)
- Get a confirmation number

**Step 4: Document & Send Confirmation**
- Paste all payment plan details in GetPaid notes
- Send written confirmation to the customer
- Reference the plan in all future communications

**Step 5: Monitor**
- Note in GetPaid when each payment is due
- Set reminders for follow-up if payments miss
- Update notes as payments post

---

### Workflow 4: Removing a Hold or Suspension

When an account with a hold/suspension becomes current.

**Important:** A **credit hold in SAP** blocks online orders and prevents IDEXX from updating services, Care Plus, or standing orders. Removing it requires action in multiple systems.

**Step 1: Verify Payment is Current**
- Confirm the past-due amount is now paid
- Check GetPaid balance is $0 or acceptable
- Verify in SAP that balance shows current

**Step 2: Remove Credit Hold in SAP**
- Open SAP
- Go to the account
- Remove the credit hold flag
- Save changes

**Step 3: If Lab/Telemedicine Services Were Suspended**
- Notify **Transportation Liaison** that courier service can resume
- Notify **Telemedicine Accounts team** that services can resume
- Note in GetPaid that suspension has been lifted

**Step 4: Document in GetPaid**
- Log the hold removal date
- Note the action taken
- Record which systems were updated

---

## Payment Processing

### Credit Card Payments

**Used for:** One-time CC payments or scheduled CC payment plans.

**System:** SAP → ZOAR screen

**To Process a Credit Card Payment:**

1. Get from the customer:
   - Card number (securely)
   - Expiration date
   - CVV
   - Cardholder name
   - Amount to charge
   - Billing zip code

2. In SAP, open the **ZOAR** transaction screen

3. Enter the payment details

4. Verify the amount and account number

5. Submit the payment

6. Confirm with the customer and get confirmation number

7. Paste the confirmation in GetPaid notes

**Important:** Always confirm the payment has posted in SAP before telling the customer it's complete.

---

### ACH / Check-by-Phone Payments

**Used for:** Direct bank transfers, recurring payments, or customer preference.

**System:** Billtrust / Client Connect

**To Process an ACH Payment:**

1. Go to **Billtrust** (or use **Client Connect**)

2. Search for the customer/account number

3. If no email on file, look up in **Salesforce** and add it

4. Confirm the outstanding balance

5. Accept the ACH payment details from the customer

6. Process the payment

7. Get the confirmation number

8. Paste the confirmation in GetPaid notes

**Note:** ACH payments typically post within 1-2 business days. Document in GetPaid with the expected posting date.

---

### Bank Memo Notices (ACH's That Didn't Clear)

When an ACH payment fails or doesn't clear, you may need to send a bank memo notice.

**To Send a Bank Memo Notice:**

1. Enter the account number in **GetPaid**

2. Check the notes to understand why the ACH failed

3. Highlight the account row and **Copy**

4. Right-click → **Send**

5. From the dropdown, select **Bank Memo Notice**

6. Click **Edit and Send**

7. Paste the bank memo details in the email template

8. If the account appears in red, look up the contact in **Salesforce** first

9. Send the notice

---

### Credit Card Maintenance (Updating on File)

When a customer needs to update their credit card on file.

**System:** SAP → ZICN or BP (Maintain Business Partner) screen

**To Update a Credit Card:**

1. In SAP, open **ZICN** (or BP transaction for Maintain Business Partner)

2. Enter the **SAP account number**

3. Go to **Payment Cards** section

4. Click on the card to edit

5. Press **F4** to access the lookup/enrich function

6. Update the card details:
   - Card number
   - Card type
   - Expiration date
   - Name on card

7. Save changes

**Documentation:** Note in GetPaid that the card was updated and the new expiration date.

---

## Collections & Follow-Up

### Collection Stages & Actions

IDEXX uses a **defined escalation process** for past-due accounts. The action you take depends on **how many days past due** the account is. Here's the complete strategy:

| Days Past Due | Stage | Your Action | Contact Method |
|---|---|---|---|
| **0** | Reminder | No action yet — invoices are due on 25th of following month | — |
| **>4** | Reminder | Send reminder communication | Fax / Email (call if no fax contact) |
| **2–7 (Note: "12")** | Escalated Serious | Send escalation notice (past due alert) | Fax / Email (call if no fax contact) |
| **2–8 (Note: "19")** | Problem Serious | Send delinquency notice + warn about 30-day hold | Fax / Email (call if no fax contact) |
| **≥30 (Note: "231")** | Order Hold | Place order hold in SAP + explain impact to customer | Fax / Email (call if no fax contact) |
| **≥40** | Lab/Telemed Suspension Pending | Email field sales team (RM, VDC, VDS, DR, VSS, VSS Manager) | Email to sales |
| **≥42** | Lab/Telemed Suspension | Call the customer + notify transportation & telemedicine teams | Phone call + email |
| **≥54** | Final Demand Letter | Mail physical letter with collection agency threat | Physical letter |
| **≥69** | 3rd Party Collections | Write off balance + send A/R form to collections agency | Email to agency |

### Collection Contact Script

**Use this when calling a customer with a past-due account:**

> "Hi, may I speak with [Practice Manager or AP contact] please?
>
> Hi, this is [your name] calling from IDEXX Laboratories. I'm reaching out regarding your account [account number]. Your account currently has an outstanding balance of [amount] that is [X days] past due.
>
> I wanted to reach out today to see how you'd like to take care of this.
>
> We have several options available:
> - Retry a credit card
> - Process an ACH payment
> - Set up a payment plan if needed
>
> What works best for you?"

### After-Call Documentation

**Always document immediately after the call:**

- Who you spoke with (name, title)
- Date and time of call
- What was discussed
- Payment method agreed upon
- Promise date or follow-up date
- Any special circumstances or notes

---

### Payment Did Not Clear — Call Script

When a credit card payment fails or an ACH bounces:

> "Hi, may I speak with [Practice Manager or AP contact] please?
>
> Hi, this is [your name] from IDEXX Laboratories. I'm reaching out regarding your account. A recent payment we attempted didn't go through successfully, and we need to try a different approach.
>
> The outstanding balance is [amount]. Would you prefer to:
> - Retry the credit card with updated information?
> - Process an ACH payment instead?
> - Set up a payment plan?
>
> What works best for you?"

---

### Special Procedures

#### Waiving Interest

If a customer requests interest removal or if IDEXX policy allows for waiver:

1. In **SAP**, open query **SQ01**
2. Use the **Default** variant
3. Enter the **customer number**
4. Execute the query
5. Open the record (double-click)
6. Set **Posting Interest Date** to **Today**
7. Save

---

#### Viewing & Printing Statements

To pull a statement for a customer:

1. Go to **Billtrust**
2. Check the **Statement** checkbox
3. Download the statement

---

#### Lab/Telemedicine Suspension Notifications

When you place a lab or telemedicine suspension:

1. **Transportation Liaison** — Email to notify that lab courier pickup is suspended until account is resolved

2. **Telemedicine Accounts Team** — Email to notify that telemedicine services are suspended

3. Always call the **customer** to inform them of the suspension before notifying internal teams

**Important:** Do not suspend on **Fridays** or the **last business day of the week**. This prevents account resolution delays over weekends.

---

## Quick Reference Procedures

### View Account in GetPaid
1. Go to GetPaid
2. Search by account number or practice name
3. Review balance, aging, and stage
4. Click **Notes & History** to see prior activity

### View Account in SAP
1. Go to SAP
2. Use the account lookup tool
3. View invoices, balance, and credit holds
4. For credit card payments: go to ZOAR screen

### View Account in Billtrust
1. Go to Billtrust
2. Search by account number or practice email
3. View outstanding invoices
4. View payment history

### Look Up Customer Contact Info
1. First choice: **Billtrust** (check email/phone)
2. Second choice: **Salesforce** (search practice name or LIMS)
3. Third choice: Call practice general line and ask for AP

### Send Email or Fax to Customer
1. GetPaid: Highlight account row
2. Right-click → **Send**
3. Choose **Email** or **Fax**
4. Select the template (e.g., "Reminder," "Past Due Notice")
5. Review the content
6. Click **Send**

---

## Key Contacts

### Internal Idexx Resources

| Role | Use For |
|------|---------|
| Transportation Liaison / Supervisor | Lab courier suspensions and resumptions |
| Telemedicine Accounts Team | Telemedicine service suspensions and resumptions |
| Sales Team (RM, VDC, VDS, DR, VSS, VSS Manager) | Pending lab/telemedicine suspensions (≥40 days past due) |
| Practice Manager / AP Staff | Account questions, billing issues, payment discussions |
| Third Party Collection Agency | Accounts ≥69 days past due (write-off stage) |

### External Resources

| System | Purpose | Notes |
|--------|---------|-------|
| **Salesforce** | Look up LIMS → SAP; find customer contact info | Used for account research |
| **Billtrust** | Invoice delivery; ACH payments; customer contact info | Most reliable for email/phone |
| **SAP** | Core accounting system; invoices; account holds | ZOAR for credit card payments |

---

## Tips for Success

✅ **Always start with GetPaid.** It's your main workbench for account management.

✅ **Check notes first.** 90% of the information you need is already documented.

✅ **Document everything.** Future you (and your team) will thank you.

✅ **Use the right system for the right job:**
   - GetPaid = Collections management
   - Billtrust = Payments & contact info
   - SAP = Accounting & holds
   - Salesforce = Account research & LIMS lookup

✅ **When in doubt**, follow the escalation strategy by days past due. It's your roadmap.

✅ **Never suspend on Friday.** Always think about the weekend.

✅ **Get everything in writing.** Payment plans, promised dates, and agreements should be documented.

---

## Common Troubleshooting

**Q: I have a LIMS number but need the SAP account number.**
A: Go to Salesforce, search for the LIMS number, and note the SAP number shown in the account record.

**Q: I can't find a customer's email in Billtrust.**
A: Look it up in Salesforce by practice name. If still not found, call the practice's main number and ask for the AP contact.

**Q: A credit card payment was supposed to post but hasn't.**
A: Check SAP (ZOAR screen) to confirm it was submitted. CC payments typically take 1-2 days to post. If still pending after 2 days, call the customer to verify the card.

**Q: I placed an order hold, but the customer says they can still order.**
A: The hold may not have fully propagated through the system. Confirm the hold is in place in SAP and give it 2–4 hours to take effect. If the issue persists, check with SAP support.

**Q: The customer says they sent a payment but I don't see it in GetPaid.**
A: Check Billtrust or SAP payment history. If it's not there, ask the customer for the confirmation number. It may still be in process (1-2 days for ACH, immediate for CC). If they have confirmation but payment isn't showing, escalate to the processor.

---

## Document Version

**Last Updated:** July 1, 2026
**Compiled From:** Original training materials, task procedures, collection strategies, and standard operating procedures.
**Questions or Updates?** Refer to the original source documents or contact your manager.

---

*This guide consolidates scattered training notes into one comprehensive reference. For historical details or alternative procedures, refer to the original documents in the Unindexed folder.*
