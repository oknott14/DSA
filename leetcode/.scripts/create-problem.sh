# dirname = $1
# test file name = $2
# code file name = $3

if [ -e "$1" ]; then
  echo "Using Existing Directory"
else
  mkdir $1
fi

if [ -e "$1/description.md" ]; then
  echo "Using Existing Description"
else
  touch $1/description.md
fi

if [ -z "$3" ] && [ -e "$3" ]; then
  echo "Using Existing Code File"
else
  touch $3
fi

if [ -e "$2" ]; then
  echo "Using Existing Test File"
else
  touch $2
fi

echo "'$1' Created"