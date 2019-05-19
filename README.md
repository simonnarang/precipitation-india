## Goal: Calculate average monthly rainfall in selected districts

In order to determine the average rainfall for each district, the 52 districts were first geocoded and given bounding boxes according to the coordinates of their Northeastern and Southwestern points from Google. These 4 points are then averaged as the center of the region. Finally, the four closest readings to this center point from the Terrestrial Precipitation Gridded Monthly Time Series are averaged to create the average for each district in a given month and year.

### Global Assumptions
* A reading from the Terrestrial Precipitation Gridded Monthly Time Series does not necessarily need to lie within a district's area for that reading to contribute to a sound indication regarding that district's rainfall.
* Precipitation does not vary drastically in different areas of a district (that is, each district can be approximated to a point).

## Reference

* `precip_2017/district_precipitation.ipnyb`: Python code for prompt
* `precip_2017/district_avg_precips.csv`: output for prompt

