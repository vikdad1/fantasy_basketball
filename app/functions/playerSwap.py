import os
import pandas as pd

def aggregatePlayerStats(data, player_list):

    team_data = data[data['player'].isin(player_list)] #subset data in the player list
    sum_data = team_data[['fga', '3pa', '2pa', 'fta',
                       'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']].sum()
    avg_data = team_data[['2p%', '3p%', 'fg%', 'ft%', 'efg%', 'age', 'per', '3par',
                         'ftr', 'orb%', 'drb%', 'trb%', 'ast%', 'stl%', 'blk%', 'tov%',
                         'usg%', 'ows', 'dws', 'ws', 'ws/48', 'obpm', 'dbpm', 'bpm', 'vorp']].mean()
    final = pd.DataFrame(pd.concat([sum_data, avg_data], axis=0)).transpose()
    return final

def getZScores(player_list, player_data, season_average_data):
    
    #season_average_data must be for the season in question... subset before hand\
    team_stats = aggregatePlayerStats(player_data, player_list)
    
    z_scores = list()
    #get mean/standard deviation for stats of specific season
    season_data = season_average_data.drop('season', axis=1) 
    #find the columns that intersect between two data sets to iterate over
    columns = team_stats.columns[team_stats.columns.isin(season_average_data.columns)]
    
    for stat in columns:
        if stat not in ['tov', 'pf']: #if not turnovers or personal fouls
            # z = (X - X_bar) / SD
            z = (team_stats[stat][0] - season_data.loc['mean', stat])/season_data.loc['sd', stat]
        else:
            # z = -(X - X_bar) / SD
            z = -(team_stats[stat][0] - season_data.loc['mean', stat])/season_data.loc['sd', stat]
            
        z_scores.append(z)
    
    # Put it all together in a single DataFrame
    z_scores = pd.DataFrame(z_scores, columns = ['z_score'], index = columns)
    z_scores = z_scores.sort_values('z_score', ascending = True)
    return z_scores

def teamAssessment(data, bottom_n=3, top_n=3):
    
    strengths = list(data.tail(top_n).index)
    strengths.reverse() #reverse order
    weaknesses = list(data.head(bottom_n).index)
    
    results = {'weaknesses': "Your weakest {} areas are (in order): {}".format(str(bottom_n), str(weaknesses)),
            'strengths': "Your strongest {} areas are (in order): {}".format(str(top_n), str(strengths))}
    
    return(results)

def salaryCap(player_list, salary_data, max_percentage):
    
    cap_total = 94.14 #hard coding for 2016
    cap_starters = cap_total * (max_percentage/100)
    salary = (salary_data[salary_data['player'].isin(player_list)]['salary'].sum(axis=0))/1000000
    
    if salary > cap_starters:
        return {'total_salary': salary, 'starter_cap': cap_starters, 'over_cap': True}
    else:
        return {'total_salary': salary, 'starter_cap': cap_starters, 'over_cap': False}

def assessPlayerSwaps(player_list, player_data, season_average_data, salary_data, salary_cap):
    
    ###Issue: this returns nothing right now if there is no way to get under the salary cap given the players

    potential_swaps = pd.DataFrame() #empty data frame
     
    og_team_stats = aggregatePlayerStats(player_data, player_list) #get the average stats 
    og_z_score = getZScores(player_list, player_data, season_average_data) #get z-score for each team stat
    og_cum_z_score = og_z_score.sum()[0] #get cumulative z score
    
    for player_new in player_data['player']:
        for player_og in player_list: #could add check here for whether player input is already on team
            new_player_list = [player_new if x == player_og else x for x in player_list] #create new player list

            salary = salaryCap(new_player_list, salary_data, 80)

            if salary['over_cap'] == True:
                continue

            new_team_stats = aggregatePlayerStats(player_data, new_player_list) #find stats for new team
            new_z_score = getZScores(new_player_list, player_data, season_average_data) #find z scores for new team
            new_cum_z_score = new_z_score.sum()[0] #find cumulative z score for new team

            cum_z_score_net_change = new_cum_z_score - og_cum_z_score #find net change in z score
            per_stat_diff = new_z_score - og_z_score #find per stat difference 
            stats_improved_count = len(per_stat_diff[per_stat_diff['z_score'] > 0]) #how many stats improved
            
            #Assign variables
            new_team_stats['player_og'] = player_og 
            new_team_stats['player_new'] = player_new
            new_team_stats['cum_z_score_og'] = og_cum_z_score
            new_team_stats['cum_z_score_new'] = new_cum_z_score
            new_team_stats['cum_z_score_net_change'] = cum_z_score_net_change
            new_team_stats['stats_improved_count'] = stats_improved_count
            
            #Concatentate with final df
            potential_swaps = pd.concat([potential_swaps, new_team_stats], axis=0)
            
    return(potential_swaps) #return results of all potential swaps.

def recommendPlayer(player_list, player_swap_data, return_new_team_list=False):
    best_swap = player_swap_data[player_swap_data['cum_z_score_net_change'] ==
                                 max(player_swap_data['cum_z_score_net_change'])]
    
    if return_new_team_list == False:
    	final = "You should drop {} and add {}, he should help the team in {} statistical categories.".format(
        	best_swap['player_og'][0], best_swap['player_new'][0], best_swap['stats_improved_count'][0])
    else:
    	final = [best_swap['player_new'][0] if x == best_swap['player_og'][0] else x for x in player_list]
    
    return(final)