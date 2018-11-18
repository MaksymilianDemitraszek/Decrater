import base64, json
jsont = 'WzEsIDIsIDNd'
decoded_list = base64.b64decode(jsont)
print(json.loads(decoded_list))