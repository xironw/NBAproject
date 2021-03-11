from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def linear_regression(data):
    """
    This function takes into a dataframe. Based on this dataframe, a linear
    regression machine learning model will be produced by using the players'
    age, height, average points per game and rebounds as features and assists
    as labels. then it will print out the intercept and coefficients of the
    linear regression relationship and some values related to the accuracy
    of the model.
    """
    # splitring the data to x(features) and y(labels)
    x = data.loc[:, ['age', 'player_height', 'pts', 'reb']]
    y = data['ast']

    # splitting the training(80%) and testing(20%) data
    x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.8, random_state=4, shuffle=True)

    # create and fit the linear regression model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # print out the linear regression relationship of the model we build.
    # print out the different coefficient values for different features.
    print('Intercept of the model:', model.intercept_)
    print('coefficient of age:', model.coef_[0])
    print("coefficient of players' height:", model.coef_[1])
    print("coefficient of average points per game:", model.coef_[2])
    print("coefficient of rebounds:", model.coef_[3])

    # evaluate the accuracy of our machine learning model
    # from model score(R squared) and mean square error.
    print('model score:', model.score(x, y))
    print('mean_squre_error', mean_squared_error(y, model.predict(x)))


def regression_tree(data):
    """
    This function take in a data frame as a parameter. Using the data
    frame for training, a Decision Tree Regressor model will be created
    by using a players usage percentage, offensive rebound percentage,
    true shooting percentage, and assist percentage in order to predict
    that players average points.
    The function will then print out the mean squared errors associated
    with the model in predicting points using the training features from
    the training set and the test features from the test set.
    :param data: Data frame of NBA player statistics
    """
    # Filtering data down to only desired rows and columns
    year_mask = data['season'] != '2019-20'
    data_clean = data.loc[year_mask, :]
    columns = ['usg_pct', 'oreb_pct', 'ts_pct', 'ast_pct']
    features = data_clean.loc[year_mask, columns]
    label = data_clean['pts']
    # Splitting the data set 70% training and 30% testing
    features_train, features_test, label_train, label_test = \
        train_test_split(features, label, test_size=0.3)
    # Training and predicting with the model
    model = DecisionTreeRegressor()
    model.fit(features_train, label_train)
    train_predictions = model.predict(features_train)
    test_predictions = model.predict(features_test)
    # Calculated mean squared error in prediction for training and test
    train_error = mean_squared_error(label_train, train_predictions)
    test_error = mean_squared_error(label_test, test_predictions)
    error = {
        'Training Error': round(train_error, 2),
        'Testing Error': round(test_error, 2)
        }
    """
    Print statement used to display the mean squared error of our model
    in predicting the target for the training and test sets.
    """
    print(error)