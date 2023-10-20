# Parametric tests
## t-test (Student's t-test)
### Purpose: 
Compare the means of two groups.
### Assumptions:
- Data is continuous.
- The data follows a normal distribution (or nearly normal).
- The variances of the two groups are equal (for an independent two-sample t-test with equal variance). If variances are not equal, a variation called Welch’s t-test can be used.
- Observations are independent of each other.

## z-test
### Purpose: 
Compare the mean of a sample to a known population mean (one-sample z-test) or compare the means of two large samples.
### Assumptions:
- Sample size is large (typically n > 30).
- Data has a normal distribution, or the sample size is sufficiently large for the Central Limit Theorem to apply.
- Known population variance (rarely met in practice; if variance is unknown, a t-test is often preferred).

## ANOVA (Analysis of Variance)
### Purpose: 
Compare the means of three or more groups.
### Assumptions:
- Data is continuous.
- Data follows a normal distribution within each group.
- Homogeneity of variances (variances are equal across groups).
- Observations are independent.

## Chi-square test
### Purpose: 
Test the association between categorical variables.
### Assumptions:
- Expected frequencies in each cell should be at least 5.
- Observations are independent.

.
# Non-Parametric tests
## Mann-Whitney U Test (Wilcoxon Rank Sum Test)
### Purpose: 
Non-parametric alternative to the t-test; compare two independent samples.
### Assumptions:
- Data does not need to be normally distributed.
- Observations are independent.
- The distributions of both groups are the same shape.

## Wilcoxon Signed-Rank Test
### Purpose: 
Non-parametric alternative to the paired t-test; compare two related samples.
### Assumptions:
- Data does not need to be normally distributed.
- The differences between pairs follow a symmetric distribution.

## Kruskal-Wallis Test
### Purpose: 
Non-parametric alternative to ANOVA; compare three or more independent samples.
### Assumptions:
- Data does not need to be normally distributed.
- Observations are independent.
- The distributions of all groups are the same shape.

## Spearman's Rank Correlation
### Purpose: 
Assess the strength and direction of the monotonic relationship between two variables.
### Assumptions:
- Data does not need to be normally distributed.
- The relationship is monotonic.