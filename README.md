# bard-bot
This is a simple bot that uses google bard api to talk to a user. It's got a few other commands that are less notable as well
# Setup
Clone the repository with
~~~
git clone https://github.com/https://github.com/wertytop/bard-bot
~~~
Then cd into the folder
~~~
cd ./bard-bot
~~~
Install requirements
~~~
pip install -r requirements.txt
~~~
After installing the requirements,
create a ***.env*** file 
~~~
touch .env
~~~
Inside that ***.env*** file, put your [Bard API key](https://github.com/dsdanielpark/Bard-API/blob/main/README.md) and discord bot token 
~~~
BARD_API_KEY=YOUR_KEY_HERE
DISCORD_TOKEN=YOUR_TOKEN_HERE
~~~
Save the .env file, and then run ***main.py*** with
~~~
python main.py
~~~
If that does not work, try 
~~~
python3 main.py
~~~
