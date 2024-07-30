#!/bin/bash

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
