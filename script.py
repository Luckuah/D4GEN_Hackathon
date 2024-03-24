import pandas as pd

# Define the file paths
# input_file = "subject19/1.morning/EDA.csv"
input_file = "subject_23/2.evening/EDA.csv"
output_file = "abnormal_eda.csv"

# Load the input file into a pandas DataFrame, skipping the first 3 lines
df = pd.read_csv(input_file, skiprows=3, header=None)

# Print the number of rows in the DataFrame
print(df.shape[0])

# Calculate the maximum number of lines you can write to the output file
max_lines = df.shape[0] // 540

# Repeat the process for the maximum number of lines
for _ in range(max_lines):
    # Print the current iteration number
    print(_)

    # Take the next 540 rows from the current DataFrame
    samples = df.iloc[:540]

    # Remove these rows from the DataFrame
    df = df.iloc[540:]

    # If there are any samples, transpose them and append them as a line to the output file
    if not samples.empty:
        samples.T.to_csv(output_file, mode='a', header=False, index=False)
