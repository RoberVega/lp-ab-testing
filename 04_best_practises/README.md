# Best Practises 📌✅

This section is dedicated to polishing your rigor when performing A/B testing. There is a reason statiticians are not very popular with people: the level of rigor that proper statistics requires is high, and meticulous people can be a bit overwhelming. The main reason being that without understanding proper statistics is hard to empathise with them. But trust me, once you learn the power of proper and beauty of proper statistics, you will start appreciating clean statistics and how much value the give. 

Therefore, this section focuses on Best Practises. Let us start with the simplest indications and then move to more advanced stuff. 

## Parametric vs Non-Parametric tests

In the realm of A/B testing and hypothesis testing at large, the choice between parametric and non-parametric tests is crucial. Both approaches offer different ways to analyze data, and each comes with its own set of assumptions and best practices. Making the right choice can be the difference between drawing valid conclusions or making misguided decisions.

### Parametric Tests
These are based on specific distributional assumptions about the underlying population from which the sample is drawn. The most common assumption is that of **normality**. When these assumptions hold true, parametric tests are powerful tools that can provide precise and accurate insights. 

#### Best Practices:
- Before applying a parametric test, always assess the underlying assumptions.
- Visualize the data to check for normality, and consider formal tests (e.g., Shapiro-Wilk) if necessary.
- Be cautious with small sample sizes; distributional assumptions are more crucial in these cases.

### Non-Parametric Tests 
These tests do not rely on strict distributional assumptions and are therefore more flexible. They can be applied when data is ordinal, skewed, or when the sample size is small. Non-parametric tests rank the data rather than using the data's actual values, making them more robust against outliers. 

#### Best Practices:
- Opt for non-parametric tests when data is clearly non-normal and transformations fail to normalize it.
- Recognize that while they are more flexible, non-parametric tests can be less powerful (less likely to detect a true effect) than their parametric counterparts when parametric test assumptions are met.
- When using ranking methods, ensure the data's ordinal nature is meaningful.

Here you have two videos, an introduction to further understand these differences and a in-depth video about non-parametric tests.

<img src="../images/ftnOBcXtBEQhd.jpg" alt="" width="300" height="auto">

[Link to video](https://www.youtube.com/watch?v=ftnOBcXtBEQ)

<img src="../images/IcLSKko2tsghd.jpg" alt="" width="300" height="auto">

[Link to video](https://www.youtube.com/watch?v=IcLSKko2tsg)


In [here](cheatsheet_hypothesis_tests.md) you have a short cheatsheet on the main hypothesis tests that you can use as a reference.

## Test with a small population

Before scaling up an A/B test to a wider audience, it's a prudent strategy to soft-launch the test on a smaller, representative subset of your user base. This preliminary phase offers several invaluable advantages:

- **Verifying Test Integrity**: A soft-launch ensures that the mechanics of the A/B test are functioning as intended. This can help detect any issues with randomization, tracking, or data collection that might jeopardize the validity of the test results.

- **Identifying Glaring Issues**: If the new variant (B) has unforeseen problems or causes strong negative reactions, it's better to identify these early with a smaller group rather than risking broader user dissatisfaction.

- **Resource Efficiency**: Testing on a smaller scale can be more manageable and cost-effective. It allows you to gauge initial reactions and results without committing extensive resources.

- **Refining Test Parameters**: Based on the feedback and results from the soft-launch, you might identify opportunities to adjust and improve your testing strategy, such as refining segmentation or tweaking the design changes.

In essence, soft-launching an A/B test serves as a preparatory step, enabling businesses to ensure the test's readiness and maximize the chances of obtaining accurate, actionable insights during the full-scale test.



## Simpson's Paradox

Simpson's Paradox is a counterintuitive statistical phenomenon in which a trend that appears within several different groups disappears or reverses when the groups are combined. Essentially, it highlights the potential dangers of overlooking lurking variables and making conclusions based solely on aggregated data. 

For example, a treatment might seem to be less effective than a control when examining the total outcomes, but when accounting for a lurking variable (like age or gender), the treatment might be more effective for every subgroup within that variable. 

The paradox serves as a stark reminder of the importance of understanding the underlying structures and factors in data before drawing definitive conclusions.

<img src="../images/ebEkn-BiW5khd.jpg" alt="" width="300" height="auto">

[Link to video](https://www.youtube.com/watch?v=ebEkn-BiW5k)

## Be careful with Data Peeking

Data peeking, or the act of frequently checking the results of an A/B test before its completion, is a common pitfall that testers often fall into. While it's tempting to see early results and potentially conclude tests prematurely, doing so can introduce substantial risk of drawing incorrect conclusions. Early results may be misleading due to variability, and stopping a test based on these transient patterns can lead to false positives, meaning we believe there's a significant difference between variants when there isn't.

The dangers of data peeking underscore the importance of setting a predetermined test duration and sample size based on power calculations. By adhering to these parameters and resisting the urge to make decisions based on interim results, testers can maintain the integrity of their experiments and increase the likelihood of arriving at genuine, replicable findings.


<img src="../images/6G8F22NSCxkhd.jpg" alt="" width="300" height="auto">

[Link to video](https://www.youtube.com/watch?v=6G8F22NSCxk)


## Define "control" metrics

Instead of merely monitoring the metric we are interested in, it is good practice to divide your metrics into different categories. The goal of this procedure is to define some "control" metrics to understand and interpret our findings as rigorously as possible. 

Define three groups of metrics:
- **Expected impact** ($\alpha\sim0.05$): these are the ones you have defined your A/B test for and expect to change.
- **Potential impact** ($\alpha\sim0.01$): these are the ones you think might be affected, but in theory should remain at least similar.
- **Unlikely impact** ($\alpha\sim.0.001$): these ones are the ones you would be very surprised if they get any changes at all. 

By combining these three categories one can analyse the results and understand if a change in the metric we are interested is a solid one or if there is something suspicius going on. 



## Common mistakes in A/B testing

Finally, we give a couple of examples of common mistakes when designing or analysing A/B tests.

<img src="../images/dLwH1kp03kEhd.jpg" alt="" width="300" height="auto">

[Link to video](https://www.youtube.com/watch?v=dLwH1kp03kE)