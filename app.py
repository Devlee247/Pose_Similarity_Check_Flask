from flask import Flask, json, request

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to flask'

@app.route('/data/get')
def data_get():
    return json.jsonify({'success': '성공'}), 200

@app.route('/post', methods=['POST'])
def post():
    result = request.get_json()
    return json.jsonify({'success': result}), 200

if __name__ == "__main__":
    app.run(debug=True)