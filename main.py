from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV files
finalresults_df = pd.read_csv('finalresults.csv')
output_df = pd.read_csv('output.csv')

@app.route('/')
def home():
    return "API is working!"

@app.route('/find_roll_details', methods=['GET'])
def find_roll_details():
    roll = request.args.get('roll')
    if not roll:
        return jsonify({'error': 'Please provide a roll number'}), 400

    roll_details = finalresults_df[finalresults_df['roll'] == int(roll)]
    if roll_details.empty:
        return jsonify({'error': 'Roll number not found'}), 404

    details = roll_details.to_dict(orient='records')[0]
    return jsonify(details), 200

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/find_roll_details?roll=1613613511
