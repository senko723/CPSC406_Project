import requests
# import code.predictor.predictor as pr

# GET the current state of the blockchain
response = requests.get("http://127.0.0.1:5000/blockchain")
print(response.json())

# POST a new block to the blockchain
data = {"transactions": ["SVM equals ")]}
response = requests.post("http://127.0.0.1:5000/blockchain/add_block", json=data)
print(response.json())

# GET the current state of the blockchain again
response = requests.get("http://127.0.0.1:5000/blockchain")
print(response.json())

pr.predictor("advanced_svm")
