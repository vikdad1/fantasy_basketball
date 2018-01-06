import os
import pickle
import pandas as pd
import sys
import cmd

path = os.getcwd() #get working directory
player_data = pd.read_csv(path + '/data/player_data.csv') #get data
player_list = ("Kobe Bryant","Lebron Jame","Yao Ming","Dwyane Wade","Chris Paul")
season = 2015

season_data = player_data[player_data['season'] == season]
message = ("Error Message:")
player = ("sd")
print(not player)
# season_data['player'].str.match(player_list,case = False).any():
# for player in player_list:
#     if season_data['player'].str.match(player,case = False).any():
#         message = message
#     else:
#         message = (message + " " + player)
#
# message = (message + " cannot be found in the dataset of the year.")
# print(message)