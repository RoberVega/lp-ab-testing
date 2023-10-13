import statsmodels.stats.api as sms
from typing import Optional
def compute_sample_size(
        baseline_conversion_rate: float,
        minimum_detectable_effect: float,
        alpha: float = 0.05,
        power: float = 0.8):

    effect_size = sms.proportion_effectsize(
        baseline_conversion_rate,
        baseline_conversion_rate + minimum_detectable_effect
    )
    sample_size = (sms.NormalIndPower()
                   .solve_power(effect_size=effect_size,
                                alpha=alpha,
                                power=power,
                                ratio=1)
    )

    # Return the sample size rounded up to the nearest whole number
    return int(round(sample_size))

if __name__ == "__main__":
    baseline_rate = 0.1  # example: 10% current conversion rate
    effect_size = 0.02   # example: you want to detect a 2% increase
    alpha = 0.05
    power = 0.8

    required_sample_size = compute_sample_size(baseline_rate, effect_size, alpha, power)
    print(f"Required sample size per group: {required_sample_size}")

