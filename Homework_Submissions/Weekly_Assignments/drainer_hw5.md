## Dave Drainer
## HWRS 501
## 26 Sep 2023, Homework 5

### Forecast Summary
   
- My forecast this week is going off of an average of the last two week's observed data. I am still clueless on how to forecast streamflow, but based on the max, median, and mean of the last two and four weeks, I elected to go with something a little closer to the mean, maybe a little lower. No rain is still expected near the site for the  next several days. The average for the last two weeks was about 84 cfs, and 87 for the last four weeks. Max values were 111 and 157 for those same time periods, respectively. I think it's safer to go with something close to the mean, but a little lower due to the absence of any new precipitation. We'll go with 80 for the first week, and 85 for the two week forecasts.
    
  ### Homework Exercise Answers
   1. The new array that I created "flow_5year" has dimensions of 1826 rows and 4 columns.
   2. The average flow in this 5 year period is 325.1862541073384 cfs.
   3. There are 2 dimensions in the flow_5year array with 1826 rows and 4 columns.
   4. The total daily flow for this 5-year period is:  51303464640.0 cubic feet (cf), or ~ 5.13 x 10^10 cf.
   5. The first 5 flow values are 19,353,600, 19,008,000, 18,748,800, 18,316,800, 18,316,800 cf.
   6. The first 5 rows of my final 60-row array are:
      1.  [[2.01500000e+03 1.00000000e+00 3.03451613e+02]
      2.  [2.01600000e+03 2.00000000e+00 4.29500000e+02]
      3.  [2.01700000e+03 3.00000000e+00 1.41806452e+03]
      4.  [2.01800000e+03 4.00000000e+00 9.86966667e+01]
      5.  [2.01900000e+03 5.00000000e+00 1.21548387e+02]]



### Reflection
- I'm having a hard time breaking down what I'm trying to do when taking out pieces of an array. I understand taht I first need to check data against something that I want, but then it's hard to take that result and make something new from it. I'm also having a hard time telling the difference between the dimensions of an array. If I have 4 columns and 4 rows, does that mean I have 16 dimensions? or 4 dimensions? Functions within functions are confusing. The best way I learn is making a much smaller array and then trying things to visualize what's going on. That's the key for me--visualizing what's happening. This was really important with the last part of the question with creating the array with 60 rows using np.tile with np.arange nested inside of it. I finally created a 60-row array, but the numbering was very inconsistent. I have an average for each month of each year, but they are not in the right order and everything is in scientific notation.

### Python Script
- My script is located here: Homework Submissions>>Weekly Assignments\drainer_HW5.py