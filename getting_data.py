import requests
import pandas as pd
import numpy as np


index = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
index_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
conditions = [
    final_df['team'] == 1,
    final_df['team'] == 2,
    final_df['team'] == 3,
    final_df['team'] == 4,
    final_df['team'] == 5,
    final_df['team'] == 6,
    final_df['team'] == 7,
    final_df['team'] == 8,
    final_df['team'] == 9,
    final_df['team'] == 10,
    final_df['team'] == 11,
    final_df['team'] == 12,
    final_df['team'] == 13,
    final_df['team'] == 14,
    final_df['team'] == 15,
    final_df['team'] == 16,
    final_df['team'] == 17,
    final_df['team'] == 18,
    final_df['team'] == 19,
    final_df['team'] == 20,
]
values = [
    'ARS',
    'AVL',
    'BHA',
    'BUR',
    'CHE',
    'CRY',
    'EVE',
    'FUL',
    'LEI',
    'LEE',
    'LIV',
    'MCI',
    'MUN',
    'NEW',
    'SHU',
    'SOU',
    'TOT',
    'WBA',
    'WHU',
    'WOL',
]

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json = r.json()
json.keys()
# print(json.keys())
events_df = pd.DataFrame(json['events'])
# print(events_df.columns)

elements_df = pd.DataFrame(json['elements'])
elements_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])
# print(teams_df.columns)
# print(elements_df.columns)
team_list = []
team_list = teams_df[['short_name']]
# print(team_list)
# print(team_list['Index'])
# slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
slim_elements_df = elements_df[['id','first_name', 'second_name', 'element_type', 'points_per_game', 'transfers_in', 'selected_by_percent', 'team', 'transfers_out', 'goals_scored', 'assists', 'clean_sheets', 'ict_index', 'chance_of_playing_this_round', 'minutes', 'form', 'saves']]
sorted_by_form_elements_df = slim_elements_df.sort_values('form', ascending=False).head(20)
# for index, row in slim_elements_df.iterrows():
#     for x in team_list:   ITERATING THROUGH THE DF
#         if row['team'] - 1 == team_list['Index']
# sorted_by_ict_elements_df = slim_elements_df.sort_values('ict_index', ascending=False).head(20)
# sorted_by_points_per_game_elements_df = slim_elements_df.sort_values('points_per_game', ascending=False).head(20)
# sorted_by_minutes_elements_df = slim_elements_df.sort_values('minutes', ascending=False).head(20)
# sorted_by_transfer_in_elements_df = slim_elements_df.sort_values('transfers_in', ascending=False).head(20)
# # print(slim_elements_df.sort_values('form', ascending=False).head(20))
# sorted_by_form_elements_df.to_excel('E:/F.L.A.P backend/form_data.xlsx')
# sorted_by_transfer_in_elements_df.to_excel('E:/F.L.A.P backend/transfers_in_data.xlsx')
# sorted_by_minutes_elements_df.to_excel('E:/F.L.A.P backend/minutes_data.xlsx')
# sorted_by_ict_elements_df.to_excel('E:/F.L.A.P backend/ict_data.xlsx')
# sorted_by_points_per_game_elements_df.to_excel('E:/F.L.A.P backend/points_data.xlsx')

def sorting(df):
    df = df.sort_values('form', ascending=False)
    return df
def team_name(row):
    if row['team'] == 17:
        return "TOT"

gk_df = slim_elements_df.loc[slim_elements_df.element_type == 1]
# print(gk_df.loc[7])
# sorted_gk_df = gk_df.sort_values(['chance_of_playing_this_round', 'form', 'clean_sheets', 'transfers_in', 'saves'], ascending=[False, False, False, False, True])
# print(sorted_gk_df)
mid_df = slim_elements_df.loc[slim_elements_df.element_type == 3]
def_df = slim_elements_df.loc[slim_elements_df.element_type == 2]
att_df = slim_elements_df.loc[slim_elements_df.element_type == 4]

gk_df = sorting(gk_df)
# print(gk_df)
def_df = sorting(def_df)
mid_df = sorting(mid_df)
att_df = sorting(att_df)

final_df = gk_df.head(2)
final_df = final_df.append(def_df.head(5))
final_df = final_df.append(mid_df.head(5))
final_df = final_df.append(att_df.head(3))
# print(final_df.element_type)
test_df = final_df
test_df['Index'] = index
# print(test_df.set_index(test_df.Index))
final_df = test_df.set_index(test_df.Index)
# final_df['team_name'] = final_df.apply(team_name())


final_df['team_name'] = np.select(conditions, values) #elegant solution

# print(final_df[['first_name', 'second_name', 'team', 'team_name']])
# print(test_df)
# print(test_df.element_type)
# print(elements_df)



#
# print(gk_df)
# print(def_df)
# print(mid_df)
# print((att_df))

# print(gk_df.to_json())

#
# print(att_df.loc[5])
# sorted_att_df = att_df.sort_values(['form', 'points_per_game', 'selected_by_percent', 'transfers_in', 'goals_scored', 'assists', 'ict_index', 'clean_sheets'], ascending=[False, False, False, False, False, False, False, False])
# print(sorted_att_df)
# print(sorted_att_df.loc[551])
# print(sorted_att_df.loc[119])



# print(slim_elements_df.loc[slim_elements_df.element_type == 2])
