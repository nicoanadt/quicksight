import json
import os

output_folder = 'quicksight_analysis_definitions'
output_folder_update = 'quicksight_analysis_definitions_updated'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_update):
    os.makedirs(output_folder_update)

# Assign the filename that you want to update, or use the loop to update all files in the source folder
# filename = "<analysis-id>_<analysis-name>.json"

# Loop through the files in the updated folder 
for filename in os.listdir(output_folder):

    analysis_def_file = os.path.join(output_folder, filename)
    updated_analysis_def_file = os.path.join(output_folder_update, filename)

    # Load the JSON file
    with open(analysis_def_file, 'r') as file:
        data = json.load(file)

    # Loop through the FilterGroups
    for filter_group in data['FilterGroups']:
        # Check the CrossDataset property
        cross_dataset = filter_group['CrossDataset']
        print(f"CrossDataset: {cross_dataset}")

        # Update the value if it is ALL DATASET
        if cross_dataset == 'ALL_DATASETS':
            filter_group['CrossDataset'] = 'SINGLE_DATASET'
        

    # Write the updated data back to the JSON file
    with open(updated_analysis_def_file, 'w') as file:
        json.dump(data, file, indent=2)

    print(f"JSON file {updated_analysis_def_file} updated successfully.")
