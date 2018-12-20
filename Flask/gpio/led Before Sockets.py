from flask import Flask, render_template, request
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
from time import sleep 
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def blink_worker():
	while True:
		GPIO.output(17,GPIO.HIGH)
		sleep(2)
		GPIO.output(17,GPIO.LOW)
		sleep(2)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/blink")
def blink():
	t1 = threading.Thread(target= blink_worker)
	t1.start()
	state = GPIO.input(17)
	templateData = {"LED" : state}nano
	return render_template("blink.html",**templateData)

@app.route("/switch")
def switch():
	state = GPIO.input(17)
	return render_template("switch.html",state)

if __name__ == "__main__":
     socketio.run(app,host="0.0.0.0",port=80)
