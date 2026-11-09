## About Easterscraping

If you are a fan of Stuttgart's chocolates, this script will suit you well. By the simple action of executing the file, you are able to send to yourself (or anyone that you have the email adress) a report of all the available chocolates and their respective price in the bomboniere section of Stuttgart's website. Project made with Python as the main programming language and MySQL as the database to store the information.

## REQUIREMENTS
In order for the script to run properly, you will need the following software to be installed:
- MySQL 8.0
- Python 3.13
- A code editor (I personally recommend VSCode) that supports Python language 
- An email to send the reports that has a app password
- An email to receive the reports

After downloading the python file and requirements.txt, open the .py with your favorite code editor and change the email on the bottom of the code, alongside with the app password
Before running, you need to open the terminal for your project and run the following command:
pip install -r requirements.txt
 
**
The project originally comes with a example email for both sending and receiving as well as a exemple app password
**

If you want to make an executable file for the script, the following steps are needed:
In the terminal, do "pyinstaller --onefile --noconsole main.py"
you will notice that new folders will be created on the directory of the script. Open the "dist" folder and then "main", inside it you will be able to find the script as an .exe that will run and send the email every time you open it
