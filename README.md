# ML2020-p26
Kaggle Solar Power Generation Data projekt for Machine Learning 2020 in Univeristy of Tartu. 

## Results
Add your model jupyter notebook references and results to [Results.md](Results.md).

## New features created:
General naming logic is {production field}_{description of statistic}_{period}. Following fields were created:

{production fields} = AC_POWER, DC_POWER, DAILY_YIELD. TOTAL_YIELD
* {production field}_PER_INVERTER_MOMENT_SHIFT_MINUS_1 - that inverter production info 15 minutes ago
* {production field}_PER_INVERTER_MOMENT_SHIFT_MINUS_2 - that inverter production info 30 minutes ago
* {production field}_PER_INVERTER_MOMENT_SHIFT_MINUS_3 - that inverter production info 45 minutes ago
* {production field}_PER_INVERTER_DAY_SHIFT_MINUS_1 - that inverter production info 1 day ago
* {production field}_PER_INVERTER_DAY_SHIFT_MINUS_2 - that inverter production info 2 days ago
* {production field}_PER_INVERTER_DAY_SHIFT_MINUS_3 - that inverter production info 3 days ago
* {weather measurement}_PER_INVERTER_MOMENT_SHIFT_MINUS_1 - weather info 15 minutes ago
* {weather measurement}_PER_INVERTER_MOMENT_SHIFT_MINUS_2 - weather info 30 minutes ago
* {weather measurement}_PER_INVERTER_MOMENT_SHIFT_MINUS_3 - weather info 45 minutes ago
* {weather measurement}_PER_INVERTER_DAY_SHIFT_MINUS_1 - weather info 1 day ago
* {weather measurement}_PER_INVERTER_DAY_SHIFT_MINUS_2 - weather info 2 days ago
* {weather measurement}_PER_INVERTER_DAY_SHIFT_MINUS_3 - weather info 3 days ago
* DC_POWER_DIF_AVG_PER_ALL - that inverter DC production compared with average of all inverters per whole period
* AC_POWER_DIF_AVG_PER_ALL - that inverter DC production compared with average of all inverters per whole period
* DC_DIF_AVG_PER_INVERTER_WHOLE_PERIOD - that inverter DC production compared with average of that inverter per whole period
* AC_DIF_AVG_PER_INVERTER_WHOLE_PERIOD - that inverter AC production compared with average of that inverter per whole period
* DC_DIF_AVG_PER_INVERTER_PER_DAY - that inverter DC production compared with average of that inverter per whole day
* AC_DIF_AVG_PER_INVERTER_PER_DAY - that inverter AC production compared with average of that inverter per whole day
* DC_AVG_DIF_PER_DAY - that inverter DC production compared with average of all inverters per whole day
* AC_AVG_DIF_PER_DAY - that inverter AC production compared with average of all inverters per whole day
* DC_DIF_AVG_PER_MOMENT - that inverter DC production compared with average of all inverters per that time moment
* AC_DIF_AVG_PER_MOMENT - that inverter AC production compared with average of all inverters per that time moment

* TODO Add to previous two new features like that day up to that moment, per that week upto that moment and total upto that moment???
* TODO Add production averages per week??


