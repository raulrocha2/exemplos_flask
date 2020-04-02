from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world, Flask!"

@app.route("/raul")
def raul():

    return"2 hello world, Raul!!!!"

@app.route("/lucas")
def nome():

    return"2 hello world, Lucas!!!!"


#mostrar o name adquirido na url
@app.route("/<string:name>")
def hello(name):
        return "Hello,{name}"


@app.route("/index")
def index_html():
    headline = "AnyThing in PYTHON varible"
    return render_template("index.html", headline=headline)


@app.route("/html")
def html():
    date_time = datetime.now()
    date_time_str = date_time.strftime('%d/%m/%Y %H:%M')

    return render_template("html_flask.html", date_time_str=date_time_str)


@app.route("/html_if")
def html_if():
	n1 = 30
	n2 = 43

	if n1 > n2:
		nR  = n1
		#n1 = True

	else:
		nR = n2
		#n2 = True


	return render_template("html_if.html", nR=nR)


 
if (__name__ == "__main__"):
    #app.run(port = 5000)
    app.run(debug = True)

