Dave Drainer <br>
17 Sep 2023 <br>
Homework Assignment 4 <br>

<h3> Assignment Question Answers <br>

<h4>

1. I calculated the mean flow for all of Sep to get an idea of what the average streamflow is for that month, which resulted in approx 123 cfs. I then broke out the most frequent values of all of the streamflow, which appeared to be less than 300 cfs for all months. Looking at just the data for the month of Sep, I calculated the max, min and median values for the subset of flow that is less than 300 cfs for the month of Sep. These values lined up with the trends of most recent observed streamflow, so I picked some values that were a happy medium for the next couple of weeks. Flow seems to fluctuate between 50-80 cfs and 110-130 cfs regardless of the presence of rainfall near Campe Verde.
   
2. The variable flow_data is a 2-D numpy array containing 12,677 rows in 4 columns. The data are 64-bit floating point numbers.

3. 



<h2> Summary of Forecast <br>

<h4> For this week's forecast, I looked at the total number of occurrences of specific streamflow. It appears that most often, streamflow in Septemeber is at or below 300 cfs. I then isolated the flow to show a histogram of everything less that 300 cfs. From that data, most often the flow is around 100-110 cfs. Based on the most recen obseved streamflow of 111 cfs and the trend of flow as low as 58 cfs and as high as 157 cfs, I'm going to go with a forecast of the mean streamflow for Sep, which is 123 cfs for week 1. To go a little lower, I'll go with a flow of 85 for week 2, as that's still within a range of most frequent streamflow values in Sep, between the 2nd and 3rd quartiles.