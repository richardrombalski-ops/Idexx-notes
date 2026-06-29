# IDEXX Credit Specialist Training Notes

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
3. **Customer Pays** — Payment submitted through Bill Trust
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

- B/T Bill Trust - ACH Payments
- SAP - ZOAR - CC Payments
- Get Paid - Nothing Accts

- T - Client Completion
  - enter Account Number, Amt, accept
  - copy all info in GP

![[Image to Texts/IMG_6476.JPG]]

Aww # IDEXX ACCT NUMBERS

## SAP
- older: 0000001965 / EZVET
- newer: 0000400000 

## LIMS
Laboratory Information Management System  
- USA: small # (no zeros)  
- CAD: Letters & #'s = M5Q  

## Staff at Practice
- MAY KNOW & USE LIMS
- Acct Practice Managers & AP
- MAY KNOW & USE SAP  

## Additional Information
USE Salesforce to find LIMS to find SAP (for GetPd)  

---

### Explanation of Account Number Formats

There are different formats for account numbers within the IDEXX system:

- **SAP Account Numbers**: The older format consists of a specific numeric sequence, while the newer format follows a similar structure but with a different starting point.
  
- **LIMS Account Numbers**: For the USA, the account number is represented as a smaller number without leading zeros. In Canada, the format includes letters along with numbers. 

Understanding these formats is crucial for staff to efficiently manage and navigate the account systems.

![[Assets/Images/IMG_6493.JPG]]

# Payment Plans - Spreadsheet

- **Get Account #**
  - Payment Amount, Type

- **Notes, History**
  - Print icon brings up detail of previous transaction types

## Invoice Management

- Invoice generated in SAP
- Invoice delivered through Billtrust
- Customer payment through Billtrust
- Payment remittance
- Follow up managed through GetPaid
- Accounting records finalized in SAP

![[Assets/Images/Images/IMG_6477.JPG]]

# Handwritten Notes

OSes assyed to generate either VDC or GND
Digital VR

RTI click /SAD

SPI correspondence

CMAl Pax

Cash at install

exit & (0) SEND

CMAl

Black Book

TON (0) DR cc.Myoff

# Handwritten Notes

Send

Transfer of bill

My due to 7 days ahead

Budget Explainable

cash or install

# Send

## Transatletes

My Due to 7 Days ahead

## Garage Explanation

Cash at Install

# Handwritten Notes

Users asked to generate either VDC or DRC
D6464 VR

Rt click - SQd

Send correspondence

CMal Fax

Cash at instul

exist & send

CMal

Black Book
404 D DR cc: Mystaff

# Get Cut # (GP Contacts → Save)

B. / Trust - Lookup (CUST#)
  - if no email

lookup in sales force

copy to Cust N#

open in pill
  - up cust 6wp
  - upper right

under USE it?
  - 9/14 email

SAVE

# Handwritten Notes

Acron/Y126

CAG

UAFBO

VDC - Sales cy inField

@nt
cot
(gain @ install

yst sand mott 90
sates Rpt

# Payment Plans - Spread Sheet

Get Account #, Payment Amount, Type
$32 k x 2, x 3x, $60.00

Notes, History → P.O.# Icon brings up detail of previous transaction type

## INV Generation in SAP

Inv delivered through ONWUST

Customer payment through Bill Hub

Payment Remittance

Follow up Mined through Get Paid

Accountg records EndList in SAP

# Bill Trust - Acct, Payments

SAP - ZOAR - CC Payments

Cct Paid - Noting Accts

# IT - Client Connection

Enter Account Number, Amt, Accept

Copy all info in GP