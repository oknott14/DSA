# $1 = dirname

DIRECTORY_PATH="./leetcode/$1"
TEST_FILE_PATH="$DIRECTORY_PATH/$1.test.ts"
CODE_FILE_PATH="$DIRECTORY_PATH/code.ts"

bash ./leetcode/.scripts/create-problem.sh $DIRECTORY_PATH $TEST_FILE_PATH $CODE_FILE_PATH

if [ -e "$TEST_FILE_PATH" ] && [ ! -s "$TEST_FILE_PATH" ]; then
  echo "Inserting Template File"
  cat ./leetcode/.scripts/test.template.ts > $TEST_FILE_PATH
  sed -i "s/{testName}/$1/g" $TEST_FILE_PATH
fi