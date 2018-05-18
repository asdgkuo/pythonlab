ages = {}
ages['bob'] = 9
ages['alice'] = 18
print(ages['bob'])  #這個會讓執行的程式中斷
#print(ages.bob)  #這樣不行
ages['bob']              # 9
#ages.bob                 # error: 'dict' object has no attribute 'bob'
ages.get('bob')          # 9
#ages['john']             # KeyError: 'john'
ages.get('john')         # None 不會讓執行的程式中斷
ages.get('john', 'N/A')  # 'N/A' 即為找不到john時要回傳的值
len(ages)                # 2
list(ages)               # ['bob', 'alice'], order may differ
'bob' in ages            # True
'john' in ages           # False

print('bob' in ages)

ages = { 'bob': 9, 'alice': 18 }
ages2 = dict({'bob': 9, 'alice': 18}) # same as ages
ages3 = dict(bob=9, alice=18)          # same as ages
ages4 = dict([('bob', 9), ('alice', 18)]) # same as ages