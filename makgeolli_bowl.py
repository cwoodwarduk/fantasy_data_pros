import espn_api.football as ff
import pandas as pd
import os
from os.path import join, dirname
import dotenv as dot

dotenv_path = join(dirname(__file__), '.env')
dot.load_dotenv(dotenv_path)

league_id = int(os.environ.get("ESPN_LEAGUE_ID")) #your league_id
year = 2021
swid = '{'+os.environ.get("ESPN_SWID")+'}' #your swid
espn_s2 = os.environ.get("ESPN_S2") #your espn_s2
league = ff.League(league_id, year, espn_s2, swid)

# print(league.power_rankings(week=11))

# get a list of columns for our dataframe
df_columns = list(league.teams[0].__dict__.keys())

# remove roster from list of columns
df_columns.remove('roster')

print(df_columns)

league_2021 = [pd.DataFrame(league.teams[d].__dict__, columns=df_columns) for d in range(len(league.teams))]

# # append teams to dataframe
# for d in range(len(league.teams)):
#     team_df = pd.DataFrame(league.teams[d].__dict__, columns=df_columns)
#     league_2021 = league_2021.append(team_df)