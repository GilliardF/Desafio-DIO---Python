import pymongo as pyM

# Conectando com o MongoDB

client = pyM.MongoClient('mongodb://gilliard:8921@localhost:27017')
print(client)

db = client['sistema_bancario']
collection = db['bank']
print(collection)