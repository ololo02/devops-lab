from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

SECRET_KEY = "super-secret-hardcoded-123"  # 🚨 vuln intentionnelle

@app.route("/")
def hello():
    return "Hello DevOps Lab!"

@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")
    return subprocess.check_output(cmd, shell=True)  # 🚨 vuln intentionnelle

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Et `app/requirements.txt` :
```
flask==2.0.1
requests==2.20.0
