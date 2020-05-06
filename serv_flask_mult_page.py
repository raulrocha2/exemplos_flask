from flask import Flask, render_template, request, session
from flask_session import Session 


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "FileSystem"
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
	if Session.get("list_name") is None:
		Session["list_name"] = []
	if request.method == "POST":
		get_name = request.form.get("get_name")
		Session["list_name"].append(get_name) 

	return render_template("list_name.html", list_name=Session["list_name"] )



if (__name__ == "__main__"):
    #app.run(port = 5000)
    app.run(debug = True)