# ML2020-p26 - models results
Kaggle Solar Power Generation Data projekt for Machine Learning 2020 in University of Tartu. 

## Results
Predicting **next day** power generation. Note that when you are comparing the prediction by day sum, you need to sum also the daily predictions first and calculate statistics based on that.

* RMSE day - one inverter daily power generation compared to actual 1 day power generation on test data.
* RMSE 15min - one inverter 15 minute power generation compared to actual 15 minute power generation.

Function to calculate the Daily and 15 min scores: [calculate_model_statistics.py](/Analysis/calculate_model_statistics.py)
The function also reports R2, which is not a good model measure for our case. Do not hesitate about the negative or bad R2 score on Test data as we are having time series problem and R2 score is comparing against "Test set average" (our test set is pretty small and r2 can see the future).

### Plant 1
|Method|Link to Source|Comments-parameters|SCORE day (DC_POWER)|SCORE 15min (DC_POWER)|Status
|---------|------------|------|-----|---|---|
|Baseline - Plant 1|[link](/Analysis/01_running_mean.ipynb)|Last 3 days average for each inverter|RMSE:3079888.0; MAE:1823703.0; R2:-0.01559|RMSE:2572.0; MAE:1020.0; R2:0.4135|Completed
|Linear regression - Plant 1|[link](/Analysis/xyz.ipynb)|Important features (10): 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:1262887.0; MAE:1091779.0; R2:-1.6938|RMSE:1682.0; MAE:870.0; R2:0.78959|Completed
|Random Forest - Plant 1|[link](/Analysis/xyz.ipynb)|Initial attempt was using all feautures and using Grid Search CV to tune hyperparameters. After that used PCA and reduced number of components to only 4, while explaining 99% of variance.|RMSE 1568941.3; MAE 1444176.8; R2 -3.157|RMSE 1808.5; MAE 1027.; R2 0.756|Completed 
|XGBRegressor - Plant 1|[link](/Analysis/02_XGBoost_v4_Plant1.ipynb)|Feature reduction from all to best RMSE on train data. Best features set: 'HOUR', 'MINUTE', 'DAY_OF_YEAR', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:1320368.0; MAE:1214055.0; R2:-1.9446|RMSE:1609.0; MAE:844.0; R2:0.80759|Completed
|Support vector regression - Plant 1|[link](/Analysis/Support%20vector%20regression.ipynb)| |RMSE:1089902.0; MAE:698708.0; R2:-1.00637|RMSE:1768.0; MAE:894.0; R2:0.7676|Completed

### Plant 2
|Method|Link to Source|Comments-parameters|SCORE day (DC_POWER)|SCORE 15min (DC_POWER)|Status
|---------|------------|------|-----|---|---|
|Baseline - Plant 2|[link](/Analysis/01_running_mean.ipynb)|Last 3 days average for each inverter|RMSE:99585.0; MAE:84365.0; R2:-2.83702|RMSE:222.0; MAE:116.0; R2:0.40737|Completed
|Linear regression - PLant 2|[link](/Analysis/xyz.ipynb)|Important features (10): 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:89034.0; MAE:73172.0; R2:-2.06707|RMSE:186.0; MAE:111.0; R2:0.58398|Completed
|Random Forest - Plant 2|[link](/Analysis/xyz.ipynb)|Initial attempt was using all feautures and using Grid Search CV to tune hyperparameters. After that used PCA and reduced number of components to only 5, while explaining 99% of variance.|RMSE 94247.1; MAE 81524.6;R2 -2.4367|RMSE 206.5; MAE 110.1; R2 0.489 |Completed
|XGBRegressor - Plant 2|[link](/Analysis/02_XGBoost_v3_Plant2.ipynb)|Feature reduction from all to best RMSE on train data. Best features set: 'HOUR', 'DAY_OF_YEAR', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_1', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_1', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_2', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_2', 'IRRADIATION_PER_INVERTER_DAY_SHIFT_MINUS_2', 'DC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AC_POWER_PER_INVERTER_DAY_SHIFT_MINUS_3', 'AMBIENT_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3', 'MODULE_TEMPERATURE_PER_INVERTER_DAY_SHIFT_MINUS_3'|RMSE:96060.0; MAE:73384.0; R2:-2.57024|RMSE:193.0; MAE:102.0; R2:0.55495|Completed
|Support vector regression - Plant 2|[link](/Analysis/Support%20vector%20regression.ipynb)| |RMSE:82134.0; MAE:77719.0; R2:-1.61012|RMSE:230.0; MAE:111.0; R2:0.3689|Completed


# Days predicions on test data 
### 3 day running mean - baseline - Plant 1
#### Idx - Day of year - Actual - Prediction
0          162  5.784040e+06            7.193523e+06<br/>
1          163  5.045679e+06            6.829388e+06<br/>
2          164  5.222354e+06            6.021242e+06<br/>
3          165  7.593776e+06            5.350691e+06<br/>
4          166  6.350495e+06            5.953936e+06<br/>
5          167  6.055536e+06            6.388875e+06<br/>
6          168  5.572501e+06            6.666602e+06<br/>
7          169  5.317780e+06            5.992844e+06<br/>

### 3 day running mean - baseline - Plant 2
#### Idx - Day of year - Actual - Prediction
0          162  393589.770390           543879.961868<br/>
1          163  342752.854139           517316.908030<br/>
2          164  411233.862857           430123.237859<br/>
3          165  455305.790476           382525.495795<br/>
4          166  505911.451905           403097.502491<br/>
5          167  410998.909524           457483.701746<br/>
6          168  480810.068571           457405.383968<br/>
7          169  380211.240476           465906.810000<br/>

### Linear Plant 1
#### Idx - Day of year - Actual - Prediction
0          162  5.784040e+06            7.181942e+06<br/>
1          163  5.045679e+06            6.476474e+06<br/>
2          164  5.222354e+06            5.877386e+06<br/>
3          165  7.593776e+06            5.489943e+06<br/>
4          166  6.350495e+06            6.269846e+06<br/>
5          167  6.055536e+06            6.213408e+06<br/>
6          168  5.572501e+06            6.680883e+06<br/>
7          169  5.317780e+06            6.059745e+06<br/>

### Linear Plant 2
#### Idx - Day of year - Actual - Prediction
0          162  393589.770390           547289.878305<br/>
1          163  342752.854139           475413.596101<br/>
2          164  411233.862857           388800.203925<br/>
3          165  455305.790476           410535.787869<br/>
4          166  505911.451905           476915.730874<br/>
5          167  410998.909524           513485.802099<br/>
6          168  480810.068571           471319.237131<br/>
7          169  380211.240476           471052.421460<br/>

### Random Forest Plant 1
#### Idx - Day of year - Actual - Prediction
0          162    5.784040e+06          7.088507e+06<br/>
1          163    5.045679e+06          7.433907e+06<br/>
2          164    5.222354e+06          7.305881e+06<br/>
3          165    7.593776e+06          6.619427e+066<br/>
4          166    6.350495e+06          6.749476e+06<br/>
5          167    6.055536e+06          7.033310e+06<br/>
6          168    5.572501e+06          7.206046e+06<br/>
7          169    5.317780e+06          7.110322e+06<br/>


### Random Forest Plant 2
#### Idx - Day of year - Actual - Prediction
0          162    393589.770390       519517.559642<br/>
1          163    342752.854139       479125.969286<br/>
2          164    411233.862857       450419.196099<br/>
3          165    455305.790476       450667.489504<br/>
4          166    505911.451905       462197.870685<br/>
5          167    410998.909524       518962.580603<br/>
6          168    480810.068571       524179.728576<br/>
7          169    380211.240476       488056.642407<br/>

## XGBRegressor Plant 1
#### Idx - Day of year - Actual - Prediction
0          162  5.784040e+06               6876625.0<br/>
1          163  5.045679e+06               7018585.5<br/>
2          164  5.222354e+06               6835856.0<br/>
3          165  7.593776e+06               6171558.0<br/>
4          166  6.350495e+06               6579280.0<br/>
5          167  6.055536e+06               6719795.0<br/>
6          168  5.572501e+06               7084776.0<br/>
7          169  5.317780e+06               6523687.5<br/>

### XGBRegressor Plant 2
#### Idx - Day of year - Actual - Prediction
0          162  393589.770390            546967.68750<br/>
1          163  342752.854139            500868.56250<br/>
2          164  411233.862857            414590.68750<br/>
3          165  455305.790476            409555.87500<br/>
4          166  505911.451905            508642.87500<br/>
5          167  410998.909524            523350.28125<br/>
6          168  480810.068571            495220.18750<br/>
7          169  380211.240476            486095.25000<br/>

### Support vector regression Plant 1
#### Idx - Day of year - Actual - Prediction
0          162  5.784040e+06            6.624898e+06<br/>
1          163  5.045679e+06            5.297057e+06<br/>
2          164  5.222354e+06            4.620887e+06<br/>
3          165  7.593776e+06            4.782682e+06<br/>
4          166  6.350495e+06            6.954362e+06<br/>
5          167  6.055536e+06            5.815801e+06<br/>
6          168  5.572501e+06            5.545686e+06<br/>
7          169  5.317780e+06            5.103337e+06<br/>

### Support vector regression Plant 2
#### Idx - Day of year - Actual - Prediction
0          162  393589.770390            522478.498884<br/>
1          163  342752.854139            371238.23824<br/>
2          164  411233.862857            323315.544653<br/>
3          165  455305.790476            387870.884356<br/>
4          166  505911.451905            429416.391819<br/>
5          167  410998.909524            477121.087261<br/>
6          168  480810.068571            387649.399706<br/>
7          169  380211.240476            453458.638964<br/>

