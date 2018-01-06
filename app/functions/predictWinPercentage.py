import os
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

path = os.getcwd() #get working directory
model = pickle.load(open(path + '/models/top_5_players.sav', 'rb'))

def aggregatePlayerStats(data, player_list):

    team_data = data[data['player'].isin(player_list)] #subset data in the player list
    sum_data = team_data[['fga', '3pa', '2pa', 'fta',
                       'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']].sum()
    avg_data = team_data[['2p%', '3p%', 'fg%', 'ft%', 'efg%', 'age', 'per', '3par',
                         'ftr', 'orb%', 'drb%', 'trb%', 'ast%', 'stl%', 'blk%', 'tov%',
                         'usg%', 'ows', 'dws', 'ws', 'ws/48', 'obpm', 'dbpm', 'bpm', 'vorp']].mean()
    final = pd.DataFrame(pd.concat([sum_data, avg_data], axis=0)).transpose()
    return final

def predictWinPercentage(player_data, season_average_data, player_list, season):
    
    season_data = player_data[player_data['season']==season]
    season_average = season_average_data[season_average_data['season']==season]
    team_stats = aggregatePlayerStats(season_data, player_list)
    team_stats = team_stats - season_average.loc['mean'].drop('season', axis=0) #reflects model type
 
    winning_percentage = float(model.predict(team_stats)) *100
    winning_percentage = round(winning_percentage, 1)
    final = str(winning_percentage) + '%'
    return final