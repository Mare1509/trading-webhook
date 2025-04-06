from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Neue Nachricht empfangen:")
    print(data)
    signal = data.get("signal")
    pair = data.get("pair")
    if signal == "buy" and pair == "EUR/USD":
        print("🚀 Kaufsignal erkannt für EUR/USD!")
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
