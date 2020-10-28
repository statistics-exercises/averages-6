import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "you have plotted the wrong number of data points" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates in your plot are incorrect" )
            bar = np.sqrt(pval*(1-pval)/(i+1))*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( this_y[i] - pval )<bar, "it looks like you are sampling from the wrong statistical distribution" )
    
