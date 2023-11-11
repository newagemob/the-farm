# script that simply executes the src/main.py file in the root folder of this repository with python

echo "🤖 🚜 Starting The Farm: Instagram Bot 🚜 🤖"
echo "===================="

# get absolute path of the dir
BASEDIR=$(dirname "$BASH_SOURCE")
cd $BASEDIR

# ask if they want to start the bot or the manual script
echo "🤖 🚜 Which script would you like to run? 🚜 🤖"
echo "1. Bot"
echo "2. Manual"

read -p "Enter your choice: " choice

if [ $choice -eq 1 ]
then
    echo "🤖 🚜 Starting The Farm: Instagram Bot 🚜 🤖"
    echo "===================="
    python3 ./src/bot.py
elif [ $choice -eq 2 ]
then
    echo "🤖 🚜 Starting The Farm: Instagram Manual 🚜 🤖"
    echo "===================="
    python3 ./src/manual.py
else
    echo "🤖 🚜 Starting The Farm: Instagram Bot 🚜 🤖"
    echo "===================="
    python3 ./src/bot.py
fi
