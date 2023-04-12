from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():
    req_data = request.get_json()
    id = req_data['id']
    type = req_data['type']
    attribute = req_data['attribute']
    data = req_data['data']
    # Process the data as needed
    # Check if the ID already exists in the JSON file
    with open('data.json', 'r') as f:
        for line in f:
            data_dict = json.loads(line)
            if data_dict['id'] == id:
                response = {'message': 'ID already exists in data.json'}
                return jsonify(response), 409
    # Save the data to a local JSON file
    data_dict = {
        "id": id,
        "type": type,
        "attribute": attribute,
        "data": data
    }
    with open('data.json', 'a') as f:
        f.write(json.dumps(data_dict))
        f.write('\n')
    # Return a response
    response = {'message': 'Data received and saved successfully'}
    return jsonify(response)

@app.route('/api/data', methods=['GET'])
def get_data():
    data_list = []
    with open('data.json', 'r') as f:
        for line in f:
            data_dict = json.loads(line)
            data_list.append(data_dict)
    # Return a response
    response = {'data': data_list}
    return jsonify(response)

@app.route('/api/data/reset', methods=['GET'])
def reset_data():
    with open('data.json', 'w') as f:
        pass
    # Return a response
    response = {'message': 'Data.json reset successfully'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

