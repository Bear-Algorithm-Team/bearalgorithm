#!/bin/bash

# Note: this script should run with the environmental variables such as APIKey, APIToken and BoardID.

function find_card_id_of_ticket() {
  local TicketNumber=$1

  # fetch all the cards in a given list
  all_cards=$(curl --silent --request GET \
  --url "https://api.trello.com/1/boards/${BoardID}/cards?key=${APIKey}&token=${APIToken}" \
  --header 'Accept: application/json')

  # return full card name where contains TicketNumber
  echo "$all_cards" | jq -r --arg ticket "$TicketNumber" '.[] | select(.name | contains($ticket)) | .name' | tr -d '\r'

  # return card id where name contains TicketNumber
  echo "$all_cards" | jq -r --arg ticket "$TicketNumber" '.[] | select(.name | contains($ticket)) | .id' | tr -d '\r'
}

function fetch_list_ids() {
    local list_name="$1"

    # fetch all the lists
    response=$(curl --silent --request GET \
      --url "https://api.trello.com/1/boards/${BoardID}/lists?key=${APIKey}&token=${APIToken}" \
      --header 'Accept: application/json')

    # fetch the ID of the Done list
    echo "$response" | jq -r --arg name "$list_name" '.[] | select(.name == $name).id'
}

# fetch the target list id
TargetListID=$(fetch_list_ids "$2")

# find the card id of the ticket
  IFS=$'\n' read -d '' -r -a output_array < <(find_card_id_of_ticket "$1" && printf '\0')
  target_card_name="${output_array[0]}"
  target_card_id="${output_array[1]}"
  if [ -n "$target_card_id" ]; then
    ERROR_FILE=$(mktemp)

    # Update Trello
    curl --silent --request PUT \
      --url "https://api.trello.com/1/cards/${target_card_id}?key=${APIKey}&token=${APIToken}" \
      --header 'Accept: application/json' \
      --data "idList=$TargetListID&pos=top" \
      -o /dev/null 2> "$ERROR_FILE"

    if [ $? -eq 0 ]; then
      echo "Successfully changed the status of the card \"$target_card_name\" into \"$2\"."
    else
      echo "Failed to change the status of the card \"$target_card_name\" into \"$2\": "
      cat "$ERROR_FILE"
    fi

    rm "$ERROR_FILE"
    exit $?
  fi

echo "Failed to find the card containing the given string \"$1\""
exit 1
