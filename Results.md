# ML2020-p26 - models results
Kaggle Solar Power Generation Data projekt for Machine Learning 2020 in Univeristy of Tartu. 

## Results
Predicting **next day** power generation. Note that when you are comparing the prediction by day sum, you need to sum also the daily predictions first and calculate statistics based on that.

* RMSE day - one inverter daily power generation compared to actual 1 day power generation on test data.
* RMSE 15min - one inverter 15 minute power generation compared to actual 15 minute power generation.

Function to calculate the Daily and 15 min scores: [calculate_model_statistics.py](calculate_model_statistics.py)

### Plant 1
|Method|Link to Source|Comments-parameters|SCORE day (DC_POWER)|SCORE 15min (DC_POWER)|Status
|---------|------------|------|-----|---|---|
|Baseline - Plant 1|[link](/Analysis/01_running_mean.ipynb)|Last 3 days average for each inverter|RMSE:3079888.0; MAE:1823703.0; R2:-0.01559|RMSE:2572.0; MAE:1020.0; R2:0.4135|Completed
|Linear regression - Plant 1|[link](/Analysis/xyz.ipynb)|Important features (11): 'IRRADIATION', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'TOTAL_YIELD_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'AMBIENT_TEMPERATURE_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3'|RMSE:76791.0; MAE:61089.0; R2:0.99937|RMSE:396.0; MAE:128.0; R2:0.98607|Completed
|Random Forest - Plant 1|[link](/Analysis/xyz.ipynb)|Initial attempt was using all feautures and using Grid Search CV to tune hyperparameters. After that used PCA and reduced number of components to only 4, while explaining 99% of variance.|RMSE 3607.6; MAE 2952.3; R2 -0.1538|RMSE 5222459.1; MAE 3624121.4; R2 -1.9201|Completed
|XGBoost - Plant 1|[link](/Analysis/02_XGBoost_v4_Plant1.ipynb)|Feature reduction from all to best RMSE on train data. Best features set: 'HOUR', 'MINUTE', 'DAY_OF_YEAR', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:4401179.0; MAE:3759344.0; R2:-1.0739|RMSE:3427.0; MAE:1793.0; R2:-0.04139|Completed

### Plant 2
|Method|Link to Source|Comments-parameters|SCORE day (DC_POWER)|SCORE 15min (DC_POWER)|Status
|---------|------------|------|-----|---|---|
|Baseline - Plant 2|[link](/Analysis/01_running_mean.ipynb)|Last 3 days average for each inverter|RMSE:99585.0; MAE:84365.0; R2:-2.83702|RMSE:222.0; MAE:116.0; R2:0.40737|Completed
|Linear regression - PLant 2|[link](/Analysis/xyz.ipynb)|Important features (14): 'IRRADIATION', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:7639.0; MAE:6728.0; R2:0.97742|RMSE:107.0; MAE:45.0; R2:0.86375|Completed
|Random Forest - Plant 2|[link](/Analysis/xyz.ipynb)|Initial attempt was using all feautures and using Grid Search CV to tune hyperparameters. After that used PCA and reduced number of components to only 5, while explaining 99% of variance.|RMSE 94247.1; MAE 81524.6;R2 -2.4367|RMSE 206.5; MAE 110.1; R2 0.489 |Completed
|XGBoost - Plant 2|[link](/Analysis/02_XGBoost_v4_Plant2.ipynb)|Feature reduction from all to best RMSE on train data. Best features set: 'HOUR', 'DAY_OF_YEAR', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:96060.0; MAE:73384.0; R2:-2.57024|RMSE:193.0; MAE:102.0; R2:0.55495|Completed

