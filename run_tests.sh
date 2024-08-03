#!/bin/bash

# ~/ve/bin/python -m pip install changelogs csvtotable Pygments -i https://mirrors.aliyun.com/pypi/simple/

TEST_FILES_DIRECTORY=poe_ai_generated
RESULTS_DIRECTORY=compatibility_results

rm -rf $RESULTS_DIRECTORY /tmp/python-workspace
mkdir -p $RESULTS_DIRECTORY

./python_file_version_compatibility_test.sh 7  $TEST_FILES_DIRECTORY/first.py  $RESULTS_DIRECTORY/first_modified.py
./python_file_version_compatibility_test.sh 7  $TEST_FILES_DIRECTORY/second.py $RESULTS_DIRECTORY/second_modified.py
./python_file_version_compatibility_test.sh 7  $TEST_FILES_DIRECTORY/third.py  $RESULTS_DIRECTORY/third_modified.py
./python_file_version_compatibility_test.sh 7  $TEST_FILES_DIRECTORY/fourth.py $RESULTS_DIRECTORY/fourth_modified.py
./python_file_version_compatibility_test.sh 5  $TEST_FILES_DIRECTORY/fifth.py  $RESULTS_DIRECTORY/fifth_modified.py
./python_file_version_compatibility_test.sh 11 $TEST_FILES_DIRECTORY/sixth.py  $RESULTS_DIRECTORY/sixth_modified.py

./python_pacakge_version_compatibility_test.sh 9 poe_ai_generated/scrapy_test.py compatibility_results/scipy_modified.py scrapy 1.7.4
./python_pacakge_version_compatibility_test.sh 9 poe_ai_generated/numpy_test.py compatibility_results/numpy_modified.py numpy 1.26.4
