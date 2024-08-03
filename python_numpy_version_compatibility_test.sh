#!/bin/bash

output_name=$3
filename=$2
python_base_version=$1
package_name=$4
package_ok_version=$5

output_directory=`~/ve/bin/python testing_ground/test-case-creator.py $filename $output_name $python_base_version`
python_executable=~/ve$python_base_version/bin/python

$python_executable -m pip install "$package_name==$package_ok_version" --prefer-binary -i https://mirrors.aliyun.com/pypi/simple/
$python_executable $output_name 1> /dev/null
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

echo package version,line_number,status,error message > "$csv_file"

counter=0
for dir in "$output_directory"/*/; do
    dir_name=$(basename "$dir")
    cd $dir
    if [ -e False.db ]; then
        echo line $dir_name had been runned.
    else
        echo line number $dir_name didnt run
        echo ,$dir_name,-,didnt run >> "$csv_file"
    fi
done

for i in $current_dir/changelog-info/$package_name/*; do
    package_version=$(basename "$i")
    echo $i
    echo $package_version
    if [[ "$package_version" == *"1.2"* ]]; then
        python_executable=~/ve9/bin/python
    elif [[ "$package_version" == *"2.0."* ]]; then
        python_executable=~/ve9/bin/python
    elif [[ "$package_version" == *"1.14."* ]]; then
        python_executable=~/ve6/bin/python
    else
        python_executable=~/ve7/bin/python
    fi
    pip_not_worked=""
    $python_executable -m pip install "$package_name==$package_version" --prefer-binary -i https://mirrors.aliyun.com/pypi/simple/ || pip_not_worked="1"
    if [ ! -z "$pip_not_worked" ]; then
        error_message="pip error"
        status="-3"
        echo $package_version,,$status,$error_message >> "$csv_file"
    else
        for dir in "$output_directory"/*/; do
            dir_name=$(basename "$dir")
            cd $dir
            if [ -e False.db ]; then
                tmpFile=$(mktemp)
                $python_executable test_case.py 2>> $tmpFile 1> /dev/null
                err=$(cat $tmpFile)
                rm $tmpFile
                counter=$((counter + 1))
                status="0"
                error_message=""
                if [ ! -z "$err" ]; then
                    if [[ "$err" == *"invalid syntax"* ]]; then
                        error_message="invalid syntax"
                        status="-2"
                    elif [[ "$err" == *"results are diffrent"* ]]; then
                        error_message="results are diffrent"
                        status="-2"
                    elif [[ "$err" == *"has no attribute"* ]]; then
                        error_message="has not the attribute"
                        status="-2"
                    elif [[ "$err" == *"AttributeError"* ]]; then
                        error_message="Attribute Error"
                        status="-2"
                    elif [[ "$err" == *"NameError"* ]]; then
                        error_message="Name Error"
                        status="-2"
                    elif [[ "$err" == *"ModuleNotFoundError"* ]]; then
                        error_message="Module Not Found Error"
                        status="-2"
                    elif [[ "$err" == *"FileNotFoundError"* ]]; then
                        error_message="File Not Found Error"
                        status="-2"
                    elif [[ "$err" == *"ImportError"* ]]; then
                        error_message="Import Error"
                        status="-2"
                    elif [[ "$err" == *"Error"* ]]; then
                        error_message="unknown Error"
                        status="-2"
                        echo $err
                    elif [[ "$err" == *"DeprecationWarning"* ]]; then
                        status="-1"
                        error_message="Deprecation Warning"
                    else
                        error_message="unknown"
                        status="-2"
                        echo $err
                    fi
                fi
                echo $package_version,$dir_name,$status,$error_message >> "$csv_file"
            fi
        done
    fi
done

cd $current_dir

echo "CSV file created: $csv_file"

source ~/ve/bin/activate
csvtotable $csv_file $table_file
deactivate

rm original.py
