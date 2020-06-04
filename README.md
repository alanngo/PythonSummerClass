# Python Summer Class
## Prereqs 
Download and install the following 
- Python3: https://www.python.org/downloads/release/python-380/
- Pycharm: https://www.jetbrains.com/pycharm/download/

If you're running a Windows OS, you also need to install the WSL linux terminal
1. Open start menu, type and click on "Developer Settings"
2. Check "Developer Mode" and reboot if prompted
3. Open start menu, type and click "Turn Windows Features On or Off"
4. Check "Windows Subsystem for Linux" and reboot when prompted
5. Go to Microsoft Store and search "Ubuntu"
6. Click the link that says "Ubuntu" and download it
7. Once it finishes, launch the program and let it initialize
8. Enter your username and password
    - if you don't see your password, while you're typing, it's normal (it's a linux security feature)
    - if you think you messed up on the password, press backspace at least 30x and retype your password
9. That's it you are now ready to run python

## Running Python
##### Via terminal
1. open terminal and navigate to your python working directory
2. type "python3 <program.py>" and press enter

##### Via Pycharm
1. Open your Python project
2. Open <file_name.py>
3. right click anywhere on your code and click "Run <file_name.py>"

## Setting up Github
INITIALIZATION
1. Create remote repo named PythonSummerClass on Github
2. Create local repo named PythonSummerClass
3. Open terminal
4. $ cd <PATH TO LOCAL REPO>
5. $ touch README.md
6. $ git init
7. $ git add .
8. $ git commit - m "initial commit"
9. $ git remote add origin https://github.com/<USERNAME>/PythonSummerClass.git
- replace USERNAME w/ your github username
10. $ git push -u -f origin master
11. $ git pull

CONTINUOUS
1. $ git add <file name>
2. $ git commit -m "<message>"
3. $ git push


