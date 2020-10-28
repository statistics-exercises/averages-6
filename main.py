import matplotlib.pyplot as plt
import numpy as np

def bernoulli(p) :
  # Your code to generate the bernoulli random variable goes here.
  
pval = 0.3
ssum, indices, estimator = 0, np.zeros(200), np.zeros(200)
for i in range(200) : 
  # Add code to setup the numpy arrays called indices and average to generate the desired
  # plot here.
  
  
  
# This will plot the graph for the data.  You should not need to adjust this.
plt.plot( indices, estimator, 'ro' )
plt.plot( [0,200], [pval,pval], 'k--' )
plt.xlabel("Number of random variables")
plt.ylabel("Estimator")
plt.savefig("bernoulli_estimator.png")
