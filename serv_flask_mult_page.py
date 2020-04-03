from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def index():
	return render_template("page1.html")

@app.route("/more")
def more():
	return render_template("more.html")



@app.route("/getname")
def getname():
	return render_template("get_name.html")

@app.route("/myname", methods=["POST"])
def myname():
    
    name = request.form.get('name')
    return render_template("my_name.html", name=name)	




if (__name__ == "__main__"):
    #app.run(port = 5000)
    app.run(debug = True)