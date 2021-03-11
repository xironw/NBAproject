# import the packages
import os
from data_processing import cleandata
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


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
    # from model score(R sauqred) and mean square error.
    print('model score:', model.score(x, y))
    print('mean_squre_error', mean_squared_error(y, model.predict(x)))


def main():
    current_path = os.getcwd()
    data = cleandata(current_path + '/NBAPlayerData.csv')
    linear_regression(data)


if __name__ == "__main__":
    main()
