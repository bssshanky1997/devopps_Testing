import os
import threading
import webbrowser

from flask import Flask

app = Flask(__name__)


def open_browser():
    url = "http://127.0.0.1:5000"
    try:
        os.startfile(url)
    except AttributeError:
        webbrowser.open_new_tab(url)

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
    threading.Timer(1.0, open_browser).start()
    app.run(host="0.0.0.0", port=5000)