#!/bin/bash

function gitPr () {
    # Check if arguments aren't empty
    if [ -z "$2" ]; then 
        echo Second argument is empty...
        echo Exiting...
    elif [ -z "$1" ]; then
        echo No argument entered...
        echo Exiting...
    else
        if [ ! -d "$~/Documents/FunProjects/$1" ]; then
            mkdir ~/Documents/FunProjects/$1
            echo Creating folder $1...
            cd ~/Documents/FunProjects/$1
        else
            echo Moving to folde $1...
            cd ~/Documents/FunProjects/$1
        fi

        python GitHubCrProject.py $1 $2
        touch README.md
        if [ -d "~/Documents/FunProjects/$1.$2"]; then
            chmod 744 $1.$2
            git init
            git remote add origin git@github.com:BEE1214/$1.git
            git add .
            git commit -m "Initial commit"
            git push -u origin master
            lsd -l --group-dirs first
            code .
        else
            echo File $1.$2 does not exist...
        fi
    fi
}