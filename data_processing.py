import pandas as pd


def cleandata(data_set):
    """
    This helper function takes in a data frame as a parameter and
    return back a version of the given data frame filtered down to
    only the desired columns.
    :param data_set: Data frame of NBA player statistics
    :return:
    """
    data = pd.read_csv(data_set)
    """
    Print statement used to show the first 8 rows of the dataframe
    prior to being filtered down to only the desired columns
    """
    print(data.head(8))
    columns = ['age', 'player_height', 'pts', 'reb', 'ast',
               'oreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season']
    data = data.loc[:, columns]
    """
    Print statement used to show the first 8 rows of the dataframe
    after being filtered down to only our columns of interest
    """
    print(data.head(8))
    return data