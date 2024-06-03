# Update analysis definition in a Quicksight dashboard
#
# Author Nico Anandito
# AWS


import boto3
import json
import os

# AWS credentials should be fetched from environment variables
quicksight = boto3.client('quicksight')

your_aws_account_id = 'XXXXXXX'

# The script will pick up the analysis definitions from the output folder and update them in AWS QuickSight.
output_folder_update = 'quicksight_analysis_definitions_updated'
output_log_folder = 'quicksight_update_log'

# Create the output folder if it doesn't exist
if not os.path.exists(output_log_folder):
    os.makedirs(output_log_folder)

# Loop through the files in the updated folder 
for filename in os.listdir(output_folder_update):

    #split filename by _
    analysis_id = filename.split('_')[0]
    analysis_name = filename.split('_')[1].split('.')[0]

    updated_analysis_def_file = os.path.join(output_folder_update, filename)
    log_file = os.path.join(output_log_folder, filename)

    with open(updated_analysis_def_file, 'r') as f:
        updated_analysis_definition = json.load(f)

    print(f"Updating {filename} to analysis {analysis_id} with name {analysis_name}.")

    response = quicksight.update_analysis(
            AwsAccountId=your_aws_account_id,
            AnalysisId=analysis_id,
            Name=analysis_name,
            Definition=updated_analysis_definition
        )
    
    print(f"Filename {filename} updated with: {response['UpdateStatus']}")
    
    # Write log to file
    with open(log_file, "w") as f:
        json.dump(response, f, indent=4)
    
    
