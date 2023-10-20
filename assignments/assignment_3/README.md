# Assignment 3

In this assignment, you'll delve deeper into understanding A/B testing using Bayesian statistics, multi-armed bandits, and sequential testing techniques. By the end of this assignment, you should be able to integrate advanced statistical concepts into real-world A/B testing scenarios.

You are provided with a new dataset, `data/campaign_data.csv`, for a new product launch. The dataset contains:

- `user_id`
- product_variant: the version of the product the user saw ("Standard", "New_Feature_A", "New_Feature_B")
- `clicked`: if the user clicked on the product (0 for no, 1 for yes)
- `purchased`: if the user purchased the product after clicking (0 for no, 1 for yes)

## Bayesian A/B Testing:

1. Using `PyMC3`, construct a Bayesian model to estimate the posterior distributions for the conversion rates of each product variant. Display the distributions graphically.
2. Calculate the probability that "New_Feature_A" has a higher conversion rate than "Standard" and similarly for "New_Feature_B" versus "Standard".

## Multi-Armed Bandits:

Imagine you are dynamically assigning users to different product variants based on the observed conversion rates.

3. Implement the $\varepsilon$-greedy algorithm to decide which variant to show to the users. Use a decaying epsilon value.
4. Simulate the multi-armed bandit scenario for 10,000 users and compare the cumulative rewards (i.e., purchases) obtained using the $\varepsilon$-greedy algorithm against a random assignment approach.

## Sequential Testing:

The idea behind sequential testing is to reduce the time taken to decide between product variants by continuously monitoring the results and potentially stopping the experiment early.

5. Implement a basic sequential testing approach using the Wald's Sequential Probability Ratio Test (SPRT). Determine if, at any point, you can conclude that one of the product variants is better than the "Standard" variant.
6. Compare the results of the sequential test with the Bayesian A/B test results. Discuss the advantages and disadvantages of each approach.

## Bonus (Optional):

7. Integrate the multi-armed bandit with Bayesian updating. After each user interaction, update the conversion rate distribution for the chosen variant using PyMC3 and use it to guide the next $\varepsilon$-greedy decision.