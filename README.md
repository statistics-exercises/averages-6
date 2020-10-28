# Method of moments estimator for Bernoulli random variables

In this exercise, we are going to use the method of moments that was discussed in the video to investigate how the method of moments estimator for the sample mean of a Bernoulli random variable changes as we calculate the estimator from different numbers of samples of random variables.  Recall that the probability mass function for a Bernoulli random variable is:

![](https://render.githubusercontent.com/render/math?math=P(X=0)=(1-p)\qquad\P(X=1)=p)

And that the expectation for this type of random variable is:

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)=p)

As discussed in the video the method of moments works by noting that the expectation for the statistic:

![](https://render.githubusercontent.com/render/math?math=\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i)

is the same as the expectation of the underlying random variables (the ![](https://render.githubusercontent.com/render/math?math=X_i) in this expression).  As we have seen in the previous exercises, however, the distribution from which the statistic above is "narrower" than the distribution that is sampled by the underlying random variables.  The estimate that we obtain when we compute this statistic is thus likely to "be close" to the true value of the expectation.  

We can thus use the estimate we get from this expression to estimate the parameter, p, of the underlying distribution using the expression that relates the expectation to the parameter of the distribution.  In this case as there is, in fact, no calculation to be done here as ![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)=p).  

__With that in mind, the aim is for you to write a code to investigate how the method of moments estimator for the parameter of a Bernoulli random variable depends on the number of samples that it is computed from.__  To complete the exercise you will need to

1. Finish the  function `bernoulli`. This function should take a single argument `p`. It should return a Bernoulli random variable from a distribution with parameter `p`. 
2. Set the first element of the list called `indices` equal to 1, the second element of the list called `indices` to 2 and so on.
3. Set the first element of the list called `estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 1 Bernoulli random variable with parameter `pval`, the second element of the list `estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 2 Bernoulli random variables with parameter `pval`, set the third element of the list called `estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 3 Bernoulli random variables with parameter `pval` and so on until you have computed an estimate of the parameter of the distribution from 200 Bernoulli random variables. 

When your code is complete a graph will be generated.  The red dots are the values of the method of moments estimator for the parameter of the distribution you sampled from.  The black dashed line is then the true value of the parameter.  You should see that the estimator converges to the true value of the parameter.
