import pandas as pd, numpy as np
from pandas_datareader import wb
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from scipy import stats
import sklearn.metrics as metrics
from sklearn.metrics import mean_squared_error

data_gdp_ghg = pd.read_csv('data_gdp_ghg.csv')
countries = wb.get_countries()
income_level = countries[~countries['incomeLevel'].isin(['Aggregates', 'Not classified'])][['iso3c', 'incomeLevel']].rename(columns={"iso3c": "Code"})
data_regression = data_gdp_ghg.merge(income_level, how='outer', on=["Code"]).dropna()

def linear_regression():
    y = data_regression['CO2 Emissions per capita'].to_numpy()
    x = data_regression['GDP per capita'].to_numpy()
    x1 = sm.add_constant(x)
    model = sm.OLS(y, x1).fit()
    predictions = model.predict(x1)
    print_model = model.summary()
    print(print_model)
    lin_reg_mse = mean_squared_error(y, predictions)
    lin_reg_rmse = np.sqrt(mean_squared_error(y, predictions))
    print('')
    print('Mean Squared Error (for a linear regression is', lin_reg_mse)
    print('Root Mean Squared Error (for a linear regression is', lin_reg_rmse)
    return x, y

def plot_linear_regression():
    x, y = linear_regression()
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))
    plt.figure(figsize=(20, 20))
    plt.title("Linear Regression: Environmental Kuznets Curve", size=20)
    plt.scatter(x, y)
    plt.plot(x, mymodel, c="red")
    plt.xlabel('GDP per capita')
    plt.ylabel('CO2 emissions per capita')
    plt.savefig('linear_regression.png',  bbox_inches = 'tight', facecolor='white')
    plt.show()

def polynomial_regression():
    x, y = linear_regression()
    degree = 2
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly_features = poly.fit_transform(x.reshape(-1, 1))
    poly_reg_model = LinearRegression()
    poly_reg_model.fit(poly_features, y)
    y_predicted = poly_reg_model.predict(poly_features)
    poly_reg_mse = mean_squared_error(y, y_predicted)
    poly_reg_rmse = np.sqrt(mean_squared_error(y, y_predicted))
    coeff = poly_reg_model.coef_
    print('Mean Squared Error (for a polynomial regression of degree', degree,') is', poly_reg_mse)
    print('Root Mean Squared Error (for a polynomial regression of degree', degree,') is', poly_reg_rmse)
    print('Coefficient(s) (for a polynomial regression of degree', degree,') are', coeff)
    return y_predicted

def plot_polynomial_regression():
    x, y = linear_regression()
    y_predicted = polynomial_regression()
    plt.figure(figsize=(20, 20))
    plt.title("Polynomial Regression: Environmental Kuznets Curve", size=20)
    plt.scatter(x, y)
    plt.plot(x, y_predicted, c="red")
    plt.xlabel('GDP per capita')
    plt.ylabel('CO2 emissions per capita')
    plt.savefig('polynomial_regression.png',  bbox_inches = 'tight', facecolor='white')
    plt.show()

linear_regression()
plot_linear_regression()
polynomial_regression()
plot_polynomial_regression()