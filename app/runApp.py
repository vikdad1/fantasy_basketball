import os
import pickle
import pandas as pd
import sys
import cmd

#season = input("What NBA season would you like to select? Enter between 2001-2016. ")
#season = int(season)

#player_list = input("Enter 5 players from that season in a format like this... 'Kobe Bryant','Yao Ming'...")
#player_list = player_list.split(',')
#print(player_list)
player_list = sys.argv[1].split(',')
season = int(sys.argv[2])
# player_list = ("Kobe Bryant","Lebron Jame","Yao Ming","Dwyane Wade","Chris Paul")
# season = 2015

path = os.getcwd() #get working directory
player_data = pd.read_csv(path + '/data/player_data.csv') #get data
player_data_sr= pd.read_csv(path + '/data/player_data_single_record.csv')
season_average_data = pd.read_csv(path + '/data/season_average_data.csv', index_col=0)
salary_data = pd.read_csv(path + '/data/salaries_2017.csv')

pd_sr = player_data_sr[player_data_sr['season']==season]
sa_data = season_average_data[season_average_data['season']==season]

import functions.predictWinPercentage as predictWinPercentage #import function
import functions.playerSwap as playerSwap

#Get prediction
prediction = predictWinPercentage.predictWinPercentage(player_data_sr, season_average_data, player_list, season)

#A note on salary cap
if season == 2017:
	salary_result = playerSwap.salaryCap(player_list, salary_data, .8)

	if salary_result['over_cap'] == True:
		comment = 'The total salary of your team is ' + str(salary_result['total_salary']) + 'M. That is higher than 80 percent of the salary cap' + \
		' so this team might be unrealistic... but this is just for fun! This dream team\'s ' + prediction
		print(comment)
	else:
		print(prediction)
else:
	print(prediction)

#Ask the user if more information about team is desired
response = input("Would you like to know the strengths and weaknesses of your team? Respond 'yes' or 'no'! ")

if response == 'yes':
	z_score = playerSwap.getZScores(player_list, pd_sr, sa_data)
	result = playerSwap.teamAssessment(z_score)
	print(result['weaknesses'])
	print(result['strengths'])

response = input("Would you like me to make a recommendation on a player to add to your team? Respond 'yes' or 'no'! ")

if response == 'yes' and season == 2017:
	response2 = input("Should we consider the salary cap in order to give a realistic player swap? Respond 'yes' or 'no'! ")

	if response2 == 'yes':
		potential_swaps = playerSwap.assessPlayerSwaps(player_list, pd_sr, sa_data, salary_data, True)
		result = playerSwap.recommendPlayer(player_list, potential_swaps)
	else:
		potential_swaps = playerSwap.assessPlayerSwaps(player_list, pd_sr, sa_data, salary_data, False)
		result = playerSwap.recommendPlayer(player_list, potential_swaps)

	print(result)

	response3 = input("Do you want to know the new predicted win percentage with this swap? Respond 'yes' or 'no'! ")
	
	if response3 == 'yes':
		new_player_list = playerSwap.recommendPlayer(player_list, potential_swaps, return_new_team_list=True)
		prediction = predictWinPercentage.predictWinPercentage(pd_sr, sa_data, new_player_list, season)
		print(prediction)

elif response == 'yes':
	potential_swaps = playerSwap.assessPlayerSwaps(player_list, pd_sr, sa_data, salary_data, True)
	result = playerSwap.recommendPlayer(player_list, potential_swaps)

	print(result)
	response3 = input("Do you want to know the new predicted win percentage with this swap? Respond 'yes' or 'no'! ")
	
	if response3 == 'yes':
		new_player_list = playerSwap.recommendPlayer(player_list, potential_swaps, return_new_team_list=True)
		prediction = predictWinPercentage.predictWinPercentage(pd_sr, sa_data, new_player_list, season)
		print(prediction)

if response == 'no':
	print('Sounds good, peace out!')
	exit()