
import json
tt = open('b.json')
ttt = '''{"order_external_id":["主訂單編號"],
 "order_status":["狀態"],
 "order_date":["訂單日期"],
 "product_external_id":["SKU"],
 "client_external_id":[["收件者電話","信箱"]],
 "others":["單價"]}'''
json.loads(ttt)