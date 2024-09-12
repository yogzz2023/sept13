import csv

# Function to convert text file to CSV
def txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as infile, open(csv_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        for line in infile:
            # Split each line by whitespace or use a custom delimiter
            row = line.strip().split()  # Adjust delimiter as per your file structure
            writer.writerow(row)

# Specify the input text file and output CSV file paths
txt_file = 'test.txt'  # Replace with your actual file path
csv_file = 'output_file.csv'  # Replace with your desired output file name

# Call the function to convert the text file to CSV
txt_to_csv(txt_file, csv_file)

print("Conversion complete!")
