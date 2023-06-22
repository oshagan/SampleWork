
import pandas as pd
import os


# Directory containing the Excel files
directory = '/Users/adomoshagan/Desktop/Summer 23/GitHub Portfolio/SampleWork/ExcelFiles'

# List to store the data from each Excel file
combined_data = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        file_path = os.path.join(directory, filename)
        
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)
        
        # Combine each row and remove empty cells
        df_combined = df.apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
        
        # Append the combined data to the list
        combined_data.append(df_combined)
        
# Concatenate the data from all files into a single DataFrame
combined_df = pd.concat(combined_data, ignore_index=True)

# Save the combined data to a new Excel file
combined_df.to_excel('combined_data.xlsx', index=False)
