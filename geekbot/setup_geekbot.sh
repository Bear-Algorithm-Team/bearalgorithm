#!/bin/bash

# check the number of arguments
if [ "$#" -eq 0 ] || [ "$#" -gt 1 ]; then
    echo "Error: The number of arguments is not appropriate. You should use one argument for this command."
    echo "Example: ./setup_geekbot.sh \"MDAzND....\" # The token of the discord bot"
    exit 1
fi

# check if coreutils is installed
if ! command -v gls &> /dev/null; then
    echo "Error: coreutils is not installed."
    echo "Please install coreutils using 'brew install coreutils' and try again."
    exit 1
fi

# check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed."
    echo "Please install jq using 'brew install jq' and try again."
    exit 1
fi

# Check if the 'discord' module is installed in /usr/bin/python3
if ! /usr/bin/python3 -c "import discord" 2>/dev/null; then
    echo "Error: The 'discord' module is not installed for /usr/bin/python3."
    echo "Please install it using the command: /usr/bin/pip3 install discord.py"
    exit 1
fi

# Get values from config.json
SCRIPT_PATH="$(cd "$(dirname "$0")"; pwd -P)"
CONFIG_FILE="${SCRIPT_PATH}/config.json"
CRONTAB=$(jq -r '.CRONTAB' $CONFIG_FILE)
GUILD_ID=$(jq -r '.GUILD_ID' $CONFIG_FILE)
CHANNEL_NAME=$(jq -r '.CHANNEL_NAME' $CONFIG_FILE)

# Initialize ~/.geekbot/run.sh
mkdir -p ~/.geekbot
RUN_FILE_PATH=~/.geekbot/run.sh
rm -f $RUN_FILE_PATH
echo "#!/bin/bash" >> $RUN_FILE_PATH
chmod +x $RUN_FILE_PATH

# Loop through each user in the USERS array
GTIMEOUT_PATH=$(which gtimeout)
length=$(jq '.USERS | length' $CONFIG_FILE)
for (( i = 0 ; i < $length ; i++ )); do
    USER_ID=$(jq -r ".USERS[$i].USER_ID" $CONFIG_FILE)
    USER_NAME=$(jq -r ".USERS[$i].USER_NAME" $CONFIG_FILE)

    echo "${GTIMEOUT_PATH} 86400 /usr/bin/python3 \
      ${SCRIPT_PATH}/geekbot.py $GUILD_ID \"$CHANNEL_NAME\" $USER_ID \"$USER_NAME\" \
      $1 >> ~/.geekbot/run.log" >> $RUN_FILE_PATH
done

# Store the content of the current crontab in a temporary file
crontab -l > /tmp/cron_temp

# Add a new cron task to the temporary cron file for each user
echo "${CRONTAB} $RUN_FILE_PATH" >> /tmp/cron_temp

# Apply the updated cron file to crontab
crontab /tmp/cron_temp

# Remove the temporary file
rm /tmp/cron_temp
