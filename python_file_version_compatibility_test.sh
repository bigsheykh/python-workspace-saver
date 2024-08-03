#!/bin/bash

output_name=$3
filename=$2
python_base_version=$1

output_directory=`~/ve/bin/python testing_ground/test-case-creator.py $filename $output_name $python_base_version`

echo ~/ve$python_base_version/bin/python $output_name
~/ve$python_base_version/bin/python $output_name 1> /dev/null
echo $output_directory

# Set the base directory
current_dir=`pwd`
filename_without_ext="${output_name%.*}"
csv_file="$current_dir/$filename_without_ext.csv"
diff_with_original_file="$current_dir/$filename_without_ext._diff.html"
table_file="$current_dir/$filename_without_ext._table.html"
new_file="$current_dir/$filename_without_ext.py.html"
original_file="$current_dir/$filename_without_ext._old_py.html"

~/ve/bin/python -m yapf -i original.py $output_name
diff --side-by-side -d --color=always original.py $output_name | aha --black > $diff_with_original_file
pygmentize -f html -O full -o $original_file original.py
pygmentize -f html -O full -o $new_file $output_name

echo python version,line_number,status,error message > "$csv_file"

counter=0
for dir in "$output_directory"/*/; do
    dir_name=$(basename "$dir")
    cd $dir
    if [ -e False.db ]; then
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
                    error_message="invalid syntax"
                elif [[ "$err" == *"results are diffrent"* ]]; then
                    error_message="results are diffrent"
                elif [[ "$err" == *"has no attribute"* ]]; then
                    error_message="has not the attribute"
                elif [[ "$err" == *"ModuleNotFoundError"* ]]; then
                    error_message="ModuleNotFoundError"
                elif [[ "$err" == *"Error"* ]]; then
                    error_message="unknown Error"
                    echo $err
                elif [[ "$err" == *"DeprecationWarning"* ]]; then
                    status="-1"
                    error_message="Deprecation Warning"
                else
                    error_message="unknown"
                    echo $err
                fi
            fi
            echo $i,$dir_name,$status,$error_message >> "$csv_file"
        done
    else
        echo line number $dir_name didnt run
        echo ,$dir_name,-,didnt run >> "$csv_file"
    fi
done

cd $current_dir

echo "CSV file created: $csv_file"
source ~/ve/bin/activate
csvtotable $csv_file $table_file
deactivate

rm original.py
