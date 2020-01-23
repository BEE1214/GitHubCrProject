#!/bin/bash

function gitPr () {
    # Check if arguments aren't empty


    case $1 in
        -h) if [[ $# -gt 1 ]]; then
                echo "Wrong arguments"
            else
                cat ~/Documents/FunProjects/GitHubCrProject/help.txt
            fi
        ;;

        *)
            FILE="$1.$2"
            FOLDER="~/Documents/FunProjects/$1"

            if [ -z "$1" ]; then 
                echo Second argument is empty...
                echo Exiting...
            elif [ -z "$2" ]; then
                echo No argument entered...
                echo Exiting...
            else
                if [ ! -d "$FOLDER" ]; then
                    mkdir ~/Documents/FunProjects/$1
                    echo Creating folder $1...
                    cd ~/Documents/FunProjects/$1
                else
                    echo Moving to folde $1...
                    cd ~/Documents/FunProjects/$1
                fi

                python3 ~/Documents/FunProjects/GitHubCrProject/GitHubCrProject.py $1 $2
                if [ -f "$FILE" ]; then
                    chmod 744 $1.$2
                    echo "Creatin README.md file"
                    touch README.md
                    echo "# $1" >> README.md
                    echo "Initializing git repository"
                    git init
                    echo "Adding all files to repository"
                    git add .
                    echo "Commiting initial commit"
                    git commit -m "Initial commit"
                    echo "Adding origin to https://github.com/BEE1214/$1.git"
                    git remote add origin https://github.com/BEE1214/$1.git
                    echo "Pushing files to GitHub"
                    git push -u origin master
                    lsd -la --group-dirs first
                    code .
                    code README.md
                    code $1.$2
                else
                    echo "File $FILE does not exist"
                fi
            fi
        ;;
}