#!/bin/bash

# Activate the virtual environment
source my_env/Scripts/activate

# Run the test suite
pytest test_app.py
TEST_RESULT=$?

# Exit with 0 if tests passed, 1 if any failed
if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed."
    exit 1
fi