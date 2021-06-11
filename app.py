from flask import Flask, render_template, redirect, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("body.html",hospitals = get_all_hospital())

@app.route("/get_hospital")
def get_all_hospital():
	h = json.loads(open("assets/data.json","r").read())
	# print(h)
	return (h)

@app.route("/add_hospital",methods=["POST"])
def add_hospital():
	name = request.form["name"]
	latlng = request.form["latlng"].split(",")
	data = {
		"name": name,
		"latlng":latlng,
		"data": [],
		"logs":[]
	}
	h = json.loads(open("assets/data.json","r").read())
	h.append(data)
	with open("assets/data.json",'w') as outfile:
		json.dump(h, outfile, indent="\t")
	return "DONE"


@app.route("/push_info",methods=["POST"])
def push_info():
	h = json.loads(open("assets/data.json","r").read())
	counter = 0
	for details in h:
		if details["name"] == request.form["name"]:
			print(h[counter]["data"].append(request.form))
		counter += 1
	with open("assets/data.json",'w') as outfile:
		json.dump(h, outfile, indent="\t")
	return ""


@app.route("/h")
@app.route("/h",methods=["POST"])
def h():
	res = json.loads(open("assets/data.json","r").read())
	return jsonify(res)

app.run(debug=True, host = "0.0.0.0")