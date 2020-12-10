# ML2020-p26 - models results
Kaggle Solar Power Generation Data projekt for Machine Learning 2020 in University of Tartu. 

## Results
Predicting **next day** power generation. Note that when you are comparing the prediction by day sum, you need to sum also the daily predictions first and calculate statistics based on that.

* RMSE day - one inverter daily power generation compared to actual 1 day power generation on test data.
* RMSE 15min - one inverter 15 minute power generation compared to actual 15 minute power generation.

Function to calculate the Daily and 15 min scores: [calculate_model_statistics.py](calculate_model_statistics.py)

### Plant 1
|Method|Link to Source|Comments-parameters|SCORE day (DC_POWER)|SCORE 15min (DC_POWER)|Status
|---------|------------|------|-----|---|---|
|Baseline - Plant 1|[link](/Analysis/01_running_mean.ipynb)|Last 3 days average for each inverter|RMSE:3079888.0; MAE:1823703.0; R2:-0.01559|RMSE:2572.0; MAE:1020.0; R2:0.4135|Completed
|Linear regression - Plant 1|[link](/Analysis/xyz.ipynb)|Important features (9): 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AMBIENT_TEMPERATURE_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3'|RMSE:259218.0; MAE:134616.0; R2:0.99281|RMSE:869.0; MAE:375.0; R2:0.93309|Completed
|Random Forest - Plant 1|[link](/Analysis/xyz.ipynb)|Initial attempt was using all feautures and using Grid Search CV to tune hyperparameters. After that used PCA and reduced number of components to only 4, while explaining 99% of variance.|RMSE 3607.6; MAE 2952.3; R2 -0.1538|RMSE 5222459.1; MAE 3624121.4; R2 -1.9201|Completed
|XGBRegressor - Plant 1|[link](/Analysis/02_XGBoost_v4_Plant1.ipynb)|Feature reduction from all to best RMSE on train data. Best features set: 'HOUR', 'MINUTE', 'DAY_OF_YEAR', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:4401179.0; MAE:3759344.0; R2:-1.0739|RMSE:3427.0; MAE:1793.0; R2:-0.04139|Completed

### Plant 2
|Method|Link to Source|Comments-parameters|SCORE day (DC_POWER)|SCORE 15min (DC_POWER)|Status
|---------|------------|------|-----|---|---|
|Baseline - Plant 2|[link](/Analysis/01_running_mean.ipynb)|Last 3 days average for each inverter|RMSE:99585.0; MAE:84365.0; R2:-2.83702|RMSE:222.0; MAE:116.0; R2:0.40737|Completed
|Linear regression - PLant 2|[link](/Analysis/xyz.ipynb)|Important features (13): 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_MOMENT_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_MOMENT_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:9604.0; MAE:8138.0; R2:0.96431|RMSE:125.0; MAE:62.0; R2:0.81206|Completed
|Random Forest - Plant 2|[link](/Analysis/xyz.ipynb)|Initial attempt was using all feautures and using Grid Search CV to tune hyperparameters. After that used PCA and reduced number of components to only 5, while explaining 99% of variance.|RMSE 94247.1; MAE 81524.6;R2 -2.4367|RMSE 206.5; MAE 110.1; R2 0.489 |Completed
|XGBRegressor - Plant 2|[link](/Analysis/02_XGBoost_v4_Plant2.ipynb)|Feature reduction from all to best RMSE on train data. Best features set: 'HOUR', 'DAY_OF_YEAR', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:96060.0; MAE:73384.0; R2:-2.57024|RMSE:193.0; MAE:102.0; R2:0.55495|Completed


#Days predicions on test data 
###3 day running mean - baseline - Plant 1
####Idx - Day of year - Actual - Prediction
0          162  0.000000e+00            0.000000e+00<br/>
1          163  0.000000e+00            0.000000e+00<br/>
2          164  0.000000e+00            0.000000e+00<br/>
3          165  7.593776e+06            0.000000e+00<br/>
4          166  6.350495e+06            2.531259e+06<br/>
5          167  6.055536e+06            4.648090e+06<br/>
6          168  5.572501e+06            6.666602e+06<br/>
7          169  5.317780e+06            5.992844e+06<br/>

###3 day running mean - baseline - Plant 2
####Idx - Day of year - Actual - Prediction
0          162  393589.770390           543879.961868<br/>
1          163  342752.854139           517316.908030<br/>
2          164  411233.862857           430123.237859<br/>
3          165  455305.790476           382525.495795<br/>
4          166  505911.451905           403097.502491<br/>
5          167  410998.909524           457483.701746<br/>
6          168  480810.068571           457405.383968<br/>
7          169  380211.240476           465906.810000<br/>

###Linear Plant 1
####Idx - Day of year - Actual - Prediction
0          162  0.000000e+00           -4.406840e+03<br/>
1          163  0.000000e+00           -4.406840e+03<br/>
2          164  0.000000e+00           -4.406840e+03<br/>
3          165  7.593776e+06            6.899085e+06<br/>
4          166  6.350495e+06            6.555351e+06<br/>
5          167  6.055536e+06            6.092921e+06<br/>
6          168  5.572501e+06            5.677704e+06<br/>
7          169  5.317780e+06            5.339350e+06<br/>

###Linear Plant 2
####Idx - Day of year - Actual - Prediction
0          162  393589.770390           413142.507395<br/>
1          163  342752.854139           352196.705814<br/>
2          164  411233.862857           413048.274258<br/>
3          165  455305.790476           462131.013047<br/>
4          166  505911.451905           501781.214514<br/>
5          167  410998.909524           420138.098862<br/>
6          168  480810.068571           476463.357922<br/>
7          169  380211.240476           390062.789857<br/>

###Random Forest Plant 1
####Idx - Day of year - Actual - Prediction
predictions here...

###Random Forest Plant 2
####Idx - Day of year - Actual - Prediction
predictions here...

###XGBRegressor Plant 1
####Idx - Day of year - Actual - Prediction
0          162  0.000000e+00            9.289014e+05<br/>
1          163  0.000000e+00            9.289014e+05<br/>
2          164  0.000000e+00            9.289014e+05<br/>
3          165  7.593776e+06            9.289014e+05<br/>
4          166  6.350495e+06            1.338629e+05<br/>
5          167  6.055536e+06            1.037796e+06<br/>
6          168  5.572501e+06            7.125511e+05<br/>
7          169  5.317780e+06            7.889261e+05<br/>

###XGBRegressor Plant 2
####Idx - Day of year - Actual - Prediction
0          162  393589.770390            546967.68750<br/>
1          163  342752.854139            500868.56250<br/>
2          164  411233.862857            414590.68750<br/>
3          165  455305.790476            409555.87500<br/>
4          166  505911.451905            508642.87500<br/>
5          167  410998.909524            523350.28125<br/>
6          168  480810.068571            495220.18750<br/>
7          169  380211.240476            486095.25000<br/>



