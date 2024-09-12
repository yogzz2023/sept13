import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
csv_file = 'output_file.csv'  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Extract relevant columns
time = data['MT']
measured_z = data['MR']
filtered_z = data['MA']

# Plot time vs measured z and filtered z
plt.figure(figsize=(10, 6))
plt.plot(time, measured_z, label='Measured Z', color='blue', marker='o')
plt.plot(time, filtered_z, label='Filtered Z', color='green', marker='x')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Height (Z)')
plt.title('Time vs Measured and Filtered Z')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
