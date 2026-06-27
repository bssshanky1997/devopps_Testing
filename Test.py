from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Demo</title>
        </head>
        <body style="font-family:Arial;text-align:center;margin-top:100px;">
            <h1>🚀 Shashank is DevOps Engineer 🚀</h1>
            <h2>Application Successfully Deployed!</h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
