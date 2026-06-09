from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Jarvis AI Assistant</title>
        <style>
            body {
                background: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 120px;
            }
            h1 {
                font-size: 50px;
                color: #38bdf8;
            }
            p {
                font-size: 22px;
            }
            .box {
                border: 1px solid #38bdf8;
                border-radius: 20px;
                padding: 40px;
                width: 60%;
                margin: auto;
                box-shadow: 0 0 25px #38bdf8;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🤖 Jarvis AI Assistant</h1>
            <p>AI-powered virtual assistant built with Python.</p>
            <p>Status: Running Successfully ✅</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "ok"
    }