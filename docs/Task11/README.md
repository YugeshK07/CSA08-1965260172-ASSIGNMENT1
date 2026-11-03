# Task 11 – Recommend and defend the final design

Recommend the modular Decimal-based design. Decimal values are created from strings, money is rounded to two decimal places with ROUND_HALF_UP, input is validated, and rates are stored centrally in rate-card dictionaries. The design supports regular and seasonal months and a ten-day bonus.

The calculation processes n entries in O(n) time. Storing the ten-day entries requires O(n) space, which is justified for audit and bonus calculation. It can process 150,000 records in principle, although a production deployment should use a database, transaction records, backups, access control and independent reconciliation.

A future rate revision is made in one rate-card definition. The main limitation is the stated assumption that hundredth analyser readings are rounded to whole 0.1 steps. The co-operative must approve this policy, along with the fat range and rounding policy, before production use. Support the recommendation with your own unit-test and benchmark outputs.
