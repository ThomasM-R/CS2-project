from flask import Flask, request, send_file, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return send_file("public/index.html")

@app.route("/<path:path>")
def public_files(path):
    return send_from_directory("public/", path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)