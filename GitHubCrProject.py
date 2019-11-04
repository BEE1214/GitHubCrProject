##=================================##
##=-Project:     GitHubCrProject -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2019-06-19 -=##
##=================================##

import sys
import os
import datetime
from github import Github

token = ""

def py():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile("/home/adam/Documents/FunProjects/CreateProject/Templates/PYTHON.py", f'{argv[1]}.{argv[2]}')
    return argv[2]

def sh():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile("/home/adam/Documents/FunProjects/CreateProject/Templates/BASH.sh", f'{argv[1]}.{argv[2]}')
    return argv[2]

def cpp():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile("/home/adam/Documents/FunProjects/CreateProject/Templates/CPP.cpp", f'{argv[1]}.{argv[2]}')
    return argv[2]

def vhd():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile("/home/adam/Documents/FunProjects/CreateProject/Templates/VHDL.vhd", f'{argv[1]}.{argv[2]}')
    return argv[2]

def latex():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile("/home/adam/Documents/FunProjects/CreateProject/Templates/LATEX.tex", f'{argv[1]}.{argv[2]}')
    return argv[2]

def clang():
    print(f'Creating {argv[1]}.{argv[2]}...')
    print(MakeFile(f'{argv[1]}.{argv[2]}'))
    FillFile("/home/adam/Documents/FunProjects/CreateProject/Templates/CLANG.c", f'{argv[1]}.{argv[2]}')
    return argv[2]

def GitFolder():
    reponame = str(argv[1])
    user = Github(token).get_user()
    repo = user.create_repo(reponame)
    pass

def FileChoice(aFormat):
    func = switcher.get(aFormat,lambda:'Wrong file format!')
    return func()

def FileLenght(aFile):
    with open(aFile) as iFile:
        for iLines,l in enumerate(iFile):
            pass
    return iLines + 1

def MakeFile(aFile):
    iName = aFile
    iFile = open(iName,"w+")
    if iFile.close() != None:
        eClose = 'Couldn\'t close the file.'
    else:
        return 'Done'

def OpenFile(aFile, aMod):
    iName = aFile
    iFile = open(iName,str(aMod))
    if iFile:
        print(f"File {aFile} opened...")
        return iFile
    else:
        print(f"Can\'t open {aFile}")

def FillFile(aTemplate, aCode):
    iDate = datetime.datetime.now()
    iTemplate = OpenFile(aTemplate, 'r').read()
    iCode = OpenFile(aCode, "w")
    iTemplate = re.sub("ProjectName", argv[1], iTemplate)
    iTemplate = re.sub("date", str(iDate.date()), iTemplate)
    iCode.write(iTemplate)
    return iCode

switcher = {
'py':py,
'sh':sh,
'cpp':cpp,
'vhd':vhd,
'tex':latex,
'c':clang
}

def main():
    GitFolder()
    FileChoice(argv[2])
    return 0

if __name__ == '__main__':
    # Source code
    main()
    pass