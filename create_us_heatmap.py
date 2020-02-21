# REQUIRES python3

import plotly.express as px
import argparse

# ---------------------------------------------------------
# Set paths to input file
# ---------------------------------------------------------
parser = argparse.ArgumentParser(description="This program is used to plot the number of users per state.")
parser.add_argument("--infile", required=True, type=str, help="This argument holds the input file name" )

args = parser.parse_args()

input_file        = args.infile
input_file_object = open(input_file, "r")

# ---------------------------------------------------------

state_list_abbr = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

users_per_state = [0 for i in range(len(state_list_abbr))]

for line in input_file_object:
  
  # Split comma-delimited line into list
  line_list = line.split(",")

  if line_list[5] in state_list_abbr:
    users_per_state[state_list_abbr.index(line_list[5])] = users_per_state[state_list_abbr.index(line_list[5])] + 1
  else:
    print("State entry was not found! Exiting...\n")
    quit()
 
input_file_object.close()

print(users_per_state)
print(len(users_per_state))
print(len(state_list_abbr))

# Needed to change state_list_abbr to uppercase to use with plotly
fig = px.choropleth(locations=[u.upper() for u in state_list_abbr], locationmode="USA-states", color=users_per_state, scope="usa", color_continuous_scale=px.colors.diverging.Spectral)
fig.show() 
