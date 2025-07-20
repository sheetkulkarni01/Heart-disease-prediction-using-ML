import matplotlib.pyplot as plt
from statistics import mean, median
import os

def styled_histogram(pos_data, neg_data, feature_name, xlabel, filename=None):
    # Compute stats
    mean_pos = mean(pos_data)
    median_pos = median(pos_data)
    mean_neg = mean(neg_data)
    median_neg = median(neg_data)

    # Console Output
    print(f"\n === {feature_name.upper()} ===")
    print("With Heart Disease")
    print(f"Mean: {mean_pos:.2f}")
    print(f"Median: {median_pos:.2f}")
    print("No Heart Disease")
    print(f"Mean: {mean_neg:.2f}")
    print(f"Median: {median_neg:.2f}")

    save_path = os.path.join("Plots", filename) if filename else None

    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(12, 5), facecolor="#f7f7f7")

    axs[0].hist(pos_data, bins=15, color='crimson', edgecolor='black', alpha=0.7, label='With Heart Disease')
    axs[1].hist(neg_data, bins=15, color='teal', edgecolor='black', alpha=0.7, label='No Heart Disease')

    axs[0].set_title(f'{feature_name} (Heart Disease)', fontsize=12)
    axs[1].set_title(f'{feature_name} (Healthy)', fontsize=12)

    for ax in axs:
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Frequency")
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend(loc='upper right')

    plt.suptitle(f"Comparison of {feature_name} between Patients", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    # Save if filename is provided
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Plot saved at: {save_path}")

    plt.show()

