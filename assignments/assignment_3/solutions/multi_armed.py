import numpy as np
import pandas as pd


class EpsilonGreedy:
    def __init__(self, df, variants, epsilon, decay_rate):
        self.df = df
        self.variants = variants
        self.epsilon = epsilon
        self.decay_rate = decay_rate
        self.counts = {variant: 0 for variant in variants}
        self.values = {variant: 0.0 for variant in variants}

    def select_variant(self):
        # Exploration
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.variants)
        # Exploitation
        else:
            return max(self.values, key=self.values.get)

    def get_reward_from_dataset(self, variant):
        # Get a random reward (purchase) from the dataset for the selected variant
        variant_data = self.df[self.df['product_variant'] == variant]
        random_user = variant_data.sample(1)
        return random_user['purchased'].values[0]

    def update(self, variant, reward):
        self.counts[variant] += 1
        n = self.counts[variant]
        value = self.values[variant]
        # Update the running average of rewards
        self.values[variant] = ((n - 1) / n) * value + (1 / n) * reward

    def run(self, n_trials):
        total_reward = 0
        for _ in range(n_trials):
            selected_variant = self.select_variant()
            reward = self.get_reward_from_dataset(selected_variant)
            self.update(selected_variant, reward)
            total_reward += reward
            # Decay the epsilon value
            self.epsilon *= self.decay_rate
        return total_reward


def main():
    df = pd.read_csv('data/campaign_data.csv')
    variants = ["Standard", "New_Feature_A", "New_Feature_B"]
    bandit = EpsilonGreedy(df, variants, epsilon=1.0, decay_rate=0.99)
    total_reward = bandit.run(10000)
    print(f"Total rewards after 10,000 trials: {total_reward}")


if __name__ == "__main__":
    main()