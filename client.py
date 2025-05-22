import requests

test_request_1 = {'userID' : '101', 'productName' : 'Wallet', 'productDescription' : 'Leather wallet, made in USA', 'productPrice' : '50'}
test_request_2 = {'userID' : '102', 'productName' : 'Bowl', 'productDescription' : 'Hard Oak Wood Bowl', 'productPrice' : '10'}
test_request_3 = {'userID' : '103', 'productName' : 'Spoon', 'productDescription' : 'Stainless Steel Spoon', 'productPrice' : '5'}

test_request_4 = {'userID' : '101', 'productName' : 'Wallet', 'productDescription' : 'Hard Carbon Fiber, Anti RFID, Made in China', 'productPrice' : '100'}
test_request_5 = {'userID' : '104', 'productName' : 'Bowl', 'productDescription' : 'Hard Oak Wood Bowl', 'productPrice' : '10'}
test_request_6 = {'userID' : '103', 'productName' : 'Fork', 'productDescription' : 'Stainless Steel Fork', 'productPrice' : '5'}

def add_request(json_data):
  url = 'http://127.0.0.1:12345/add'
  response = requests.post(url, json = json_data)
  return response.text

def remove_request(json_data):
  url = 'http://127.0.0.1:12345/remove'
  response = requests.post(url, json = json_data)
  return response.text

def update_request(json_data):
  url = 'http://127.0.0.1:12345/update'
  response = requests.post(url, json = json_data)
  return response.text

def show_request():
  url = 'http://127.0.0.1:12345/show'
  response = requests.get(url)
  return response.json()

print('Add to database:')
print(add_request(test_request_1))
print(add_request(test_request_2))
print(add_request(test_request_3))

print(show_request())

print('Remove from database:')
print(remove_request(test_request_2))
print(remove_request(test_request_5))
print(remove_request(test_request_6))

print(show_request())

print('Update database:')
print(update_request(test_request_4))
print(update_request(test_request_5))
print(update_request(test_request_6))

print(show_request())