if ls ./leetcode/$1; then
  echo "Using Existing Directory"
else
  mkdir ./leetcode/$1
fi

if ls ./leetcode/$1/description.md; then
  echo "Using Existing Description"
else
  touch ./leetcode/$1/description.md
fi

if ls ./leetcode/$1/code.$2; then
  echo "Using Existing Code File"
else
  touch ./leetcode/$1/code.$2
fi

if ls ./leetcode/$1/$1.test.$2; then
  echo "Using Existing Test File"
else
  touch ./leetcode/$1/$1.test.$2
fi

echo $1 " Created"