import requests

bin_id ="67458cbbacd3cb34a8af0bc0"
XMasterKey = "$2a$10$w5ey/n1H8M6JGQ32tfSu3ubMi0V8h2YZedNvBSnLni.9.EacCVj7."
XAccessKey = "$2a$10$KZ4.0TXrOwe.aigZNPIgqObco0HECBjlXz2Pu8.ILxrRAjU5l4x42"
url_root ="https://api.jsonbin.io/v3"
route = f"/b/{bin_id}"
headers = {
    "X-Master-Key": XMasterKey,
    "X-Access-Key": XAccessKey
}

r = requests.get(url_root + route, headers=headers)
print(r.json())
