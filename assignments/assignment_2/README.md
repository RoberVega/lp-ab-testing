# Assignment 2

You are provided with a preliminary dataset `data/preliminary_data.csv` from an insurance campaign. Before launching the full campaign and A/B testing it, you wish to determine the optimal sample size and ensure that the randomization process is robust.

The dataset contains:

- `user_id`
- `region`: the region where the user is from ("Norte", "Centro", "Lisboa", "Alentejo", "Algarve", "Madeira", "Azores")
- `age_group`: categorized age groups of the users ("18-25", "26-35", "36-45", "46-55", "56-65", "65+")
- `interacted`: if the user had any interaction with our preliminary campaign

## Sample Size Determination:

1. Determine the baseline conversion rate using the preliminary data.
2. Use `statsmodels` to determine the required sample size for the A/B test, assuming you want to detect a 3% increase in the conversion rate with 80% power and a significance level of 5%.

## Randomization Techniques:

Now that you know the approximate size of the sample, you can use to the `data/remaining_users.csv`, where you will have the rest of the users that you will use to design your A/B test. 

3. Propose two methods (don't forget to **only** select the number of users you computed in 2):
    * a method using `numpy` or `pandas` to randomly assign users to either Variant A or Variant B.
    * another method but now using `sklearn` ensuring an even distribution across `region` and `age_group`.
4. Create two functions in Python that, when given a dataset, returns a new dataset with an additional column variant indicating the variant assigned to each `user_id`.

## Data Integrity:

5. After randomization, compare both approaches by visualizing the distributions of users across the variants for each `region` and `age_group`. Which method seems more appropriate?

## Preliminary Testing:

6. Using the functions designed in step 4, assign variants to the users in the `remaining_users.csv`. The column should be called `version` and the versions should be called `A` and `B`. 
7. We have prepare the function `get_results` in the `results_generator/run_experiment.py`. You only need to import it and pass your dataframe to it, like so `get_results(df)`. Calculate the conversion rate for both Variant A and Variant B from this preliminary test. Discuss if the results are statistically significant or if further testing with a larger sample is necessary.

