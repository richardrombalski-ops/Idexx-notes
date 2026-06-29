# IDEXX Credit Specialist Training Notes - Reorganized

## Cash on Install

When a customer pays cash at installation, follow these steps:

### Payment Processing
- Cash payments at install are recorded separately from standard invoice payments
- Document the cash payment in the account notes immediately

### Documentation Requirements
- Enter the **Account Number** and **Payment Amount**
- Accept the transaction
- **Copy all information into GetPaid** to ensure proper tracking

### Follow-Up
- Always note the cash payment in **GetPaid** for account history
- This ensures the payment is properly recorded and tracked for accounting finalization

---

## What You'll Be Working With

As a Credit Specialist at IDEXX, you'll use **three main platforms** every day. It's important to understand what each one does and how they connect:

| Platform       | Purpose                                                                       |
| -------------- | ----------------------------------------------------------------------------- |
| **Bill Trust** | Delivers invoices to customers and processes ACH payments                     |
| **SAP**        | Generates invoices, manages account numbers, and finalizes accounting records |
| **GetPaid**    | Tracks payment collection and manages follow-up on outstanding balances       |

---

## Account Numbers — What to Know

Accounts have different ID formats depending on the system you're looking at.

### SAP Account Numbers
There are two formats you may encounter:
- **Older format** (EZVET accounts): e.g., `0000001965`
- **Newer format**: e.g., `0000400000`

### LIMS Account Numbers (Laboratory Information Management System)
LIMS numbers look different depending on the country:
- **USA accounts** — Small numbers, no leading zeros
- **Canadian accounts** — A mix of letters and numbers (e.g., `M5Q`)

### How to Find Account Information
> Use **Salesforce** to look up a customer's LIMS number → this will connect you to their **SAP account** → which you'll need to pull them up in **GetPaid**

---

## Who Has Access to What

Understanding who at a practice can help you is important when troubleshooting:

- **Practice Managers** and **Accounts Payable (AP) staff** typically have access to both **LIMS** and **SAP**

If you need account-level information from the customer's side, these are your go-to contacts.

---

## The Invoice & Payment Lifecycle

Every payment follows this path from start to finish:

1. **Invoice Generated** — Created in SAP
2. **Invoice Delivered** — Sent to the customer via Bill Trust
3. **Customer Pays** — Payment submitted through Bill Trust (or cash at install)
4. **Payment Remittance** — Payment is processed and recorded
5. **Follow-Up** — Any outstanding issues tracked in GetPaid
6. **Accounting Finalized** — Records completed in SAP

---

## Setting Up Payment Plans

When a customer needs a payment plan, here's what to do:

### Step 1 — Gather the Required Info
You'll need the following from the payment plan spreadsheet:
- **Account Number**
- **Payment Amount**
- **Payment Type**

### Step 2 — Review Transaction History
- Go to **Notes & History** to see previous transactions
- Use the **Print icon** to pull up a detailed breakdown of past transaction types

---

## Platform-Specific Notes

### GetPaid
- Used for **noting accounts** and tracking collections
- **Always note everything** — document every action and communication on an account

### Bill Trust
- Handles **ACH payments**
- Used for invoice delivery and receiving customer payments

### SAP
- For **credit card payments**, use the transaction screen called **ZOAR**

---

> 💡 **Trainee Tip:** When in doubt about an account, start in **Salesforce** to find the LIMS number, then trace it through to **SAP** and **GetPaid**. Most answers live in the account history — so always check notes first!