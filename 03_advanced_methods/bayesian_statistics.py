import pymc3 as pm
import matplotlib.pyplot as plt

# Sample data: conversions out of visitors for variant A and B
conversions_A = 105
visitors_A = 1000
conversions_B = 120
visitors_B = 1000

with pm.Model() as model:
    # Priors for unknown model parameters
    p_A = pm.Beta('p_A', alpha=2, beta=2)
    p_B = pm.Beta('p_B', alpha=2, beta=2)

    # Deterministic to calculate the difference between p_A and p_B
    delta = pm.Deterministic('delta', p_B - p_A)
    
    # Likelihood (sampling distribution) of observations
    obs_A = pm.Binomial('obs_A', n=visitors_A, p=p_A, observed=conversions_A)
    obs_B = pm.Binomial('obs_B', n=visitors_B, p=p_B, observed=conversions_B)
    
    # Sample from the posterior
    trace = pm.sample(2000, tune=1000)

# Analyze and visualize the posterior
pm.plot_posterior(trace, var_names=['p_A', 'p_B', 'delta'], ref_val=0)
plt.savefig("posterior_plot.svg", format="svg")