#!/bin/bash

# options to display
options=("FastApi (Python)" "NodeJS (Javascript)" "Cancel\n")


RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
PROMT_MESSAGE='echo -e "\033[0mCHOOSE THE BACKEND ENVIRONMENT: "\n'

printf "\033[?25l\033[s"

# Prompt the user for a microservice name
echo -n "Enter a name for your microservice: "
read microservice_name

selected=0

# Display options
while true; do
    printf "\033[u\n"
    $PROMT_MESSAGE
    for i in "${!options[@]}"; do
        if [ $i -eq $selected ]; then
            printf "${GREEN}➤ ${options[$i]}${NC}\n"
        else
            printf "  ${options[$i]}\n"
        fi
    done

    # read user input
    read -s -n1 input

    # uptade selected option
    case $input in
        A) # Up Arrow
            if [ $selected -gt 0 ]; then
                selected=$((selected - 1))
            fi
            ;;
        B) # Down Arrow
            if [ $selected -lt $((${#options[@]} - 1)) ]; then
                selected=$((selected + 1))
            fi
            ;;
        "") # Enter
            option="${options[$selected]}"
            break
            ;;
        *) ;;
    esac
done

printf "\033[u\033[?25h"


case $option in
    "${options[0]}")
        echo "Creating FastApi (Python) microservice $microservice_name ..."
        # Python Commands
        ;;
    "${options[1]}")
        echo "Creating NodeJS (Javascript) microservice $microservice_name ..."
        # Javascript Commands
        ;;
    "${options[2]}")
        echo "Exiting..."
        ;;
    *) echo "Invalid Option";;
esac
