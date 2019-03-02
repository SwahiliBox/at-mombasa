from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/sms')
def mysms():
	return render_template('sms.html')
	
@app.route('/home')
def home():
	return '<h1>Hello Bamburi!!!</h1>'

@app.route('/town/<name>')
def town(name):
	return f"<h1>I am in {name}</>"

@app.route('/names/<name>')
def names(name):
	if name.endswith('y'):
		return name[:-1] + "ifull"
	else:
		return name + "y"
if __name__ == "__main__":
	app.run(port=5000)