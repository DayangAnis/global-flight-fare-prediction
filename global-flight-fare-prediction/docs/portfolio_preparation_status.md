# Portfolio preparation status

## Completed
- Created a focused preprocessing notebook from the preprocessing section of the supplied group notebook.
- Removed stored cell outputs and execution counts so the notebook opens cleanly and does not imply a fresh successful run.
- Added a README describing the project, data sources, individual preprocessing focus, group-level modelling results, setup and limitations.
- Added a pipeline diagram in PNG and Mermaid formats.
- Added reusable helper functions for dataframe auditing, airline-name standardisation, surcharge aggregation, route aggregation and join-key validation.
- Added five unit tests for those helper functions.
- Added dependency, ignore, data-directory and licence files.
- Kept raw CSV data out of the repository.

## Validation performed in this preparation environment
- Unit tests: 5 passed.
- Notebook JSON: parsed successfully.
- Python syntax checks across notebook code cells: passed.
- Full end-to-end notebook execution against the Kaggle dataset: **not performed**. The notebook downloads source data via `kagglehub` and requires network access; therefore the final dataset dimensions and all original pipeline outputs must be confirmed by running the notebook locally.

## Before publishing to GitHub
1. Run the notebook from top to bottom in a fresh virtual environment.
2. Verify the final row and column counts against the executed output; the group report describes different stages of the pipeline with different dimensions.
3. Review the source dataset's terms and the repository licence before publication.
4. Confirm all descriptions of personal contribution accurately reflect your work and your group's agreement.
5. Create the GitHub repository and push these files. This preparation environment does not have a connected GitHub publishing action, so the repository has not been published automatically.
