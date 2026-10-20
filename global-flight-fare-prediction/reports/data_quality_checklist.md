# Data quality and validation checklist

Use this checklist when rerunning the notebook. Record observed counts from the executed pipeline rather than copying counts from the report without verification.

- [ ] Confirm all six expected CSV files are present.
- [ ] Record row count and column count for each raw table.
- [ ] Review missing-value counts and distinguish structural missingness from data errors.
- [ ] Check duplicate rows in every source table.
- [ ] Check join-key uniqueness at the intended aggregation level.
- [ ] Record row counts after every integration step and investigate unexpected multiplication or row loss.
- [ ] Review categorical mappings and unknown categories.
- [ ] Confirm target-derived columns are excluded from predictors.
- [ ] Verify the final target, data types and missingness.
- [ ] Record final row/column counts and the date the dataset was retrieved.
- [ ] Review interpolation assumptions and evaluate with a chronological split in future work.
