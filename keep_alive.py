from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
   
	)

def keep_alive():
    t = Thread(target=run)
    t.start()