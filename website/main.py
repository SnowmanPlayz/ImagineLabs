from flask import Flask
from flask import render_template, send_file, make_response, request, redirect, url_for
import time as tm

app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def auth():
    found_data = request.form.to_dict()
    print(found_data)
    save_user = open("user.txt","a")
    save_user.write( "\n" + str(found_data))
    save_user.close()
    return redirect("/image")

@app.route("/prompt", methods=["POST"])
def prompt():
    data = request.json
    print(data)
    save_user = open("user.txt","a")
    save_user.write( "\n" + str(data))
    save_user.close()
    return data


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/signup")
def signup():
    response = make_response(render_template("signup.html"))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# @app.route("/generate-image")
# def generate_image():
#     return render_template("image.html")

@app.route("/image")
def image():
    return render_template("image.html")

if __name__ == "__main__":
    app.run(debug=True)

