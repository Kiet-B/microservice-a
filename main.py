import json


def add_product(new_product):
  with open("userProduct.json") as file:
    userProductJSON = json.load(file)
    if new_product["userID"] not in userProductJSON.keys():
      userProductJSON[new_product["userID"]] = {
        new_product["productName"] : {"description" : new_product["productDescription"], "price" : new_product["productPrice"]}
      }
    

def test():
  with open("userProduct.json", "r") as file:
    data = json.load(file)
  print(type(data))
  return None

def main():
  test_request = {"userID" : "102", "productName" : "Wallet", "productDescription" : "Leather wallet, made in USA", "productPricetest" : "50"}
  add_product(test_request)


if __name__ == "__main__":
  main()