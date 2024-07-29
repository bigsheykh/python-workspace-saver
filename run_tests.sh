#!/bin/bash

./python_file_version_compatibility_test.sh 7 poe_ai_generated/first.py first_modified.py
./python_file_version_compatibility_test.sh 7 poe_ai_generated/second.py second_modified.py
./python_file_version_compatibility_test.sh 7 poe_ai_generated/third.py third_modified.py
./python_file_version_compatibility_test.sh 7 poe_ai_generated/fourth.py fourth_modified.py
./python_file_version_compatibility_test.sh 5 poe_ai_generated/fifth.py fifth_modified.py
./python_file_version_compatibility_test.sh 11 poe_ai_generated/sixth.py sixth_modified.py
