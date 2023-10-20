import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

def sequential_test(data, variant, alpha=0.05):
    """
    Perform the sequential test comparing the given variant against the Standard.
    
    Parameters:
    - data: The dataset containing the test results.
    - variant: The product variant to be compared ('New_Feature_A' or 'New_Feature_B').
    - alpha: Significance level
    
    Returns:
    - p_values: List of p-values for each step.
    """
    
    group_Standard = data[data['product_variant'] == 'Standard']
    group_Variant = data[data['product_variant'] == variant]
    
    p_values = []

    min_len = min(len(group_Standard), len(group_Variant))

    for i in range(2, min_len):
        count = [group_Standard['purchased'].iloc[:i].sum(), group_Variant['purchased'].iloc[:i].sum()]
        nobs = [i, i]
        
        # Perform the z-test
        _, p = proportions_ztest(count, nobs)
        p_values.append(p)

    return p_values

def main():
    data = pd.read_csv('data/campaign_data.csv')
    
    p_values_A = sequential_test(data, 'New_Feature_A')
    p_values_B = sequential_test(data, 'New_Feature_B')
    
    # Visualization
    plt.figure(figsize=(10,6))
    plt.plot(p_values_A, label="P-value (New_Feature_A vs Standard)", color='blue')
    plt.plot(p_values_B, label="P-value (New_Feature_B vs Standard)", color='green')
    plt.axhline(0.05, color='red', linestyle='--', label='Significance Level (alpha=0.05)')
    plt.title("P-value Progression over Sequential Testing")
    plt.xlabel("Number of Data Points")
    plt.ylabel("P-value")
    plt.legend()
    plt.grid(True)
    
    plt.savefig('sequential_testing.png', dpi=300)

if __name__ == "__main__":
    main()

