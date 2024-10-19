You can order print and ebook versions of *Think Bayes 2e* from
[Bookshop.org](https://bookshop.org/a/98697/9781492089469) and
[Amazon](https://amzn.to/334eqGo).


## Exercises

**Exercise:** Suppose you have two coins in a box.
One is a normal coin with heads on one side and tails on the other, and one is a trick coin with heads on both sides.  You choose a coin at random and see that one of the sides is heads.
What is the probability that you chose the trick coin?


```python
# Solution goes here
table4 = pd.DataFrame(index=['normal', 'trick'])
table4['prior'] = 1/2
table4['likelihood'] = 1/2, 1
update(table4)
table4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prior</th>
      <th>likelihood</th>
      <th>unnorm</th>
      <th>posterior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>normal</th>
      <td>0.5</td>
      <td>0.5</td>
      <td>0.25</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>trick</th>
      <td>0.5</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>0.666667</td>
    </tr>
  </tbody>
</table>
</div>



**Exercise:** Suppose you meet someone and learn that they have two children.
You ask if either child is a girl and they say yes.
What is the probability that both children are girls?

Hint: Start with four equally likely hypotheses.


```python
# Solution goes here
table5 = pd.DataFrame(index=['GG', 'GB', 'BG', 'BB'])
table5['prior'] = 1/4
table5['likelihood'] = 1, 1, 1, 0
update(table5)
table5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prior</th>
      <th>likelihood</th>
      <th>unnorm</th>
      <th>posterior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GG</th>
      <td>0.25</td>
      <td>1</td>
      <td>0.25</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>GB</th>
      <td>0.25</td>
      <td>1</td>
      <td>0.25</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>BG</th>
      <td>0.25</td>
      <td>1</td>
      <td>0.25</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>BB</th>
      <td>0.25</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>



**Exercise:** There are many variations of the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).  
For example, suppose Monty always chooses Door 2 if he can, and
only chooses Door 3 if he has to (because the car is behind Door 2).

If you choose Door 1 and Monty opens Door 2, what is the probability the car is behind Door 3?

If you choose Door 1 and Monty opens Door 3, what is the probability the car is behind Door 2?


```python
# Solution goes here
#Car behind door1 -> Open door 2
#Car behind door 2 -> Open door 3
#Car behind door 3 -> Open door 2

table6 = pd.DataFrame(index=['Door1', 'Door2', 'Door3'])
table6['prior']= 1/3
table6['likelihood'] = 1, 0, 1
update(table6)
table6
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prior</th>
      <th>likelihood</th>
      <th>unnorm</th>
      <th>posterior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Door1</th>
      <td>0.333333</td>
      <td>1</td>
      <td>0.333333</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>Door2</th>
      <td>0.333333</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Door3</th>
      <td>0.333333</td>
      <td>1</td>
      <td>0.333333</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Solution goes here
#Car behind door1 -> Open door 2
#Car behind door 2 -> Open door 3
#Car behind door 3 -> Open door 2

table7 = pd.DataFrame(index=['Door 1', 'Door 2', 'Door 3'])
table7['prior'] = 1/3
table7['likelihood'] = 0, 1, 0
update(table7)
table7
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prior</th>
      <th>likelihood</th>
      <th>unnorm</th>
      <th>posterior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Door 1</th>
      <td>0.333333</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Door 2</th>
      <td>0.333333</td>
      <td>1</td>
      <td>0.333333</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Door 3</th>
      <td>0.333333</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



**Exercise:** M&M's are small candy-coated chocolates that come in a variety of colors.  
Mars, Inc., which makes M&M's, changes the mixture of colors from time to time.
In 1995, they introduced blue M&M's.  

* In 1994, the color mix in a bag of plain M&M's was 30\% Brown, 20\% Yellow, 20\% Red, 10\% Green, 10\% Orange, 10\% Tan.  

* In 1996, it was 24\% Blue , 20\% Green, 16\% Orange, 14\% Yellow, 13\% Red, 13\% Brown.

Suppose a friend of mine has two bags of M&M's, and he tells me
that one is from 1994 and one from 1996.  He won't tell me which is
which, but he gives me one M&M from each bag.  One is yellow and
one is green.  What is the probability that the yellow one came
from the 1994 bag?

Hint: The trick to this question is to define the hypotheses and the data carefully.


```python
# Solution goes here
#H1: Yellow 94 , green 96
#H2: Green 94, Yellow 96

table8 = pd.DataFrame(index=['H1', 'H2'])
table8['prior'] = 1/2
table8['likelihood'] = 0.2*0.2, 0.1*0.14
update(table8)
table8
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prior</th>
      <th>likelihood</th>
      <th>unnorm</th>
      <th>posterior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>H1</th>
      <td>0.5</td>
      <td>0.040</td>
      <td>0.020</td>
      <td>0.740741</td>
    </tr>
    <tr>
      <th>H2</th>
      <td>0.5</td>
      <td>0.014</td>
      <td>0.007</td>
      <td>0.259259</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
