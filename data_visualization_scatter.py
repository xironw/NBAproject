# import the packages
import altair as alt
import os
from data_processing import cleandata


def scatter_plot(data):
    """
    This function takes into a dataframe. Based on this dataframe, it will
    plot 4 scatter plots for the players' height vs average points per game,
    , players' height vs rebounds, players' height vs assists and players'
    height vs usage percentage. The plot is then saved as a file named
    scatterchart.html in the current directory.
    """
    # create the first scatter plot for players' height vs
    # average points per game.
    chart1 = alt.Chart(data, title="Players' height vs average points" +
                                   "per game").mark_point().encode(
                                    alt.X('player_height',
                                          scale=alt.Scale(domain=(150, 240))
                                          ), y='pts'
                        ).properties(width=450, height=350)

    # create the second scatter plot for players' height vs rebounds
    chart2 = alt.Chart(data, title="Players' height vs rebounds"
                       ).mark_point().encode(
                        alt.X('player_height',
                              scale=alt.Scale(domain=(150, 240)),
                              ), y='reb').properties(width=450,
                                                     height=350)

    # create the third scatter plot for players' height vs assists.
    # height vs usage percentage.
    chart3 = alt.Chart(data, title='player height vs assists'
                       ).mark_point().encode(
                        alt.X('player_height',
                              scale=alt.Scale(domain=(150, 240)),
                              ), y='ast').properties(width=450,
                                                     height=350)

    # create the fourth scatter plot for players' height vs usage percentage.
    chart4 = alt.Chart(data, title="Players' height vs usage percentage"
                       ).mark_point().encode(
                        alt.X('player_height',
                              scale=alt.Scale(domain=(150, 240)),
                              ), y='usg_pct').properties(width=450, height=350)

    # create the interaction (zoom in and out) function for the plots
    selection = alt.selection_interval(bind='scales')

    # create the compound charts
    chart = alt.vconcat(chart1, chart2, chart3, chart4, title="Players'" +
                        " Height vs Different Performances",
                        padding=100, spacing=80).configure_mark(
                        opacity=0.5, color='pink').add_selection(
                        selection
                        ).configure_title(align='right', fontSize=23
                                          ).configure_axis(
                        titleFontSize=20)

    # saving and output the compound scatter charts.
    path = os.getcwd()
    chart.save(path + '/scatterchart.html')


def main():
    current_path = os.getcwd()
    data = cleandata(current_path + '/NBAPlayerData.csv')
    scatter_plot(data)


if __name__ == "__main__":
    main()
