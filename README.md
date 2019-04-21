# Basketball Prediction App

## Overview
I like the NBA so created an app that allows user to select dream team, applies regression model to predict win percentage, and shares some insights with user about salary cap constraints, recommended player swaps, etc.

Core app is found in /app. The runApp.py script can be run at the command line. There are three folders in the app.
app/data -> this has the player data, extracted from basketball-reference. 
app/models -> this as the linear regression model
app/functions -> code for processing data

### how to run
Enter player names as comma seperated values, plus a season. Players can only be selected from a single season. 
```
python3 runApp.py Kobe Bryant','Yao Ming','Dwyane Wade','LeBron James','Chris Paul' 2005
Expected output: "Predicted win percentage: 75.0%"
```

For 2017 data, we can also consider salary cap. Here is an example.
```
python3 runApp.py 'Stephen Curry','Dwyane Wade','LeBron James','Chris Paul','Nick Young' 2017
Expected output: "The total salary of your team is 94.588555M. That is higher than 80 percent of the salary cap so this team might be unrealistic... but this is just for fun! This dream team's Predicted win percentage: 81.3%"
```

You'll then be asked whether you would like to know your teams strengths and weaknesses. 
```
Would you like to know the strengths and weaknesses of your team? Respond 'yes' or 'no'! yes
Your weakest 3 areas are (in order): ['tov', 'orb%', 'dbpm']
Your strongest 3 areas are (in order): ['ast%', 'ast', 'age']
```

Next, you'll be asked whether you would like a recommended player to swap to improve your team. If using 2017 season, you'll also be prompted whether salary cap should be considered. and whether we should consider salary cap... this take ~30 seconds
```
Would you like me to make a recommendation on a player to add to your team? Respond 'yes' or 'no'! yes
Should we consider the salary cap in order to give a realistic player swap? Respond 'yes' or 'no'! yes

Expected output: "You should drop Dwyane Wade and add Giannis Antetokounmpo, he should help the team in 31 statistical categories."
```
Lastly, you'll be asked if you want your new predicted winning percentage with the player swap.
```
Do you want to know the new predicted win percentage with this swap? Respond 'yes' or 'no'! yes
Expected output: "Predicted win percentage: 82.3%"
```

### notes
- prediction models are really average to bad right now. C'est la vie.
- the functions have no error handling... so the players need to be spelled correctly and have played in the listed season, otherwise will error out.
- there is currently a bug with salary cap. If the salary is too high for the initial team in 2017, it may not be possible to swap a player that gets the team to below salary cap. This causes an error.
