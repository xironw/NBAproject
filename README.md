# NBAproject

-----------
### Structures
```
|-Licence

|-README.md

|-data_processing.py

|-analysis_main.py

|-visualization.py

|-machine_learning.py

|-NBAPlayerData.csv

|-datadownload.png
```

-----------
#### Libraries:
`pandas` `scikit-learn` `matplotlib`
`numpy` `altair` `os`

#### Installing:

* Open your terninal, `git clone https://github.com/xironw/NBAproject.git` to download

* To see the files inside, put `cd `NBAproject`, `ls`

#### Before starting:

environment: PyCharm for Python

### Data preprocessing:

-----------
We processed our data by filtering down the data into only our columns of interest.
For our analysis, the only columns that we required from this data set were the
age, player height, points, rebounds, assists, offensive rebound percentage,
usage percentage, true shooting percentage, assist percenatge, and season.

### Data visualization:

-----------
scatter plot for the players' height vs performance:

The plots produced will be stored in a html format in your current directory named and
By clicking and open the html files.

for the scatter plot, you can drag in and out for different plots in the website, where there

Box plots for the players' height vs performance:

The box plots produced will be stored in html format in your current directory
named age_statistics.html, which can be opened in browser.
The box plots are interactable as well, allowing users to zoom in or out and hover
over parts of the visualization to obtain more information on the plots.

### Creating Machine learning model

-----------
Linear Regression Model:

The liner regression model was used in order to predict a player's assists based on
their height, age, points, and rebounds. After prediction, the models intercept,
age coeffiecient, player height coefficient, points coefficient, and rebounds
coefficeint are printed out into the console.

Descision Tree Regression Model:
The decision tree regression model was used in order to predict a player's points based
on their usage percentage, offensive rebound percentage, true shooting percentage, and 
assist percentage.

### Data Depndencies

-----------
The dataset contains over two decades of data on each player who has been part of an NBA teams' roster. It captures demographic variables such as age, height, weight and place of birth, biographical details like the team played for, draft year and round. In addition, it has basic box score statistics such as games played, average number of points, rebounds, assists, etc.

[```Link to the NBA dataset```](https://www.kaggle.com/justinas/nba-players-data)

Download instruction:

Click on the link provided above, on the right top side of the website page, there is a download bottom. Click on it, a csv file will be downloaded and you can get access to the file. The picture below shows where the bottom is on the page.

<img src="https://github.com/xironw/NBAproject/blob/main/datadownload.png?raw=true" width="600" height="400">

