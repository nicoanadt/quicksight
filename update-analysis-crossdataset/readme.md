# Quicksight Definition Updater

This script will get quicksight analysis that has the cross-dataset filter and update it to be single dataset filter only. NOTE: The script will update all filters in the analysis. Use sparingly if you have actual filter that require cross-dataset functionality.

There are 3 parts of the scripts

1. `1_qs-get-definition.py` : This script is designed to extract the analysis definitions from an AWS QuickSight dashboard and save them to local JSON files
2. `2_update-qs-definition_file.py` : This script will update the extracted definition file with CrossDataset='ALL_DATASET' to 'SINGLE_DATASET' and save it in another JSON files in a separate output folder
3. `3_qs-update-analysis-definition.py` : This script is designed to update the analysis definitions in AWS QuickSight based on the local JSON files

## Prerequisites

- Install `boto3`
- The AWS credentials (access key and secret key) should be available in the environment variables.
- The `your_aws_account_id` variable should be replaced with the actual AWS account ID.



## Script 1: `1_qs-get-definition.py`

This script will export all analysis definition to JSON file

**Output:** 
The script creates an output folders: `quicksight_analysis_definitions`

- The analysis definitions are saved as JSON files in the `quicksight_analysis_definitions` folder, using the format `<analysis_id>_<analysis_name>.json`

## Script 2: `2_update-qs-definition-file.py`

Purpose:
This script is designed to update the `CrossDataset` property in the analysis definitions for AWS QuickSight. The script reads the analysis definitions from a specified folder, updates the `CrossDataset` property if it is set to `'ALL_DATASETS'`, and then saves the updated definitions to a new folder.

If the `CrossDataset` property is set to `'ALL_DATASETS'`, the script updates it to `'SINGLE_DATASET'`.

**Input and Output:**

- Input: The script expects the original analysis definitions to be stored in the `quicksight_analysis_definitions` folder.
- Output: The script saves the updated analysis definitions in the `quicksight_analysis_definitions_updated` folder, using the same filenames as the original files.


## Script 3: `3_qs-update-analysis-definition.py`

This script is designed to update the analysis definitions in AWS QuickSight. The script then calls the `quicksight.update_analysis()` method to update the analysis in QuickSight

**Input and Output:**

- Input: The script expects the updated analysis definitions to be stored in the `quicksight_analysis_definitions_updated` folder. The filenames should be in the format `<analysis_id>_<analysis_name>.json`
- Output: The script updates the corresponding analyses in AWS QuickSight and writes the update logs to the `quicksight_update_log` folder.
