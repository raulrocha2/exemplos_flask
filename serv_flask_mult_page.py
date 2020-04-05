from flask import Flask, render_template, request
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "null"
Session(app)

list_name = []

@app.route("/")
def index():
	return render_template("page1.html")

@app.route("/more")
def more():
	return render_template("more.html")



@app.route("/getname")
def getname():
	return render_template("get_name.html")



@app.route("/listname", methods=["POST", "GET"])
def listname():
	names = request.form.get("names")
	list_name.append(names) 

	return render_template("list_name.html", list_name=list_name )



if (__name__ == "__main__"):
    #app.run(port = 5000)
    app.run(debug = True)