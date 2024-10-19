You can order print and ebook versions of *Think Bayes 2e* from
[Bookshop.org](https://bookshop.org/a/98697/9781492089469) and
[Amazon](https://amzn.to/334eqGo).


## Exercises

**Exercise:** Use `conditional` to compute the following probabilities:

* What is the probability that a respondent is liberal, given that they are a Democrat?

* What is the probability that a respondent is a Democrat, given that they are liberal?

Think carefully about the order of the arguments you pass to `conditional`.


```python
# Solution goes here
conditional(liberal, given=democrat)
```




    0.3891320002215698




```python
# Solution goes here
conditional(democrat, given=liberal)
```




    0.5206403320240125



**Exercise:** Let's use the tools in this chapter to solve a variation of the Linda problem.

> Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student, she was deeply concerned with issues of discrimination and social justice, and also participated in anti-nuclear demonstrations.  Which is more probable?
> 1. Linda is a banker.
> 2. Linda is a banker and considers herself a liberal Democrat.

To answer this question, compute 

* The probability that Linda is a banker, given that she is female,

* The probability that Linda is a banker and a liberal Democrat, given that she is female.


```python
# Solution goes here
conditional(banker,female)
```




    0.02116102749801969




```python
# Solution goes here
conditional(banker & liberal & democrat, given=female)
```




    0.0023009316887329786



**Exercise:** There's a [famous quote](https://quoteinvestigator.com/2014/02/24/heart-head/) about young people, old people, liberals, and conservatives that goes something like:

> If you are not a liberal at 25, you have no heart. If you are not a conservative at 35, you have no brain.

Whether you agree with this proposition or not, it suggests some probabilities we can compute as an exercise.
Rather than use the specific ages 25 and 35, let's define `young` and `old` as under 30 or over 65:


```python
young = (gss['age'] < 30)
prob(young)
```




    0.19435991073240008




```python
old = (gss['age'] >= 65)
prob(old)
```




    0.17328058429701765



For these thresholds, I chose round numbers near the 20th and 80th percentiles.  Depending on your age, you may or may not agree with these definitions of "young" and "old".

I'll define `conservative` as someone whose political views are "Conservative", "Slightly Conservative", or "Extremely Conservative".


```python
conservative = (gss['polviews'] >= 5)
prob(conservative)
```




    0.3419354838709677



Use `prob` and `conditional` to compute the following probabilities.

* What is the probability that a randomly chosen respondent is a young liberal?

* What is the probability that a young person is liberal?

* What fraction of respondents are old conservatives?

* What fraction of conservatives are old?

For each statement, think about whether it is expressing a conjunction, a conditional probability, or both.

For the conditional probabilities, be careful about the order of the arguments.
If your answer to the last question is greater than 30%, you have it backwards!


```python
# Solution goes here
prob(liberal & young)
```




    0.06579427875836884




```python
# Solution goes here
conditional(liberal, young)
```




    0.338517745302714




```python
# Solution goes here
prob(old & conservative)
```




    0.06701156421180766




```python
# Solution goes here
conditional(old, conservative)
```




    0.19597721609113564




