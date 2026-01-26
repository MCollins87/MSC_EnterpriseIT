[Back to Unit](./Unit7.md)

# Hypothesis Testing Using LibreOffice

## The Related Samples T Test

Consider the container design data in Data Set F Designs (see the Data Annexe). Notice that the two variables Con1 and Con 2 indeed measure the same characteristic (the number of items sold), but under two different “conditions” (the two different container designs). 

We conduct a two-tailed related samples t test of whether the underlying (population) mean number of items sold differs between the two container designs. 

Strictly speaking, before undertaking the test we should calculate the differences **D = Con1 – Con 2** for each observation. A normal plot of these differences (i.e., of the values of the variable D) should then be constructed in order to check whether the data are acceptably near-normally distributed. 

We will assume for now that the data are indeed so distributed so that the resulting t test is valid. You might want to construct the normal plot as an additional exercise. (Ensure you save your answers in the Exercise sheets for your submission.) 
1. Open the Excel workbook [Exa 7.4F.xlsx](./Exa%207.4F.xlsx) from the Examples folder. This contains the relevant data. 
2. From the Data menu bar tab, select Statistics and from the ensuing dialogue box, select Paired t-test. A new dialogue box appears. 
3. In the Variable 1 Range box, enter the cell range where the data for the first variable (Con1) can be found, that is, the range B2:B11. In the Variable 2 Range box, enter the cell range where the data for the second variable (Con2) can be found, that is, the range C2:C11. 
4. Put the results in the cell. 
 
The resulting output is presented below. Not all this output is relevant, so it need not all be discussed. The obtained related samples t = 2.875 with 9 degrees of freedom. The associated two- tailed p-value is p = 0.018, so the observed t is significant at the 5% level (two-tailed). 

| **Paired t-test**             |                   |                  |
| ----------------------------- | ----------------- | ---------------- |		
| Alpha	                        | 0.05	            |                  |
| Hypothesized Mean Difference  | 0 	            |                  |
|                               | **Variable 1**    | **Variable 2**   |
| Mean	                        | 172.6             |159.4             |
| Variance                      | 750.267           |789.3778          |
| Observations                  | 10                | 10               |
| Pearson Correlation           | 0.863             |                  |
| Observed Mean Difference      | 13.2              |                  |	
| Variance of the Differences	| 210.8444          |                  |
| df                            | 9                 |	               |
| t Stat                        | 2.875             |	               |
| P (T<=t) one-tail	            | 0.009             |	               |
| t Critical one-tail           | 1.833             |	               |
| P (T<=t) two-tail             | 0.018             |                  |
| t Critical two-tail           | 2.262             |	               |

The sample mean numbers of items sold for Container Designs 1 and 2 were, respectively 172.6 and 159.4. The data therefore constitute significant evidence that the underlying mean number of containers sold was greater for Design 1, by an estimated 172.6-159.4 = 13.2 items per store. The results suggest that Design 1 should be preferred. 

### Excercise
Consider the filtration data of Data Set G. Open the Excel workbook Exe

7.4G.xlsx which contains these data from the Exercises folder. 

Assuming the data to be suitably distributed, complete a two-tailed test of whether the population mean impurity differs between the two filtration agents, and interpret your findings. 

#### Results

| Paired t-test                 |	                |                   |
| ----------------------------- | ----------------- | ----------------- |
| Alpha	                        | 0.05              |	                |
| Hypothesized Mean Difference  | 0                 |	                |
|                               | **Variable 1**    | **Variable 2**    |
| Mean	                        | 8.250	            | 8.683             |
| Variance	                    | 1.059	            | 1.078             |
| Observations	                | 12                | 12                |
| Pearson Correlation	        | 0.901             |	                |
| Observed Mean Difference	    | -0.433            |	                |
| Variance of the Differences	| 0.212             |	                |
| df	                        | 11                |	                |
| t Stat	                    | -3.264            |	                |
| P (T<=t) one-tail	            | 0.004             |	                |
| t Critical one-tail	        | 1.796             |	                |
| P (T<=t) two-tail	            | 0.008             |	                |
| t Critical two-tail	        | 2.201             |	                |

- The two-tailed p-value = 0.0076 < 0.05 indicates a statistically significant difference in mean impurity between the two agents. 
- The mean difference is negative (-0.433).
- Agent 1 produces a lower mean impurity than Agent 2 by an estimated 0.43 impurity units on average 

If lower impurity is the goal, Agent 1 should be preferred based on these data.

## The One-Taled Test
### Example

Recall that we conducted a two-tailed related samples t test of whether the underlying (population) mean number of items sold differs between the two container designs of data Set F Designs. 

However, now suppose that Container Design 1 is a new, hopefully more attractive design, whereas Container Design 2 is the design in current use. Presumably, the company will only go to the expense of implementing the new design if it can be shown to lead to higher sales than the current design. 

Thus, the investigators seek evidence that 1 > 2, so wish to test: H0: 1  2 against H1: 1 > 2. The relevant t test is conducted exactly as before. However, this time, the results are interpreted a little differently. 

We first check whether the data are consistent with the one-tailed alternative hypothesis. As before, the sample mean numbers of items sold for Container Designs 1 and 2 were, respectively 172.6 and 159.4, so that the data are indeed consistent with H1. 

As before, the obtained related samples t = 2.875 with 9 degrees of freedom. The associated one-tailed p-value is p = 0.009, so the observed t is significant at the 1% level (one-tailed). 

| **t-Test: Paired Two Sample for Means**   |               |               |
| ----------------------------------------- | ------------- | ------------- | 
|                                           | Con1          | Con2          |
| Mean                                      | 172.6         | 159.4         |
| Variance                                  | 750.2666667   | 789.3777778   |
| Observations                              | 10            | 10            |
| Pearson Correlation                       | 0.863335004   |               |
| Hypothesised Mean Difference              | 0             |               |
| df                                        | 9             |               |
| t Stat                                    | 2.874702125   |               |
| P(T<=t) one-tail                          | 0.009167817   |               |
| t Critical one-tail                       | 1.833112923   |               |
| P(T<=t) two-tail                          | 0.018335635   |               |
| t Critical two-tail                       | 2.262157158   |               |
| Difference in Means                       | 13.2          |               |
 
 
The data therefore constitute strong evidence (on a one-tailed test) that the underlying mean number of containers sold was greater for Design 1, by an estimated 172.6 - 159.4 = 13.2 items per store. The results continue to suggest that Design 1 should be preferred. 

Although broadly similar conclusions were reached as before, a higher level of significance was obtained with the one-tailed test. 

Notice that if we had sought to test the alternative pair of one-tailed hypotheses H0: 1 ≥ 2 against H1: 1 < 2 we would have found the difference in sample means to be consistent with the null hypothesis that the population mean sales for Design 2 was no greater than that for Design 1. We would thus have declared the result to be not significant without even bothering to inspect the p-value. 

### Excercise
Recall that in Exercise 8.4, a two-tailed test was undertaken of whether the population mean impurity differs between the two filtration agents in Data Set G. 
Suppose instead a one-tailed test had been conducted to determine whether Filter Agent 1 was the more effective. What would your conclusions have been? 

#### Results
Since the observed t value is:
- t = −3.264 (strongly negative)
- one‑tailed p = 0.00377 (half two tailed)

and p = 0.00377 < 0.05, we reject H₀.

Under a one-tailed test with the hypothesis that Filter Agent 1 is more effective (i.e., produces lower impurity):

We conclude that Filter Agent 1 is significantly more effective than Filter Agent 2.

The evidence is even stronger in the one‑tailed test than in the two‑tailed test, because all of the difference is in the expected direction (Agent 1 having lower impurity).

## The Independant Samples T Test

Consider again Data Set B Diets, the dietary data. Not unreasonably, we wish to test whether the population mean weighe data provide strong statistical support for choosing Agent 1.ht loss differs between the two diets. Since completely separate samples of individuals undertook the two diets (i.e., no-one underwent both diets), the independent samples t test is appropriate here. 

We know that such a test (and the F test that precedes it) will yield valid results, as we have already completed normal plots for the weight loss data for each of the two diets and have found both sets of data to exhibit acceptable near normality. 

1. Open the Excel workbook Exa 7.6B.xlsx from the Examples folder. This contains the relevant data, together with some of the previously calculated summary statistics for the weight loss on each diet. We begin by performing the F test of variances. 
2. From the Data menu bar tab, select Statistics and from the ensuing dialogue box, choose F-test. A further dialogue box opens. 
3. In the Variable 1 Range box, enter the cell range where the Diet A weight losses can be found (B2:B51), and in the Variable 2 Range box, enter the cell range where the Diet B weight losses can be found (B52:B101). 
4. Put the results in H2. 
 5. Some output appears. Widen columns H to J to render it legible. In cell H14, type: p2, and in cell I14, enter the formula: =2*I11 to obtain the required two-tailed p-value. 
 
The relevant output is as follows (to 3 decimal places): 
 
|**F Test**|||
| --- | --- | ---
|Alpha|0.05||
||Variable 1|Variable 2|
|Mean|5.341|3.710|
|Variance|6.429|7.668|
|Observations|50.000|50.000|
|df|49.000|49.000|
|F|0.839||
|P (F<=f) right-tail|0.730||
|F Critical right-tail|1.607||
|P (F<=f) left-tail|0.270||
|F Critical left-tail|0.622||
|P two-tail|0.540||
||||
|F Critical two-tail|0.567|1.762|
 
The sample variances for the two diets are, respectively 𝑠2 = 6.429 and 𝑠2 = 7.668. The observed F 
1 	2 test statistic is F = 0.839 with 49 and 49 associated degrees of freedom, giving a two tailed p-value of p 
= 0.5399NS. 
 
The observed F ratio is thus not significant. The data are consistent with the assumption that the population variances underlying the weight losses under the two diets do not differ, and we therefore proceed to use the equal variances form of the independent samples t test. 
 
Since we wish to test if the population mean weight losses differ between the two diets, a two-tailed t test is appropriate here. 
1. We will use the formula =TTEST(data1;data2;mode;type). Here the first two are self-explanatory, mode indicates whether it is a 1 tailed test (1) or a two tailed test (2), type indicates whether it is a paired t test (1), an equal variances independent t test (2) or and unequal variances independent t test (3). This then returns the p-value for the chosen test. 
2. As we have chosen a two tailed test then our formula will read =TTEST(B2:B51,B52:B101,2,2). We have shown above that we can assume equal variances. 

The output is as follows (The one tailed p-value is included for completeness): 
 
Two-tailed 0.00275154 P-value 
 
One-tailed 	0.00137577 P-value 
 
The associated two-tailed p-value is p = 0.0028, so the observed t is significant at the 1% level (two- tailed). The sample mean weight losses for Diets A and B were, respectively, 5.341 kg and 3.710 kg. Notice that these findings are consistent with the results of Example 3.1 and Exercise 3.1. 

The data therefore constitute strong evidence that the underlying mean weight loss was greater for Diet A, by an estimated 5.314 – 3.710 = 1.631 kg. The results strongly suggest that Diet A is more effective in producing a weight loss. 

### Excercise
Consider the bank cardholder data of Data Set C Superplus. Open the Excel workbook Exa7.6C.xlsx which contains this data from the Exercises folder. 

Assuming the data to be suitably distributed, complete an appropriate test of whether the population mean income for males exceeds that of females and interpret your findings. What assumptions underpin the validity of your analysis, and how could you validate them? 

#### Results

|                       |                     |                  |
| --------------------- | ------------------- | ---------------- |
| F-test                |                     |                  |
| Alpha                 | 0.05                |                  |
|                       | Male                | Female           |
| Mean                  | 52.9133333333333    | 44.2333333333333 |
| Variance              | 233.128971751412    | 190.17581920904  |
| Observations          | 60                  | 60               |
| df                    | 59                  | 59               |
| F                     | 1.22586022093145    |                  |
| P (F<=f) right-tail   | 0.218246240191822   |                  |
| F Critical right-tail | 1.53995660740408    |                  |
| P (F<=f) left-tail    | 0.781753759808178   |                  |
| F Critical left-tail  | 0.649368946626172   |                  |
| P two-tail            | 0.436492480383643   |                  |
| F Critical two-tail   | 0.597324477223157   | 1.67413196366705 |
|                       |                     |                  |
| T Test                | 0.00141947042516854 |                  |

Testing population mean income for males exceeds that of females, use a one‑tailed two‑sample t‑test with the following hypotheses:

H₀: μ_Male ≤ μ_Female
H₁: μ_Male > μ_Female

F‑test for equality of variances:

F = 1.226, p (two‑tail) = 0.436 (n₁ = n₂ = 60)

So there’s no evidence of unequal variances at α = 0.05. It’s therefore appropriate to use the pooled-variance (equal variances) t‑test. 

At α = 0.05 (or even α = 0.01), the one‑tailed p-value ≈ 0.00071 is far below α, so we reject H₀.

Conclusion: There is strong evidence that mean income for males exceeds that of females in the population.

Estimated difference in means: ≈ 8.68 income units (Male − Female).
