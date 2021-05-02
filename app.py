from flask import Flask, jsonify
import getting_data as d
# from flask_jsonify import jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return d.final_df.to_json()

if __name__ == "__main__":
    app.run(debug=True)
