---
title: 'vayu: A python package for analyzing air quality data'
tags:
  - Python
  - air quality
  - data science
  - heatmap
authors:
  - name: Man Vinayaka
    affiliation: 1
affiliations:
 - name: Texas A&M University
   index: 1
date: 24 July 2019
bibliography: paper.bib
---

# Summary

As climate change continues to become an existential threat due to decades of careless pollution, understanding our air quality is a vital step in curbing this problem. Air quality data has numerous metrics as to what makes up the air around us. Wind speed is a basic atmospheric quantity caused by air transitioning from high to low pressure. Wind direction indicates the direction from which the wind started. It is measured in cardinal degrees referring to which direction the wind is blowing in relation to a compass. Nitrogen oxide is a result of combustion as nitric oxide combines with oxygen which forms nitric oxide and nitrogen dioxide. Nitrogen dioxide is a well-established health hazard and is a precursor for both smog and acid rain. Ozone or O¬3 is produced as the pollutants created by combustion react with sunlight creating a hazardous air pollutant. Carbon monoxide is the product of incomplete combustion most commonly through vehicles. Particle matter are minute solids and liquids in the air causing health complications if inhaled. Plots which analyze these metrics relay extensive information on sources and concentration of air pollution. 

The fourth leading cause of death globally is air pollution according to the World Bank & Institute for Health Metrics and Evaluation. Overtime, even small amounts of air pollution can lead to respiratory problems causing 5.5 million deaths a year. ``[air quality | environmental performance index]`` Furthermore, air pollution has an adverse effect on the environment. Air pollution leads to acid rain, eutrophication, ground level ozone, as well as haze. The economic impact is tremendous as well; air pollution costs the US spends an average of 225 billion dollars a year as well as an additional five trillion dollars per year due to productivity loss. ``[air quality | environmental performance index]`` The goal of this package is to be able to easily identify visually the high concentrations of air pollution metrics and locate the sources in any geographical location given the raw data. Finding the sources of air pollution and making plans to combat it can be done using these plots.

``openAir`` is extensive package in R that aims to do much the same by using a slew of different plots analyzing the important characteristics of air quality. To the best of our knowledge, there exists no complete air quality analysis toolkit for the python language without simply creating a wrapper around ``openAir`` to accomplish air pollution analysis in python. ``vayu`` solves this by creating similar plots in the python ecosystem. Python provides a more general approach to data science; ``vayu`` when used in conjunction with other python packages leads to a more easy and complete understanding of raw air quality data.

``vayu`` is an encompassing package that contains both simple and advanced plots for complete air quality analysis given raw air quality data. ``calendarPlot`` provides a heatmap on a calendar layout based on the intensity of the pollutant per day. Each day contains an arrow indicating both wind direction as well as wind speed. ``linearRelation``, when given two pollutants, will manipulate the raw data to find the average value every day as well as the average value of each month of every year. The plot will be a line plot of the slope of yearly data superimposed with a scatter plot of the monthly data. ``scatterPlot`` provides a much easier and useful way to see how two pollutants relate to each other as it with a smooth fit. ``selectByDate`` is a utility function that can cut large raw data into data by the year with average value for each day. ``summaryPlot`` shows important graphical summary of the raw data given. It graphs line plots and histograms for each pollutant as well as statistics such as mean, max, min, median, and the 95th percentile. ``timePlot`` plots a time series for wind speed, NOx, O3, and particle matter of size 1 and 2.5 micrometers. This plot allows for easy comparison between the pollutants given just raw data, a specific year, and month. ``timeProp`` graphs a stacked bar graph of all data in the data frame based on the frequency of wind direction in cardinal directions. It takes the average of every 3 days in each bar. The height of the bar is the value of the pollutant of that 3-day period. The bars are binned proportionally based on the overall value of the pollutant in that period. ``timeVariation`` graphs 4 separate plots. The first graphs the average pollutant level per day by each hour for each day of the week across all of the data. The second graphs the average pollutant level by each hour, across all data. The third graphs the average pollutant level by each month of the year for across data. The last graphs the average pollutant level per day of the week across all data. ``trendLevel`` graphs the overall pollutant trend for every year in the raw data given. It takes the average hour value of each month and plots a heatmap showing what times of the year there is a high concentration of the pollutant. And finally ``windRose`` plots a polar graph representing the frequency of counts by wind direction, wind speed, and pollutant level. 


# Examples

The following example is for the function ``timeVariation``. It will show the plot in relation to particle matter at the 1 micrometer size. The parameter, df represents a data frame that needs to be initialized before calling the function.
```python
df = pd.read_csv("mydata.csv")
timeVariation(df,'pm10')
```
![](timeVariation.png)

![](timeVariation_2.png)

Through this plot, it is clearly shown that the pm10 levels seems to peak around 8-10 am on all weekdays and goes down to lower levels on weekends. This tells the user that the source of pollution for this specific pollutant in this example should be investigated by checking what source of pollution around the geographic area tends to be more active in the weekdays than the weekend. This can lead to finding solutions to curb air pollution. 

---
The last example is of the function ``calendarPlot``. Through this plot, the user can easily see pollutant levels throughout any specified year as well as the speed and direction of the wind.
```python
df = pd.read_csv("mydata.csv")
calendarPlot(df,'pm25','2003')
```

![](calendarPlot.png)

Through this plot, the user can tell that there is significant pollution of particle matter of size 2.5 micrometers in March. On the darker days, the arrows indicate that there is a wind that points towards the north east direction. This may mean that there is some major source of pollution active in the south west region that is carrying over in a north east direction. With this information, the user can easily begin to identify locations and eventual causes of these greater than normal particle matter levels. 

# Acknowledgements 

``vayu`` is built mainly modeling after the ``openAir`` package in R (Carslaw, D.C. (2015)

# References



