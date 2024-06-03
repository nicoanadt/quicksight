# Get analysis definition from a Quicksight dashboard
#
# Author Nico Anandito
# AWS

import boto3
import json
import os

# AWS credentials should be fetched from environment variables
quicksight = boto3.client('quicksight')

your_aws_account_id = 'XXXXXX'

# Step 1: Get the list of analyses
response = quicksight.list_analyses(
    AwsAccountId = your_aws_account_id,
    MaxResults=100  # Adjust the max results as needed
)

analysis_ids = [analysis['AnalysisId'] for analysis in response['AnalysisSummaryList']]

# Create the output folder if it doesn't exist
output_folder = 'quicksight_analysis_definitions'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Loop through the analyses and save the definitions
for analysis_id in analysis_ids:
    analysis_response = quicksight.describe_analysis_definition(
        AwsAccountId= your_aws_account_id,
        AnalysisId=analysis_id
    )
    
    analysis_definition = analysis_response['Definition']
    analysis_name = analysis_response['Name']

    output_file = os.path.join(output_folder, f"{analysis_id}_{analysis_name}.json")
    print(output_file)
    with open(output_file, "w") as f:
        json.dump(analysis_definition, f, indent=4)
    print(f"Saved analysis definition for {analysis_id} to {output_file}")

