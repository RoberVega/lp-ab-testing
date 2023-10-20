import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

def sequential_test_zstat(data, variant):

    group_Standard = data[data['product_variant'] == 'Standard']
    group_Variant = data[data['product_variant'] == variant]
    
    z_stats = []

    min_len = min(len(group_Standard), len(group_Variant))

    for i in range(2, min_len):
        count = [group_Standard['purchased'].iloc[:i].sum(), group_Variant['purchased'].iloc[:i].sum()]
        nobs = [i, i]
        
        # Compute the Z-statistic
        stat, _ = proportions_ztest(count, nobs)
        z_stats.append(stat)

    return z_stats

def main():
    data = pd.read_csv('data/campaign_data.csv')
    
    z_stats_A = sequential_test_zstat(data, 'New_Feature_A')
    z_stats_B = sequential_test_zstat(data, 'New_Feature_B')
    
    # Visualization
    plt.figure(figsize=(10,6))
    plt.plot(z_stats_A, label="z-stat (New_Feature_A vs Standard)", color='blue')
    plt.plot(z_stats_B, label="z-stat (New_Feature_B vs Standard)", color='green')
    plt.axhline(1.96, color='red', linestyle='--', label='Upper Bound')
    plt.axhline(-1.96, color='red', linestyle='--', label='Lower Bound')
    plt.title("z-statistic Progression over Sequential Testing")
    plt.xlabel("Number of Data Points")
    plt.ylabel("z-statistic")
    plt.legend()
    plt.grid(True)
    
    plt.savefig('sequential_testing_zstat.png', dpi=300)

if __name__ == "__main__":
    main()
