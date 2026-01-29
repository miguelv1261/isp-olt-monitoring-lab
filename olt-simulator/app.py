from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/api/onts")
def get_onts():
    onts = []
    for i in range(1, 33):
        onts.append({
            "ont_id": i,
            "status": random.choice(["online", "offline"]),
            "rx_power": round(random.uniform(-28, -18), 2),
            "tx_power": round(random.uniform(1, 4), 2),
            "traffic_mbps": random.randint(10, 500)
        })
    return jsonify(onts)

app.run(host="0.0.0.0", port=5000)
