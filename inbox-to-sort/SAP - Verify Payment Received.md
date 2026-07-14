# SAP -- Verify Customer Payment Received (FBL5N)

> **Purpose:** Confirm that a customer payment has been received and
> identify how it was applied.

## Workflow Overview

``` text
FBL5N
   │
   ▼
Search Customer → Display Cleared Items
   │
   ▼
Review Line Items
   │
   ▼
Open Payment Document
   │
   ▼
Verify Document Details & Amounts
```

------------------------------------------------------------------------

## Step 1 -- Open FBL5N

-   Transaction: **FBL5N -- Customer Line Item Display**
-   Enter:
    -   Customer Account
    -   Company Code
-   Select **Cleared Items**
-   Enter the clearing date.
-   Execute.

\![\[01-FBL5N.png\]\]

------------------------------------------------------------------------

## Step 2 -- Review Cleared Items

Look for:

-   Reference (example: **CREDIT CARD**)
-   Clearing Document
-   Posting Date
-   Amount
-   Assignment

Confirm the payment appears in the cleared item list.

\![\[02-Line-Items.png\]\]

------------------------------------------------------------------------

## Step 3 -- Open the Payment Document

Double-click the payment line.

Verify:

-   Customer
-   Amount
-   Clearing Date
-   Assignment
-   Text (example: **Customer OAR clearing**)

\![\[03-Document-Line.png\]\]

------------------------------------------------------------------------

## Step 4 -- Verify Accounting Entries

Open the accounting document.

Confirm:

-   Document Number
-   Posting Date
-   GL Accounts
-   Payment distribution
-   Debits equal Credits

\![\[04-Data-Entry.png\]\]

------------------------------------------------------------------------

# Quick Checklist

-   [ ] Correct customer selected
-   [ ] Correct company code
-   [ ] Cleared Items selected
-   [ ] Payment found
-   [ ] Clearing document verified
-   [ ] Amount matches expected payment
-   [ ] Posting date verified
-   [ ] GL entries reviewed
-   [ ] Payment successfully applied

## Notes

-   Payment reference often indicates payment method (e.g., **CREDIT
    CARD**).
-   "Customer OAR clearing" indicates the payment has been applied
    against Accounts Receivable.
-   If no payment appears under Cleared Items, verify the date range or
    search Open Items.
