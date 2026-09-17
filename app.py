
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🎬 Writers Room</h1>
    <h2>Story & Screenplay Management Portal</h2>
    <p>Welcome Murali</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
