# fix_santander_qif
Uses a dictionary to fix data exported from Santander online banking

For some reason, Santander online banking exports a bizzare concatenation of fields into the QIF description field including the value, exchange rate, date and then the value again.

For example:

PCARD PAYMENT TO TFL.GOV.UK/CP,6.40 GBP, RATE 1.00/GBP ON 24-04-2015, 6.40
This makes it almost impossible for financial software to automatically identify similiar transactions. This script cleans up the description and also substitutes some common strings to ensure that important information is not truncated later.
