# Mac script that simply executes the quickstart file in the root folder of this repository with python

echo "🤖 🚜 Starting The Farm: Instagram Bot 🚜 🤖"
echo "===================="

# get absolute path of the dir
BASEDIR=$(dirname "$BASH_SOURCE")
cd $BASEDIR

# start the script
python3 ./engage.py
