import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def plot_combined_blank():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Plot V_max vs Known Impulses in the first subplot
    ax1.set_xlabel('Number of Known Impulse', fontsize=14, fontweight='bold', color='#333333')
    ax1.set_ylabel('Maximum Voltage', fontsize=14, fontweight='bold', color='#333333')
    ax1.set_title('Linear Impulses', fontsize=16, fontweight='bold', color='#333333')
    ax1.grid(True, linestyle='--', alpha=0.7, color='#aaaaaa')
    ax1.tick_params(axis='x', labelsize=12, colors='#555555')
    ax1.tick_params(axis='y', labelsize=12, colors='#555555')
    ax1.set_facecolor('#f0f0f0')

    # Plot I_bit vs V_max in the second subplot
    ax2.set_xlabel('Time', fontsize=14, fontweight='bold', color='#333333')
    ax2.set_ylabel('Maximum Voltage', fontsize=14, fontweight='bold', color='#333333')
    ax2.set_title('Impulse Plot', fontsize=16, fontweight='bold', color='#333333')
    ax2.grid(True, linestyle='--', alpha=0.7, color='#aaaaaa')
    ax2.tick_params(axis='x', labelsize=12, colors='#555555')
    ax2.tick_params(axis='y', labelsize=12, colors='#555555')
    ax2.set_facecolor('#f0f0f0')

    # Add export plots button
    export_button_ax = plt.axes([0.85, 0.01, 0.1, 0.05])  # Adjust the y-position here
    export_button = Button(export_button_ax, 'Export Plots')

plot_combined_blank()
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
