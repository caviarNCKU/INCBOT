# INCBOT
Telegram bot created with python
## Setup
----
### Prequisite
* Install Python3
* Install BeautifulSoup for crawling data
## Server
* Use `ngrok` as a proxy
* `./ngrok http 8443` connect to port 8443
## Finite State machine
![](https://i.imgur.com/Yd2RMsE.png)
## Description
### Set local host
* `./ngrok http 8443` connect to port 8443
### Run the server
* `python app.py`
### Interact with INCBOT
* **user state**: Type in **weather**, **financial**, **sport**, or **game** to get through each state.
* **weather state**: Type in any word to show the current temperature and weather notification
* **financial state**: Type in corressponding stock number to get it Chinese name
* **game**: Type paper, sissors or stone to guess finger with the bot
* In **weather**, **financial**, **sport**, or **game**, type **user** to go back to the user state
