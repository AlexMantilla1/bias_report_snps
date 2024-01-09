
file_list=test.txt
to_be_replaced="Vds_--MXX-- - --MXX--_vdsat"
to_replace="Vds_--MXX-- - --MXX--_vdsat   "

ls core_files > $file_list

while read file; do 

    if [ -z file ]; then # Avoid empty spaces
        echo "Skipping for $file"
    else # For each MOS label clone the info to the output file
        # Reading for each device.
        echo "Cloning for $file"
        echo "{gsub(/$to_be_replaced/, \"$to_replace\"); print}"
        awk "{gsub(/$to_be_replaced/, \"$to_replace\"); print}" core_files/$file > core_files_new/$file
    fi 

done < $file_list