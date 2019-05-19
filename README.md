## Goal: Calculate Average Monthly Rainfall in Selected Districts

In order to determine the average rainfall for each district, the 52 districts were first geocoded and given bounding boxes according to the coordinates of their Northeastern and Southwestern points from Google. These 4 points are then averaged as the center of the region. Finally, the four closest readings to this center point from the Terrestrial Precipitation Gridded Monthly Time Series are averaged to create the average for each district in a given month and year.

### Global Assumptions
* A reading from the Terrestrial Precipitation Gridded Monthly Time Series does not necessarily need to be within a district for that reading to contribute to a sound indication of that district's rainfall.
* Precipitation does not vary drastically in different areas of a district (that is, each district can be approximated to a point with relatively insignificant loss in accuracy).


* `precip_2017/district_precipitation.ipnyb`: Python code for prompt
* `precip_2017/district_avg_precips.csv`: output for prompt

