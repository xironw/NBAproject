import visualization
import machine_learning
import data_processing
import os
from data_processing import cleandata


def main():
    """
    Used to run all of the data processing, visualization generation,
    and machine learning
    """
    data_filtered = data_processing.cleandata('NBAPlayerData.csv')
    current_path = os.getcwd()
    data = cleandata(current_path + '/NBAPlayerData.csv')
    visualization.scatter_plot(data)
    visualization.boxplots(data_filtered)
    machine_learning.regression_tree(data_filtered)
    machine_learning.linear_regression(data)


if __name__ == '__main__':
    main()