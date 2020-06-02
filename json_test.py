import json
a = open('a.json')
b = json.load(a)
#print(b, type(b))
header = ['序號', '訂單編號', '轉單日', '最晚出貨日', '收件人姓名', '收件人電話(日)', '收件人電話(夜)',
 '收件人手機', '收件人地址', '商品名稱', '商品屬性', '數量', '商品成本', '成本小計', '購物車備註', '活動序號',
  '訂單狀態', '供應商料號', '合併序號']

must = []
for x in b:
    print(x,b[x])
    requirements = b[x]

    for target in requirements:
        if isinstance(target,list):
            requirements.remove(target)
            print(set(target).intersection(header))
        else:
            must.append(requirements)
print(must)
for x in must:
    print(x,type(x))
# str_source = '狀態,訂單日期,主訂單編號,SKU,[收件者電話,信箱],單價'
# str_source = str_source.split(',')

# for x in str_source:
#     print(x,type(x))
# print(str_source)



# missing = list(set(requirements) - set(header))
# print(missing) 
