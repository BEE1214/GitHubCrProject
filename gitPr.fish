##=================================##
##=-Project: GitHubCrProject------=##
##=-Author: Adam Dvorsky----------=##
##=-Date: 2019-06-19 -------------=##
##=================================##
#Fish function for creating new projects and upload it to github.

function GitHubCrProject
    cd /home/adam/Documents/FunProjects/
    if [ ! -d "/home/adam/Documents/FunProjects/$argv[1]" ]
        mkdir /home/adam/Documents/FunProjects/$argv[1]
        echo Creating folder $argv[1]...
        cd /home/adam/Documents/FunProjects/$argv[1]
    else
        cd /home/adam/Documents/FunProjects/$argv[1] 
    end
    python /home/adam/Documents/FunProjects/CreateProject/createPr.py $argv[1] $argv[2]
    chmod 744 $argv[1].$argv[2]
    ls -l

end