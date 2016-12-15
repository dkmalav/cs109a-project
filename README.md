# cs109a-project
Repo for CS109a project - Forecasting Economic Growth Using Business News Data

# Introduction
Business news sentiment can be conjectured to both reflect how the economy is doing, as well as influencing the spending of consumers and investors who read it. It is likely, therefore, there is predictive value in the sentiment that is contained in business news. This project will collect business news over a certain time span, perform sentiment analysis on it, and forecast economic growth (GDP). These forecasts are relevant for e.g. investors making investment decisions, or for policy makers who wish to meet a certain economic policy objective.

# Objective
Predict GDP (economic growth) from the sentiment that is contained inThe New York Times business news, perhaps supplemented with traditional economic indicators.

# Running the Python Notebook
1. Clone the repo
2. Unzip articles.sqlite.zip as articles.sqlite, this is a SQLite database containing daily articles from Jan 1988 to Oct, 2016
3. Open and run src/analysis.ipynb