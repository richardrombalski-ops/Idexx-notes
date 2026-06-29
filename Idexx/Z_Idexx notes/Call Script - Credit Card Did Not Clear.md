# Call Script — Credit Card Did Not Clear

#idexx #collections #credit-specialist #call-script #payment

---

## Purpose

Use this script when a customer's credit card payment did not process successfully and you need to contact them to resolve the outstanding balance.

**Before calling:**
- Pull up the account in **GetPaid** — review balance, aging, stage, and prior notes
- Confirm contact information in **Billtrust** first; use **Salesforce** if no email/phone on file
- Know the outstanding balance amount before dialing

---

## Script

> "Hi, may I speak with [Practice Manager or AP contact] please?
>
> Hi, this is [your name] calling from IDEXX Laboratories. I'm reaching out regarding your account — I wanted to let you know that a recent credit card payment came back as unsuccessful and we weren't able to process it.
>
> The outstanding balance on the account is [amount]. I wanted to reach out today to see how you'd like to take care of that.
>
> We do have a few options available — we can retry a credit card, process an ACH payment, or if needed, we can look at setting up a payment arrangement. Whatever works best for you.
>
> How would you like to handle this?"


## Payment Options to Offer

| Method | System |
|--------|--------|
| Credit Card retry | SAP → ZOAR |
| ACH / Check-by-Phone | Billtrust / Client Connect |
| Payment Plan | Payment Plan Spreadsheet → Billtrust or SAP/ZOAR |

---

## After the Call — Document in GetPaid

Always note the following immediately after hanging up:

- Who you spoke with (name and title)
- Date and time of call
- What was discussed
- Payment method agreed upon
- Any promise date or follow-up date
- Next scheduled action

> 💡 **Reminder:** The task is not complete until the call and any payment details are documented in GetPaid.

---

## Related Notes

- [[IDEXX_Credit_Collections_Task_Reference_with_Screen_Procedures]]
- [[⭐️IDEXX Credit Specialist Training Notes 1]]
- [[Strategy for Accounts with Total Balance Less than $50,000]]
