from flask import Flask

app = Flask("Hamada's App")

@app.route("/")
def hello_world():
	return "hello world!"

app.run(host='0.0.0.0', port=80, debug=True)
