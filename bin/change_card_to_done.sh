#!/bin/bash

# set API 
APIKey=""
APIToken=""
BoardID=""

function find_card_id_of_ticket() {
  local ListID=$1
  local TicketNumber=$2

  # fetch all the cards in a given list
  all_cards=$(curl --silent --request GET \
  --url "https://api.trello.com/1/lists/${ListID}/cards?key=${APIKey}&token=${APIToken}" \
  --header 'Accept: application/json')

  # return card id where name contains TicketNumber
  echo "$all_cards" | jq -r --arg ticket "$TicketNumber" '.[] | select(.name | contains($ticket)) | .id'
}

function fetch_list_ids() {
    # fetch all the lists
    response=$(curl --silent --request GET \
      --url "https://api.trello.com/1/boards/${BoardID}/lists?key=${APIKey}&token=${APIToken}" \
      --header 'Accept: application/json')

    # fetch the ID of the Done list
    echo "$response" | jq -r '.[] | select(.name == "Done").id'

    # fetch all the list IDs
    echo "$response" | jq -r '.[].id'
}

# Call function and capture output in an array
IFS=$'\n' read -d '' -r -a output_array < <(fetch_list_ids && printf '\0')
DoneListID="${output_array[0]}"
list_ids=("${output_array[@]:1}")

# find the card id of the ticket
for id in "${list_ids[@]}"; do
  target_card_id=$(find_card_id_of_ticket "$id" "$1")
  if [ -n "$target_card_id" ]; then
    # Update Trello
    curl --silent --request PUT \
      --url "https://api.trello.com/1/cards/${target_card_id}?key=${APIKey}&token=${APIToken}" \
      --header 'Accept: application/json' \
      --data "idList=$DoneListID&pos=top" \
      -o /dev/null
    exit $?
  fi
done

exit 1
