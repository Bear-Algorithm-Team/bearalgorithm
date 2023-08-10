# geekbot for discord

## Description

The `setup_geekbot.sh` script allows you to automate daily report reminders on Discord. Once installed on your computer, it schedules a task to run every weekday at 10 AM. At this time, users listed in the config.json file will receive a Direct Message, prompting them to compose their daily report. These reminders are sent within the specified Discord channel from the configuration. Generally, this utility runs on an admin's machine, so there's no action required from the regular users.

## Specification

### The content of `config.json`
```json
{
    "CRONTAB": "0 10 * * 1-5",
    "GUILD_ID": 1138900602823393320,
    "CHANNEL_NAME": "일반",
    "USERS": [{"USER_ID": 882859405283041280}, {"USER_NAME": "Kangwook Lee"}],
    "GEEKBOT_ID": "MTEzODg5MDAzNDM5MzY2NTY5OA.GfP9Zf.Lort5HAlrKrXuyyVjwGFYoxJ-ineIG3qoVoFuE"
}
```

- `CRONTAB`: Specifies the cron schedule for the task.

- `GUILD_ID`: The unique identifier for the Discord server (also known as a guild) where the bot operates. It can be obtained from Discord's developer mode.

- `CHANNEL_NAME`: The name of the channel in the Discord server where the bot sends messages. You can obtain it in your guild's channel list.

- `USERS`: A list of users the bot asks to compose their daily report. 

  - `USER_ID`: Each user can be identified either by their unique `USER_ID`. It can be obtained from Discord's developer mode.
  
  - `USER_NAME`: This is the name shown in the daily report and can be set as desired.

- `GEEKBOT_ID`: The bot's unique authentication token, required for logging into Discord's API and performing actions on behalf of the bot user. You can obtain it when you create a new bot for Discord.
