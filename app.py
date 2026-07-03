from flask import Flask

app = Flask(__name__)
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"

@app.route("/")
def home():
    return {"message": "Hello from the DevSecOps demo app!"}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    