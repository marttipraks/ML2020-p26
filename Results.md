# ML2020-p26 - models results
Kaggle Solar Power Generation Data projekt for Machine Learning 2020 in Univeristy of Tartu. 

###Results
Predicting **next day** power generation. Note that when you are comparing the prediction by day sum, you need to sum also the daily predictions first and calculate statistics based on that.

* RMSE day - one inverter daily power generation compared to actual 1 day power generation on test data.
* RMSE 15min - one inverter 15 minute power generation compared to actual 15 minute power generation.

Function to calculate the Daily and 15 min scores: [calculate_model_statistics.py](calculate_model_statistics.py)

|Method|Link to Source|Comments-parameters|SCORE day (DC_POWER)|SCORE 15min (DC_POWER)|Status
|---------|------------|------|-----|---|---|
|Baseline|[link](/Analysis/01_running_mean.ipynb)|Last 3 days average|TBD|TBD|Under work
|Linear regression|[link](/Analysis/xyz.ipynb)|TBD|TBD|TBD|Under work
|Logistic regression|[link](/Analysis/xyz.ipynb)|TBD|TBD|TBD|Under work
|Random Forest|[link](/Analysis/xyz.ipynb)|TBD|TBD|TBD|Under work
|XGBoost - Plant 1|[link](/Analysis/02_XGBoost_v3.ipynb)|'HOUR', 'MINUTE', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_3'|12703150638905 - RMSE; MSE - 3018756|RMSE - 8784919; MSE - 1532|Completed
|XGBoost - Plant 2|[link](/Analysis/02_XGBoost_v3.ipynb)|'HOUR', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1'|6397038876 - RMSE; MSE - 65853|RMSE - 34900; MSE - 94|Completed


