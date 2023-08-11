# bearalgorithm

## Intro

This repository is for studying algorithms. Users submit their solutions to algorithm problems via pull requests, and reviewers conduct code reviews. Once the review is completed and the code is approved, it is merged into the main branch.

## Initial setup

1. Clone this repository

2. Move to the repository's directory and run this command.

```zsh
./command/one-time-setup
```

We use [Trello](https://trello.com/b/g3XvbpAQ/problem-solving) as our ticket management tool. Unlike Jira, Trello does not automatically assign ticket numbers when adding a new card. Therefore, a custom command called `bearcard` has been created to enable this. This custom command can be used when running the setup script.

## Procedure

1. Create a new card with the `bearcard` command. With this command, a new card will be added to the `To Do` list.

```zsh
bearcard "Kakao 2018 #3 Shuttle bus"
```

2. Create a new branch for this card, open a new PR for it, and ask a review for it to reviewers.

3. Merge the branch once it is approved, and change the status of the card into `Done`. 

    - We should use `Squash and merge` when merging PRs. Using this, we can write a new commit message for the squashed commit.
