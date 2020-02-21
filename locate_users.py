import argparse
# ---------------------------------------------------------
# Set paths to input and output files and open them
# ---------------------------------------------------------
parser = argparse.ArgumentParser(description="This program is used to find users in target states.")
parser.add_argument("--infile", required=True, type=str, help="This argument holds the input file name")
parser.add_argument("--outfile", required=True, type=str, help="This argument holds the output file name")
parser.add_argument("--states", required=True, nargs='+', type=str, help="Enter a space-delimited list of states (all lowercase)")

args = parser.parse_args()

input_file = args.infile
input_file_object = open(input_file, "r")

output_file = args.outfile
output_file_object = open(output_file, "w")

# ---------------------------------------------------------
# Set target states
# ---------------------------------------------------------

target_state_list = args.states

# ---------------------------------------------------------
# Find user entries from states matching the target list
# ---------------------------------------------------------

# Read in user entries
for line in input_file_object:

  # Split comma-delimited line into list to check state
  line_list = line.split(",")
  if line_list[5] in target_state_list:
    output_file_object.write(line)

print("File " + output_file + " contains the users information from the following states: " + str(target_state_list))

# ---------------------------------------------------------
# Close input and output files 
# ---------------------------------------------------------
input_file_object.close()
output_file_object.close()
  
