# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:48:23.207490Z","iopub.execute_input":"2022-11-09T17:48:23.207884Z","iopub.status.idle":"2022-11-09T17:48:23.219422Z","shell.execute_reply.started":"2022-11-09T17:48:23.207851Z","shell.execute_reply":"2022-11-09T17:48:23.218277Z"}}
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np  # linear algebra
import matplotlib.pyplot as plt
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
from sklearn.metrics import classification_report, confusion_matrix

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
plt.rcParams["figure.figsize"] = (20, 8)


# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:51.403862Z","iopub.execute_input":"2022-11-09T17:22:51.404670Z","iopub.status.idle":"2022-11-09T17:22:52.184518Z","shell.execute_reply.started":"2022-11-09T17:22:51.404623Z","shell.execute_reply":"2022-11-09T17:22:52.183151Z"}}
zillow_prices = pd.read_csv("../input/zillow-prices/ZillowPrices.csv")
zillow_prices

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.186123Z","iopub.execute_input":"2022-11-09T17:22:52.186502Z","iopub.status.idle":"2022-11-09T17:22:52.194151Z","shell.execute_reply.started":"2022-11-09T17:22:52.186455Z","shell.execute_reply":"2022-11-09T17:22:52.192798Z"}}
zillow_prices = zillow_prices.loc[:, ['RegionName', 'StateName', 'CountyName', '12/31/21',
                                      '1/31/22', '2/28/22', '3/31/22', '4/30/22', '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']]

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.196623Z","iopub.execute_input":"2022-11-09T17:22:52.197065Z","iopub.status.idle":"2022-11-09T17:22:52.233178Z","shell.execute_reply.started":"2022-11-09T17:22:52.197030Z","shell.execute_reply":"2022-11-09T17:22:52.231887Z"}}
njHomes = zillow_prices[(zillow_prices.StateName == 'NJ')]
njHomes

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.234660Z","iopub.execute_input":"2022-11-09T17:22:52.234988Z","iopub.status.idle":"2022-11-09T17:22:52.242739Z","shell.execute_reply.started":"2022-11-09T17:22:52.234958Z","shell.execute_reply":"2022-11-09T17:22:52.241279Z"}}
paterson = njHomes[(njHomes.RegionName == 'Paterson')]

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.244626Z","iopub.execute_input":"2022-11-09T17:22:52.245159Z","iopub.status.idle":"2022-11-09T17:22:52.256521Z","shell.execute_reply.started":"2022-11-09T17:22:52.245113Z","shell.execute_reply":"2022-11-09T17:22:52.255299Z"}}
pricePaterson = paterson.loc[:, ['RegionName', '12/31/21', '1/31/22', '2/28/22',
                                 '3/31/22', '4/30/22', '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']]

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.258162Z","iopub.execute_input":"2022-11-09T17:22:52.258688Z","iopub.status.idle":"2022-11-09T17:22:52.266870Z","shell.execute_reply.started":"2022-11-09T17:22:52.258650Z","shell.execute_reply":"2022-11-09T17:22:52.265858Z"}}
months = ['12/31/21', '1/31/22', '2/28/22', '3/31/22', '4/30/22',
          '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.268120Z","iopub.execute_input":"2022-11-09T17:22:52.269050Z","iopub.status.idle":"2022-11-09T17:22:52.280140Z","shell.execute_reply.started":"2022-11-09T17:22:52.269014Z","shell.execute_reply":"2022-11-09T17:22:52.279071Z"}}
pricePaterson = pricePaterson.set_index('RegionName').T

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:27:00.501293Z","iopub.execute_input":"2022-11-09T17:27:00.501799Z","iopub.status.idle":"2022-11-09T17:27:00.510670Z","shell.execute_reply.started":"2022-11-09T17:27:00.501761Z","shell.execute_reply":"2022-11-09T17:27:00.509646Z"}}
pricePaterson['Paterson']

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.283636Z","iopub.execute_input":"2022-11-09T17:22:52.284013Z","iopub.status.idle":"2022-11-09T17:22:52.505038Z","shell.execute_reply.started":"2022-11-09T17:22:52.283979Z","shell.execute_reply":"2022-11-09T17:22:52.503843Z"}}
plt.plot(months, pricePaterson['Paterson'])
plt.show()

# %% [markdown]
# **Prediction of Prices in the city of Paterson**
#
# As seen in the graph above the curve in polynomial with a degree > 2. Thus we will perform polynomial regression.
#
# To ease the study we will change months from string to integer, following this translation:
#
# 0: 12/31/21
#
#
# 1: 1/31/21
#
#
# 2: 2/28/22
#
#
# 3: 3/31/22
#
#
# 4: 4/30/22
#
# 5: 5/31/22
#
# 6: 6/30/22
#
# 7: 7/31/22
#
# 8: 8/30/22
#
# 9: 9/31/22

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.506432Z","iopub.execute_input":"2022-11-09T17:22:52.506787Z","iopub.status.idle":"2022-11-09T17:22:52.511920Z","shell.execute_reply.started":"2022-11-09T17:22:52.506756Z","shell.execute_reply":"2022-11-09T17:22:52.511053Z"}}
monthsX = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
price = np.array(pricePaterson['Paterson'])

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.512799Z","iopub.execute_input":"2022-11-09T17:22:52.513113Z","iopub.status.idle":"2022-11-09T17:22:52.722558Z","shell.execute_reply.started":"2022-11-09T17:22:52.513083Z","shell.execute_reply":"2022-11-09T17:22:52.721309Z"}}
polynomial_features = PolynomialFeatures(degree=7)
months_poly = polynomial_features.fit_transform(monthsX)

model = LinearRegression()
model.fit(months_poly, price)
price_poly_pred = model.predict(months_poly)
rmse = np.sqrt(mean_squared_error(price, price_poly_pred))
r2 = r2_score(price, price_poly_pred)
print(rmse)
print(r2)
plt.scatter(monthsX, price)

plt.plot(monthsX, price_poly_pred, color='m')
plt.show()

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:22:52.723889Z","iopub.execute_input":"2022-11-09T17:22:52.724348Z","iopub.status.idle":"2022-11-09T17:22:52.732807Z","shell.execute_reply.started":"2022-11-09T17:22:52.724314Z","shell.execute_reply":"2022-11-09T17:22:52.731615Z"}}
equation = np.polyfit(
    np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), price_poly_pred, 7)
equation

# %% [markdown]
# price = 3.96120890e+05* m^7 + 1.31529674e+03* m^6 + 4.51290820e+03 * m^5 + -4.03308066e+03 * m^4 + 1.52222986e+03 * m^3 + -2.67599028e+02 * m^2 + 2.20923611e+01 * m + -6.97123016e-01

# %% [markdown]
# Figuring out how to automate this prediction
#

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:23:45.700755Z","iopub.execute_input":"2022-11-09T17:23:45.701152Z","iopub.status.idle":"2022-11-09T17:23:45.732608Z","shell.execute_reply.started":"2022-11-09T17:23:45.701119Z","shell.execute_reply":"2022-11-09T17:23:45.731532Z"}}
njHomes = njHomes.reset_index(drop=True).loc[:, ['RegionName', '12/31/21', '1/31/22',
                                                 '2/28/22', '3/31/22', '4/30/22', '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']]
njHomes.index = njHomes.index.set_names(["index"])
njHomes

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T17:54:11.209328Z","iopub.execute_input":"2022-11-09T17:54:11.209744Z","iopub.status.idle":"2022-11-09T17:54:11.217295Z","shell.execute_reply.started":"2022-11-09T17:54:11.209703Z","shell.execute_reply":"2022-11-09T17:54:11.216142Z"}}
len(njHomes)

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T18:23:29.259945Z","iopub.execute_input":"2022-11-09T18:23:29.261156Z","iopub.status.idle":"2022-11-09T18:26:08.258212Z","shell.execute_reply.started":"2022-11-09T18:23:29.261110Z","shell.execute_reply":"2022-11-09T18:26:08.256948Z"}}
months = ['12/31/21', '1/31/22', '2/28/22', '3/31/22', '4/30/22',
          '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']
monthsX = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
# Plot the first 5 cities in New Jersey
for i in range(len(njHomes)):
    city = njHomes[(njHomes.index == i)]
    priceCity = city.T
    cityName = priceCity[i][0]
    prices = priceCity[i][1:]
    plt.subplot(1, 2, 1)
    plt.plot(months, prices)
    plt.title("Original Price Plot of " + cityName)
    plt.xlabel('Months')
    plt.ylabel('Price in %')
    prices = np.array(prices)
    polynomial_features = PolynomialFeatures(degree=7)
    months_poly = polynomial_features.fit_transform(monthsX)

    model = LinearRegression()
    model.fit(months_poly, prices)
    price_poly_pred = model.predict(months_poly)
    rmse = np.sqrt(mean_squared_error(prices, price_poly_pred))
    r2 = r2_score(prices, price_poly_pred)
    plt.subplot(1, 2, 2)
    plt.scatter(monthsX, prices)
    plt.plot(monthsX, price_poly_pred, color='m')
    plt.title(cityName + ": Polynomial Regression of the Price Plot")
    plt.xlabel('Months')
    plt.ylabel('Price in %')
    plt.show()


# Find the average price in a home in New Jersey

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T18:10:18.248769Z","iopub.execute_input":"2022-11-09T18:10:18.249292Z","iopub.status.idle":"2022-11-09T18:10:18.262294Z","shell.execute_reply.started":"2022-11-09T18:10:18.249251Z","shell.execute_reply":"2022-11-09T18:10:18.261070Z"}}
# averageNJ = njHomes['12/31/21'].mean()
averagePriceNJ = []
months = ['12/31/21', '1/31/22', '2/28/22', '3/31/22', '4/30/22',
          '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']
for i in range(10):
    averagePriceNJ.append(njHomes[months[i]].mean())

averagePriceNJ

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T18:22:18.526498Z","iopub.execute_input":"2022-11-09T18:22:18.526903Z","iopub.status.idle":"2022-11-09T18:22:18.835372Z","shell.execute_reply.started":"2022-11-09T18:22:18.526870Z","shell.execute_reply":"2022-11-09T18:22:18.834185Z"}}
months = ['12/31/21', '1/31/22', '2/28/22', '3/31/22', '4/30/22',
          '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']
monthsX = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
# Plot the average price of houses in New Jersey
plt.subplot(1, 2, 1)
plt.plot(months, averagePriceNJ)
plt.title("Original Price Plot of New Jersey")
plt.xlabel('Months')
plt.ylabel('Price in %')
averagePriceNJNP = np.array(averagePriceNJ)
polynomial_features = PolynomialFeatures(degree=7)
months_poly = polynomial_features.fit_transform(monthsX)
model = LinearRegression()
model.fit(months_poly, averagePriceNJNP)
price_poly_pred = model.predict(months_poly)
rmse = np.sqrt(mean_squared_error(prices, price_poly_pred))
r2 = r2_score(averagePriceNJ, price_poly_pred)
plt.subplot(1, 2, 2)
plt.scatter(monthsX, averagePriceNJNP)
plt.plot(monthsX, price_poly_pred, color='m')
plt.title(": Polynomial Regression of the Price Plot")
plt.xlabel('Months')
plt.ylabel('Price in %')
plt.show()

# Analysis of Prices in New Jersey

print("The minimum average price in New Jersey is:", round(min(averagePriceNJNP)))
print("The maximum average price in New Jersey is: ",
      round(max(averagePriceNJNP)))
increase = round(
    ((max(averagePriceNJNP) - min(averagePriceNJNP))/min(averagePriceNJNP))*100, 2)
print("There was an jump in prices of %", increase)

# Find the prediction Equation
equation = np.polyfit(
    np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), price_poly_pred, 7)
equation

# %% [markdown]
# #  Do this analysis for the entire USA

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T18:40:58.623910Z","iopub.execute_input":"2022-11-09T18:40:58.624354Z","iopub.status.idle":"2022-11-09T18:40:58.631767Z","shell.execute_reply.started":"2022-11-09T18:40:58.624314Z","shell.execute_reply":"2022-11-09T18:40:58.630532Z"}}
states = ['AL',  'AK',  'AZ',  'AR',  'CA', 'CO',  'CT', 'DE',  'DC', 'FL',  'GA',  'HI',  'ID', 'IL',  'IN',  'IA', 'KS',  'KY',  'LA',  'ME', 'MD',  'MA', 'MI',  'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
          'OR',  'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',  'VA',  'WA', 'WV', 'WI', 'WY']

# %% [code] {"execution":{"iopub.status.busy":"2022-11-09T18:52:56.267747Z","iopub.execute_input":"2022-11-09T18:52:56.268185Z","iopub.status.idle":"2022-11-09T18:53:14.558710Z","shell.execute_reply.started":"2022-11-09T18:52:56.268147Z","shell.execute_reply":"2022-11-09T18:53:14.557578Z"}}
for state in states:
    stateHomes = zillow_prices[(zillow_prices.StateName == state)]
    # Find the average price of houses in each state
    averagePriceState = []
    months = ['12/31/21', '1/31/22', '2/28/22', '3/31/22', '4/30/22',
              '5/31/22', '6/30/22', '7/31/22', '8/31/22', '9/30/22']
    for i in range(10):
        averagePriceState.append(stateHomes[months[i]].mean())
    # Plot the average price of houses in New Jersey
    plt.subplot(1, 2, 1)
    plt.plot(months, averagePriceState)
    plt.title("Original Price Plot of " + state)
    plt.xlabel('Months')
    plt.ylabel('Price in %')
    averagePriceStateNP = np.array(averagePriceState)
    polynomial_features = PolynomialFeatures(degree=7)
    months_poly = polynomial_features.fit_transform(monthsX)
    model = LinearRegression()
    model.fit(months_poly, averagePriceStateNP)
    price_poly_pred = model.predict(months_poly)
    rmse = np.sqrt(mean_squared_error(prices, price_poly_pred))
    r2 = r2_score(averagePriceState, price_poly_pred)
    plt.subplot(1, 2, 2)
    plt.scatter(monthsX, averagePriceStateNP)
    plt.plot(monthsX, price_poly_pred, color='m')
    plt.title(state + ": Polynomial Regression of the Price Plot")
    plt.xlabel('Months')
    plt.ylabel('Price in %')
    plt.show()

    # Analysis of Prices in New Jersey

#     print("The minimum average price in New Jersey is:", round(min(averagePriceNJNP)))
#     print("The maximum average price in New Jersey is: ", round(max(averagePriceNJNP)))
#     increase = round(((max(averagePriceNJNP)- min(averagePriceNJNP))/min(averagePriceNJNP))*100, 2)
#     print("There was an jump in prices of %", increase)

#     # Find the prediction Equation
#     equation = np.polyfit(np.array([0,1,2,3,4,5,6,7,8,9]), price_poly_pred, 7)
#     equation

# %% [markdown]
# # Tasks :
#
# * Make JSON
#
# * Ask the user for budget and what month they want to move in, and suggest what states they can live in based on the predicted values
#

# %%
