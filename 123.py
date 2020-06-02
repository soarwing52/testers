
import json
tt = open('b.json')
ttt = '''{"order_external_id":["訂單編號"],
 "order_status":[],
 "order_date":["訂購日期"],
 "product_external_id":[["店家料號", "商品編號"]],
 "client_external_id":["訂購人"],
 "others":["數量", "金額小計", "訂單編號""]}'''
json.loads(ttt)