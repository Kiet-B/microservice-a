import json
from flask import Flask, request


app = Flask(__name__)


def add_product(newProduct):
  with open('userProduct.json', 'r') as file:
    userProductJSON = json.load(file)

    userID, productName, description, price = parse_request(newProduct)

    if userID not in userProductJSON.keys():
      userProductJSON[userID] = {productName : {'description' : description, 'price' : price}}
    else:
      if productName in userProductJSON[userID].keys():
        return 'Product already exist'
      userProductJSON[userID][productName] = {'description' : description, 'price' : price}

  with open('userProduct.json', 'w') as file:
    json.dump(userProductJSON, file)

  return productName + ' has been added'
  

def remove_product(productRemove):
  with open('userProduct.json', 'r+') as file:
    userProductJSON = json.load(file)

    userID, productName, description, price = parse_request(productRemove)

    if userID not in userProductJSON.keys():
      return 'No such user exist'
    
    if productName not in userProductJSON[userID].keys():
      return 'No such item exist'
    else:
      del userProductJSON[userID][productName]

  with open('userProduct.json', 'w') as file:
    json.dump(userProductJSON, file)
  
  return productName + ' has been removed'


def update_product(productUpdate):
  with open('userProduct.json', 'r') as file:
    userProductJSON = json.load(file)
    
    userID, productName, description, price = parse_request(productUpdate)

    if userID not in userProductJSON.keys():
      return 'No such user exist'
    
    if productName not in userProductJSON[userID].keys():
      return 'No such item exist'
    else:
      userProductJSON[userID][productName]['description'] = description
      userProductJSON[userID][productName]['price'] = price

  with open('userProduct.json', 'w') as file:
    json.dump(userProductJSON, file)
  
  return productName + ' has been updated'


def show_json():
  with open('userProduct.json', 'r') as file:
    userProductJSON = json.load(file)
  return userProductJSON


def parse_request(request):
  userID = request['userID']
  productName = request['productName']
  description = request['productDescription']
  price = request['productPrice']
  return userID, productName, description, price


@app.route('/add', methods=['POST'])
def add():
  data = request.get_json()
  return add_product(data)


@app.route('/remove', methods=['POST'])
def remove():
  data = request.get_json()
  return remove_product(data)


@app.route('/update', methods=['POST'])
def update():
  data = request.get_json()
  return update_product(data)


@app.route('/show', methods=['GET'])
def show():
  return show_json()


if __name__ == '__main__':
    app.run(host = 0, port = 12345)

