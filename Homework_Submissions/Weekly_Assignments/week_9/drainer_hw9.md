## Dave Drainer
## HWRS 501
## 30 Oct 2023, Homework 9

1. Forecast Summary: I basically looked at the mean flow over the past several weeks and then tried to match it with the history of streamflow in the month of November from the past few years. I adjusted percentages based on what looked to fit the overall trend and history in the graphs that I plotted. I came up with 111 cfs for the 1-week forecast, and 101 cfs for the 2-week forecast, as it looks like Nov flow is pretty consistent, with a slight drop after the first part of the month.
2. Improvements to Script: I cut out a few lines of code and really used the linter to clean up the formatting. I was also more specific with some of the comments to make it easier to read. I also improved the historical plots and assigned each color a year to make it easier to distinguish the trend.
3. Description of Function(s): I created 3 functions to calculate min, max, and mean of a particular column of a dataframe. This made the code much easier to write and understand. Instead of attaching the mean/max/min methods to the end of resampling, I just put that part in the function and then created generic variables for the dataframe, column of interest, and period of sampling. I was able to cut out some of the code by doing this.
4. I had some trouble with the dates in the last plot that shows my forecast compared with the monthly average originally, and had to go back and grab my oringinal code. I ran into a little bit of trouble with the function(or so I think) as it returned a dataframe with the index being datetime, but the also included the site_no column along with the flow. I'm not sure why I got both of those columns, as I thought I should have just got the datetime index and flow column.

***
### These are my plots:
1. ![image info](./mon_avg_flow_2018-2023.png)
2. ![image info](./wkly_avg_flow_2018-2023.png)
3. ![image info](./oct_nov_wkly_flow_since2020.png)
4. ![image info](./oct_observed_flow_and_fcst.png)