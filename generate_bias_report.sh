# Set the input and output file names.
input_file=$1

# Read the list .csv file name:
IFS="\""
list_csv_file=`cat backend/python/config.py | grep "LIST_FILE_NAME_DEFAULT = " | (read var1 var2; echo $var2)`

# Read the output .csv file name:
IFS="\""
output_file=`cat backend/python/config.py | grep "OUTPUT_FILE_NAME_DEFAULT = " | (read var1 var2; echo $var2)` 

# Show the file names to use:
echo " "
echo "Files to use: "
echo "1. Spectre netlist file to use: $input_file"
echo "2. The .csv file to use (with the device list): $list_csv_file"
echo "3. The .csv output file to write: $output_file"
echo " "

# Check if list_csv_file exists:
if [[ -e $list_csv_file ]]; then
    # If list_csv_file does exist, ask to overwrite:
    echo "File $list_csv_file already exists. (Could be manually edited)" 
    read -p "Do you want to overwrite the $list_csv_file file? [y/N]: " answer2 
    if [[ $answer2 == "Y" ]] || [[ $answer2 == "YES" ]] || [[ $answer2 == "y" ]] || [[ $answer2 == "yes" ]]; then
        python backend/python//get_devices_from_scs.py $input_file
    fi  
else
    # If list_csv_file doesn't exist, just create it.
    echo "$list_csv_file does not exist! it will be created..."  
    python backend/python/get_devices_from_scs.py $input_file
fi

echo " " 
# Create or overwrite the output_file (this one is not expecte to be manually edited):
echo "# MOS BIAS report created from list at '$list_csv_file'" > $output_file
echo "# Created automaticaly by $USER, running the 'generate_bias_report.sh' file (V2)" >> $output_file
echo "# Created on: $(date)" >>  $output_file
# Write all devices outputs:
python backend/python/write_all_devices.py $output_file

