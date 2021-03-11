import altair as alt
import os


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
                                   " per game").mark_point().encode(
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


def boxplots(data):
    """
    This function takes in a data frame as a parameter. Based on the data
    in the dataframe, four box plots will be generated. The box plots will
    compare a basketball players age to points, rebounds, assists, and usage
    percentage. The plot is then finally saved as 'age_statistics.html' in
    the file directory.
    :param data: Data frame of NBA player statistics
    """
    age_range = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    age_mask_lower = data['age'] >= 21
    age_mask_upper = data['age'] <= 31
    columns_interest = ['age', 'pts', 'reb', 'ast', 'usg_pct']
    data_clean = data.loc[age_mask_lower & age_mask_upper, columns_interest]
    # Generate box plot of Age vs Points
    age_vs_points = alt.Chart(
        data_clean
    ).mark_boxplot(size=50, extent=2).encode(
        alt.X('age', title='Age', axis=alt.Axis(values=age_range),
              scale=alt.Scale(domain=(20, 32))),
        y=alt.Y('pts', title='Points'),
        color=alt.Color('age', scale=alt.Scale(scheme='accent'), legend=None)
    ).properties(width=850, title='Age VS Points')
    # Generate box plot of Age vs Rebounds
    age_vs_rebounds = alt.Chart(
        data_clean
    ).mark_boxplot(size=50, extent=2.5).encode(
        alt.X('age', title='Age', axis=alt.Axis(values=age_range),
              scale=alt.Scale(domain=(20, 32))),
        y=alt.Y('reb', title='Rebounds'),
        color=alt.Color('age', scale=alt.Scale(scheme='accent'), legend=None)
    ).properties(width=850, title='Age VS Rebounds')
    # Generate box plot of Age vs Assists
    age_vs_ast = alt.Chart(data_clean).mark_boxplot(size=50, extent=3).encode(
        alt.X('age', title='Age', axis=alt.Axis(values=age_range),
              scale=alt.Scale(domain=(20, 32))),
        y=alt.Y('ast', title='Assists'),
        color=alt.Color('age', scale=alt.Scale(scheme='accent'), legend=None)
    ).properties(width=850, title='Age VS Assists')
    # Generate box plot of Age vs Usage Percentage
    age_vs_usg = alt.Chart(data_clean).mark_boxplot(size=50, extent=2).encode(
        alt.X('age', title='Age', axis=alt.Axis(values=age_range),
              scale=alt.Scale(domain=(20, 32))),
        y=alt.Y('usg_pct', title='Usage Percentage'),
        color=alt.Color('age', scale=alt.Scale(scheme='accent'), legend=None)
    ).properties(width=850, title='Age VS Usage Percentage')
    # create the interaction (zoom in and out) function for the plots
    selection = alt.selection_interval(bind='scales')
    # Compound the charts with one another and save the chart
    charts = alt.vconcat(
        age_vs_points, age_vs_rebounds,
        age_vs_ast, age_vs_usg,
        title="Players'" + " Age vs Different Performances",
        padding=100, spacing=80).configure_mark(
        opacity=0.5, color='red').add_selection(
        selection
    ).configure_title(
        align='right', fontSize=23
    ).configure_axis(
        titleFontSize=20
    )
    charts.save('age_statistics.html')
