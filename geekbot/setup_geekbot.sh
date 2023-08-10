#!/bin/bash

# check if coreutils is installed
if ! command -v coreutils &> /dev/null; then
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

# Get values from config.json
CONFIG_FILE="./config.json"
CRONTAB=$(jq -r '.CRONTAB' $CONFIG_FILE)
GUILD_ID=$(jq -r '.GUILD_ID' $CONFIG_FILE)
CHANNEL_NAME=$(jq -r '.CHANNEL_NAME' $CONFIG_FILE)
GEEKBOT_ID=$(jq -r '.GEEKBOT_ID' $CONFIG_FILE)

# Store the content of the current crontab in a temporary file
crontab -l > /tmp/cron_temp

# Loop through each user in the USERS array
length=$(jq '.USERS | length' $CONFIG_FILE)
for (( i = 0 ; i < $length ; i++ )); do
    USER_ID=$(jq -r ".USERS[$i].USER_ID" $CONFIG_FILE)
    USER_NAME=$(jq -r ".USERS[$i].USER_NAME" $CONFIG_FILE)

    # Add a new cron task to the temporary cron file for each user
    echo "${CRONTAB} /usr/local/bin/gtimeout 86400 /usr/bin/python3 geekbot.py $GUILD_ID \"$CHANNEL_NAME\" $USER_ID \"$USER_NAME\" $GEEKBOT_ID" >> /tmp/cron_temp
done

# Apply the updated cron file to crontab
crontab /tmp/cron_temp

# Remove the temporary file
rm /tmp/cron_temp
