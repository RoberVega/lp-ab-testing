# Multi-armed bandits 🎰🎰🎰🎰

Following Bayesian methods, we stumble upon the fascinating world of multi-armed bandits. Instead of the traditional split-testing, this dynamic approach adjusts the traffic allocation to different variants in real-time based on their performance.

## The Casino Analogy 🎰🎰🎰🎰

Imagine you're at a casino facing multiple slot machines (bandits). Each machine provides a different but unknown reward probability. Your challenge? To decide which arm to pull to maximize your total reward over a series of trials.

In digital terms, think of each "arm" as a variant of your campaign. The multi-armed bandit algorithm helps you dynamically allocate more traffic to better-performing variants, rather than waiting for a test to conclude as in traditional A/B testing.

## Exploration vs Exploitation

The method of multi-armed bandits is based on two important terms: exploration and exploitation

<img src="../images/e3L4VocZnnQsd.jpg" alt="" width="300" height="auto">

[Link to video](https://www.youtube.com/watch?v=e3L4VocZnnQ)


## Advantages of MAB

- **Real-time Learning**: MAB algorithms continuously learn and adjust the traffic allocation.
- **Regret Minimization**: By dynamically adjusting, they reduce the chance of sticking to underperforming variants.
- **Less Wasted Traffic**: More users experience the better-performing variant sooner.
- **Handles Exploration vs. Exploitation**: Striking a balance between trying all variants and settling on the best.

## A Simple Python Simulation

The $\varepsilon$-greedy strategy is a common MAB approach. Here's how you can simulate it:

```python

import numpy as np

# True conversion rates and the number of variants
true_conversion_rates = [0.1, 0.12, 0.11]
n_arms = len(true_conversion_rates)

# Number of trials and epsilon
n_trials = 10000
epsilon = 0.1

counts = np.zeros(n_arms)
wins = np.zeros(n_arms)

for _ in range(n_trials):
    # Epsilon greedy strategy
    if np.random.rand() < epsilon:
        # Explore: choose a random arm
        chosen_arm = np.random.randint(n_arms)
    else:
        # Exploit: choose the arm with the highest current conversion rate
        chosen_arm = np.argmax(wins / (counts + 1))

    # Simulate user interaction and update counts & wins
    reward = np.random.rand() < true_conversion_rates[chosen_arm]
    counts[chosen_arm] += 1
    wins[chosen_arm] += reward

# Estimated conversion rates
print(wins / counts)
```

This simulation lets you observe how the $\varepsilon$-greedy strategy performs, exploring randomly with probability $\varepsilon$ and exploiting the best-performing arm otherwise.

For an extended exploration, we refer you to the following [article](https://tech.clevertap.com/maximising-your-a-b-test-outcomes-with-multi-armed-bandits/) in which you will also learn alternative methods to $\varepsilon$-greedy. Fortunately, it also comes with [code](https://github.com/SidJain1412/MultiArmBanditExploration/blob/main/MultiArmedBanditExploration.ipynb).
