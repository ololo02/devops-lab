from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY")

@app.route("/")
def hello():
    return "Hello DevOps Lab!"

ALLOWED_COMMANDS = {
    "ls": ["/bin/ls"],
    "pwd": ["/bin/pwd"],
    "date": ["/bin/date"],
}

@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")
    if cmd not in ALLOWED_COMMANDS:
        return "Command not allowed", 403
    return subprocess.check_output(ALLOWED_COMMANDS[cmd])

if __name__ == "__main__":
    app.run(host=os.environ.get("FLASK_HOST", "127.0.0.1"), port=5000)
```

Et `app/requirements.txt` :
```
flask==2.0.1
requests==2.20.0
