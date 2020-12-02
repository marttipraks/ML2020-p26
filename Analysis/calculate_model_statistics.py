from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
###Prints out RMSE, MAE for both individual measurements and also next day total measurements
# input:
# - test_data has to have column columns DAY_OF_YEAR and prediction column (DC_POWER)
# - column to be predicted (target)
# - predictions on the test data
def calculate_RMSE_MSE(test_data, predict_column, test_predictions):
    #INDIVIDUAL PERIODS PREDICTIONS
    RMSE_tm = np.sqrt(mean_squared_error(test_data[predict_column], test_predictions))
    MAE_tm = mean_absolute_error(test_data[predict_column], test_predictions)
    R2_tm = r2_score(test_data[predict_column], test_predictions) #uniform average
    #GROUPED BY DAY PREDICATIONS SCORES
    test_data['PREDICTED_DC_POWER'] = test_predictions
    grouped_test_data_target = test_data.groupby(['DAY_OF_YEAR'])[['DC_POWER', 'PREDICTED_DC_POWER']].agg({'sum'}).reset_index()
    grouped_test_data_target = grouped_test_data_target.set_axis(['DAY_OF_YEAR','DC_POWER_SUM','PREDICTED_DC_POWER_SUM'], axis = 1)
    print(grouped_test_data_target)

    RMSE_daily = np.sqrt(mean_squared_error(grouped_test_data_target['DC_POWER_SUM'], grouped_test_data_target['PREDICTED_DC_POWER_SUM']))
    MAE_daily = mean_absolute_error(grouped_test_data_target['DC_POWER_SUM'], grouped_test_data_target['PREDICTED_DC_POWER_SUM'])
    R2_daily = r2_score(grouped_test_data_target['DC_POWER_SUM'], grouped_test_data_target['PREDICTED_DC_POWER_SUM'])

    print('daily predictions:')
    print(f' RMSE:{np.round(RMSE_daily,0)}; MAE:{np.round(MAE_daily,0)}; R2:{np.round(R2_daily,5)}')

    print('individual measurements:')
    print(f' RMSE:{np.round(RMSE_tm,0)}; MAE:{np.round(MAE_tm,0)}; R2:{np.round(R2_tm,5)}')

