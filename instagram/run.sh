# script that simply executes the src/main.py file in the root folder of this repository with python

echo "🤖 🚜 Starting The Farm: Instagram Bot 🚜 🤖"
echo "===================="

# get absolute path of the dir
BASEDIR=$(dirname "$BASH_SOURCE")
cd $BASEDIR

# start the script
python3 ./src/main.py
