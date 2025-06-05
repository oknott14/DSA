TEST_TEMPLATE='''class Solution:\n\tdef prob_function():\n\t\tpass\n\nsoln = Solution()\n\ndef test_case_1():\n\tassert true'''
DIRECTORY_PATH="./leetcode/$1"
TEST_FILE_PATH="$DIRECTORY_PATH/test_$1.py"

bash ./leetcode/.scripts/create-problem.sh $DIRECTORY_PATH $TEST_FILE_PATH

if [ -e "$TEST_FILE_PATH" ] && [ ! -s "$TEST_FILE_PATH" ]; then
  echo "Inserting Template File"
  cat ./leetcode/.scripts/test_template.py > $TEST_FILE_PATH
fi