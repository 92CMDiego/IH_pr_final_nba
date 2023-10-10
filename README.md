# NBA | How the game is changing

##### 1. Motivation.

The NBA is the world's top professional basketball league and has seen significant changes in recent decades. The main goal of this exercise is to analyze the most important game-changing trends using data from the NBA API. We've collected data from the past 25 years and we've focused on these key insights:
- Impact of international players in the league.
- Shift towards more versatile players.
- Faster-paced gameplay.
- Growing importance of three-point shots in the game.

In addition, we have developed a model with the objective of predicting the NBA regular season MVP. This model incorporates the following components:
- Independent Variables: player statistics, both base and advanced, along with the ranking of each player's team within the league.
- Target Variable: the percentage of MVP votes received by each player.

##### 2. Sources.

- Main datasets. NBA API. (https://github.com/swar/nba_api).
- Shots locations (2003-2023). Github project. (https://github.com/DomSamangy/NBA_Shots_04_23).
- MVP votes csv's (1999-2023). Basketball reference. (https://www.basketball-reference.com/awards/awards_2023.html).

##### 3. Data gathering and analysis.

The 'nba_api.ipynb' file is used to retrieve data from the NBA API. Most of the datasets analyzed in the project are collected here. These datasets are saved as CSV files for later analysis.

In various subfolders ('advanced_stats,' 'rosters,' 'team_stats_fg'), we analyze datasets previously gathered.

Within the 'shot_charts' folder, you will find the code used for generating shot charts using matplotlib. Please note that the dataset containing the shot locations (seasons 2003-04 to 2022-23) is not uploaded due to its large size.

##### 4. Streamlit.

The 'streamlit' folder contains the code used for building a Streamlit application. This application allows us to select an NBA team and a season (from the period 2003-04 to 2022-23) and visualize the most common shot locations of the team (the five thousand most common shot locations).

Please note that the dataset containing shot locations (seasons 2003-04 to 2022-23) is not uploaded due to its large size.

##### 5. MVP prediction model.

The 'mvp' folder contains data related to MVP votes for the period spanning from 1999 to 2023.

In the 'model' folder, you'll find the code used to build the MVP prediction model. This model incorporates data from the 'mvp' folder (the share of MVP votes is used as the target variable). It also includes player statistics and their respective team rankings spanning the entire period (as the independent variables).

To develop the model, we employed a model pipeline, which allowed us to assess various models and their performance (Random Forest Regressor, Gradient Boosting Regressor, Support Vector Regressor, XGB Regressor). We selected the Random Forest Regressor as the best-performing model. Additionally, we conducted hyperparameter tuning to optimize the model's performance.

##### 6. Reporting.

The main insights are summarized in the presentation (pr_finpr_v2).