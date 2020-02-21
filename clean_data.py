# REQUIRES python3
import argparse

# ---------------------------------------------------------
# Set paths to input and output files
# ---------------------------------------------------------
parser = argparse.ArgumentParser(description="This program is used to clean user data.")
parser.add_argument("--infile", required=True, type=str, help="This argument holds the input file name" )
parser.add_argument("--outfile", required=True, type=str, help="This argument holds the output file name" )

args = parser.parse_args()

input_file        = args.infile
input_file_object = open(input_file, "r")

output_file        = args.outfile
output_file_object = open(output_file, "w")

# ---------------------------------------------------------

state_list_abbr = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

state_list = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

# ---------------------------------------------------------
unique_users = list()

for line in input_file_object:

  # Split comma-delimited line into list
  line = line.split(",")

  # Strip trailing newline character from zip code
  line[6] = line[6].rstrip("\n")
  line[6] = line[6].rstrip("\r")

  # Change state to lowercase 
  line[5] = line[5].lower()

  while True:
    if(line[5] in state_list_abbr):
      break
    elif(line[5] in state_list):
      line[5] = state_list_abbr[state_list.index(line[5])]
      break
    elif(line[5] == 'delete'):
      print("Deleting entry.")
      break
    else:

      print("\n--------------------------------------------")
      print("State not found in either list!")
      print("Entry: " + line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "," + line[6] + "\n")

      response = 'n'
      while response != 'y':
        line[5] = input("Please change the value of state (or delete entry): ")
        print("You entered: " + line[5])
        response = input("Is this correct (y,n)? ")
        if response == 'y':
          break
        elif response == 'n':
          continue
        else:
          print("You must enter y or n. Please try again.\n")
          continue

  # Keep only unique lines in new list (needed to remove duplicates - even though not used afterward)
  if(line in unique_users):
    continue
  else:
    if line[5] == 'delete':
      continue
    else:  
      unique_users.append(line)
      output_file_object.write(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "," + line[6] + "\n")

# ---------------------------------------------------------

input_file_object.close()
output_file_object.close()
