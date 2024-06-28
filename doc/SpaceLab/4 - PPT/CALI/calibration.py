import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

sns.set(style="whitegrid")

def detect_max_voltage(csv_files, voltage_column, start_row):
    max_voltages = []  # List to store maximum voltages
    
    for csv_file in csv_files:
        print("Processing file:", csv_file)
        df = pd.read_csv(csv_file)  # Load CSV file into a DataFrame
        voltage_data = df.loc[start_row:, voltage_column]  # Select the 'CH4' column starting from row 17
        voltage_data = pd.to_numeric(voltage_data, errors='coerce')  # Convert voltage data to numeric type
        voltage_data.dropna(inplace=True)  # Drop rows with NaN values in the voltage data
        max_voltage = voltage_data.max()  # Find maximum voltage value
        max_voltages.append(max_voltage)  # Append maximum voltage to the list
        print("Maximum voltage:", max_voltage)  # Print maximum voltage value
        print()

    return max_voltages

def plot_vmax_vs_impulses(known_impulses, max_voltages, subplot_index):
    plt.subplot(2, 1, subplot_index)  # Use the provided subplot index
    plt.plot(known_impulses, max_voltages, marker='o', linestyle='-', color='#ff5733', linewidth=3, markersize=10)  # Adjust line and marker styles
    plt.xlabel('Number of Known Impulse', fontsize=14, fontweight='bold', color='#333333')  # Adjust font size and style
    plt.ylabel('Maximum Voltage', fontsize=14, fontweight='bold', color='#333333')  # Adjust font size and style
    plt.title('Linear Impulses', fontsize=16, fontweight='bold', color='#333333')  # Adjust font size and style
    plt.grid(True, linestyle='--', alpha=0.7, color='#aaaaaa')  # Adjust grid style
    plt.xticks(fontsize=12, color='#555555')  # Adjust tick labels
    plt.yticks(fontsize=12, color='#555555')  # Adjust tick labels
    plt.tight_layout()  # Adjust layout
    plt.gca().set_facecolor('#f0f0f0')  # Set background color of plot face

# I_bit = v_max / c ------------------------------------------------------------------------------------------------------------------------------
def plot_ibit_vs_vmax(max_voltages, slope, subplot_index):
    plt.subplot(2, 1, subplot_index)  # Use the provided subplot index
    bit_impulses = [v / slope for v in max_voltages]
    plt.plot(bit_impulses, max_voltages, marker='s', linestyle='--', color='blue', linewidth=2, markersize=8)  # Adjust line and marker styles
    plt.xlabel('Time', fontsize=14, fontweight='bold', color='#333333')  # Adjust font size and style
    plt.ylabel('Maximum Voltage', fontsize=14, fontweight='bold', color='#333333')  # Adjust font size and style
    plt.title('Impulse Plot', fontsize=16, fontweight='bold', color='#333333')  # Adjust font size and style
    plt.grid(True, linestyle='--', alpha=0.7, color='#aaaaaa')  # Adjust grid style
    plt.xticks(fontsize=12, color='#555555')  # Adjust tick labels
    plt.yticks(fontsize=12, color='#555555')  # Adjust tick labels
    plt.tight_layout()  # Adjust layout
    plt.gca().set_facecolor('#f0f0f0')  # Set background color of plot face

# Example usage
csv_files = ['C:/Users/every/OneDrive/Desktop/CODE/4 - PPT/CALI/T0298.csv', 'C:/Users/every/OneDrive/Desktop/CODE/4 - PPT/CALI/T0299.csv']
new_csv_files = ['C:/Users/every/OneDrive/Desktop/CODE/4 - PPT/CALI/T0298_I_bit.csv', 'C:/Users/every/OneDrive/Desktop/CODE/4 - PPT/CALI/T0299_I_bit.csv']

voltage_column = "CH4"  # Adjust column name as needed
start_row = 17  # Adjust the starting row as needed

known_impulses = [1, 2, 3, 4]  # Extend known impulses to 3 and 4

# Detect maximum voltages for the initial CSV files
max_voltages = detect_max_voltage(csv_files, voltage_column, start_row)

# Calculate the slope using linear regression
model = LinearRegression()
X = pd.DataFrame(known_impulses[:len(max_voltages)])  # Ensure known impulses match the length of max_voltages
y = pd.DataFrame(max_voltages)
model.fit(X, y)
slope = model.coef_[0][0]

# Print the slope
print("Slope value:", slope)

# Plot both graphs on the same figure
plt.figure(figsize=(10, 12))  # Adjust figure size

# Plot V_max vs Known Impulses in the first subplot
plot_vmax_vs_impulses(known_impulses[:len(max_voltages)], max_voltages, 1)

# Detect maximum voltages for the new CSV files (if different from initial)
new_max_voltages = detect_max_voltage(new_csv_files, voltage_column, start_row)

# Plot I_bit vs V_max in the second subplot
plot_ibit_vs_vmax(new_max_voltages, slope, 2)

plt.show()
