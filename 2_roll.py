import pandas as pd

# Read the CSV file
df = pd.read_csv("finalresults.csv")

# Define roll number to search
roll_num = "21011403001"

# Initialize variables to hold data
paper_code = None
scgpa = None
cgpa = None

# Initialize list to collect results
new_arr = []

# Iterate over the DataFrame
for n, api in enumerate(df["roll"]):
    if str(roll_num) == str(api):
        paper_code = df["paper_code"][n]
        scgpa = df["scgpa"][n]
        cgpa = df["cgpa"][n]
    
    # Create the dictionary and add it to the list
    new_js = {
        "roll": api,
        "paper_code": paper_code,
        "scgpa": scgpa,
        "cgpa": cgpa
    }
    
    print(new_js)
    new_arr.append(new_js)

print(new_arr)
