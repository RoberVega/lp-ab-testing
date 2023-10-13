 # Assignment 1

We have provided you with a dataset `data/ab_test_data.csv`. Assume it to be an extremely simplified version of an A/B testing in which we have
- `user_id`
- `variant`: whether we used campaign $A$ or campaign $B$ 
- `converted`: whether the user bought our insurance or not

## Basic Exploratory Data Analysis (EDA):
1. Calculate the policy purchase rate for both Variant A and Variant B.
2. Visualize the distribution of policy purchases for both variants using a bar graph.

## Hypothesis Formulation:
3. State the null hypothesis and alternative hypothesis.
4. Decide on a significance level ($\alpha$).

## Statistical Test:
5. Choose an appropriate statistical test for this A/B test (e.g., two-proportions z-test).
6. Perform the test using Python and state the resulting p-value.

## Evaluation:
7. Based on the p-value, decide whether to reject the null hypothesis.
8. Discuss Type I and Type II errors in the context of your decision. What would be the implications of each error type for the insurance company?