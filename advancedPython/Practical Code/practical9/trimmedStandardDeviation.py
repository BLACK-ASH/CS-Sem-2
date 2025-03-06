from scipy import stats 
import numpy as np  
   
# array elements ranging from 0 to 19 
x = np.arange(20) 
    
print("Trimmed Standard Deviation : ", stats.tstd(x))     
print("\nTrimmed Standard Deviation by setting limit : ", stats.tstd(x,(2,10)))