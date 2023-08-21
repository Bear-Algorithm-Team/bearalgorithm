# bearalgorithm

## Intro

This repository is for studying algorithms. Users submit their solutions to algorithm problems via pull requests, and reviewers conduct code reviews. Once the review is completed and the code is approved, it is merged into the main branch.

## Initial setup

1. Clone this repository

2. Move to the repository's directory and run this command.

```zsh
bin/command/one-time-setup
```

We use [Trello](https://trello.com/b/g3XvbpAQ/problem-solving) as our ticket management tool. Unlike Jira, Trello does not automatically assign ticket numbers when adding a new card. Therefore, a custom command called `bearcard` has been created to enable this. This custom command can be used when running the `one-time-setup` script.

## Procedure

1. Create a new card with the `bearcard` command. With this command, a new card will be added to the `To Do` list in Trello.

```zsh
bearcard "Kakao 2018 #3 Shuttle bus"
```

- Please note that you must have the Trello API key & token in your local PC before running this command. Please ask the administrator for the key & token and run the command below to save it to your local PC.

```zsh
bearcard --update-key
```

2. Create a new branch for this card, open a new PR for it, and ask a review for it to reviewers.

3. Merge the branch once it is approved.
    - The status of the card will be changed into `Done` automatically after merging if the PR title is written in a proper format. (i.e. "[PS-22] Kakao 2018 #3 Shuttle bus")

## Useful features

### Setting up your Trello ID for bearcard

```zsh
bearcard --setup-id "Your Trello name"
```

If you run this command with your Trello name, your Trello ID will be fetched and it will be saved in `~/.bearcard/id`. Then Trello will assign you as the assignee for the card automatically when you run bearcard.
