#!/bin/bash

output_name=$3
filename=$2
python_base_version=$1

output_directory=`~/ve/bin/python testing_ground/test-case-creator.py $filename $output_name`

~/ve$python_base_version/bin/python $output_name 1> /dev/null
echo $output_directory

# Set the base directory
current_dir=`pwd`
filename_base=$(basename "$filename")
filename_without_ext="${filename_base%.*}"
csv_file="$current_dir/$filename_without_ext.csv"

echo python version,line_number,status,error message > "$csv_file"

counter=0
for dir in "$output_directory"/*/; do
    dir_name=$(basename "$dir")
    cd $dir
    for i in {5..13}; do
        tmpFile=$(mktemp)
        ~/ve$i/bin/python test_case.py 2> $tmpFile 1> /dev/null
        err=$(cat $tmpFile)
        rm $tmpFile
        counter=$((counter + 1))
        status="0"
        error_message=""
        if [ ! -z "$err" ]; then
            status="-2"
            if [[ "$err" == *"invalid syntax"* ]]; then
                error_message="invalid synt7ax"
            elif [[ "$err" == *"results are diffrent"* ]]; then
                error_message="results are diffrent"
            elif [[ "$err" == *"has no attribute"* ]]; then
                error_message="has not the attribute"
            elif [[ "$err" == *"Error"* ]]; then
                error_message="unknown Error"
            elif [[ "$err" == *"DeprecationWarning"* ]]; then
                error_message="Deprecation Warning"
            else
                error_message="unknown"
                echo $err
            fi
        fi
        echo $i,$dir_name,$status,$error_message >> "$csv_file"
    done
done

cd $current_dir

echo "CSV file created: $csv_file"