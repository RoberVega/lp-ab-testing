import pandas as pd
import pymc3 as pm
import matplotlib.pyplot as plt

def run_bayesian_analysis(data):
    with pm.Model() as model:
        # Priors
        p_Standard = pm.Beta("p_Standard", alpha=2, beta=2)
        p_A = pm.Beta("p_A", alpha=2, beta=2)
        p_B = pm.Beta("p_B", alpha=2, beta=2)
        
        delta_A = pm.Deterministic("delta_A", p_A - p_Standard)
        delta_B = pm.Deterministic("delta_B", p_B - p_Standard)

        # Likelihood
        obs_Standard = pm.Bernoulli("obs_Standard", p_Standard, observed=data[data['product_variant'] == 'Standard']['purchased'])
        obs_A = pm.Bernoulli("obs_A", p_A, observed=data[data['product_variant'] == 'New_Feature_A']['purchased'])
        obs_B = pm.Bernoulli("obs_B", p_B, observed=data[data['product_variant'] == 'New_Feature_B']['purchased'])

        # Sampling
        trace = pm.sample(2000, tune=1000, target_accept=0.95)
    
    return trace

def main():
    data = pd.read_csv('data/campaign_data.csv')
    trace = run_bayesian_analysis(data)

    # Plotting
    pm.plot_posterior(trace, var_names=['p_Standard', 'p_A', 'p_B', 'delta_A', 'delta_B'], 
                      ref_val=0, color='#87ceeb')
    
    plt.savefig('bayesian_posterior.png', dpi=300)

if __name__ == "__main__":
    main()


