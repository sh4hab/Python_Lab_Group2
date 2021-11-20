# -*- coding: utf-8 -*-

nation = ['Roman','Egypt','Greek','Chinese','Islamic','Mayan','Persian','Mongol']
golden_age = ['27BC-1453AD','3150BC-30BC','800BC-600AD','221BC-1912AD','750AD-1257AD','2000BC-1540AD','550BC-651AD','1206AD-1368AD']

a=zip(nation,golden_age)
print(type(a))
dictionary=dict(a)
print("access to value: "+dictionary['Roman'])
print("access to key by value: "+list(dictionary.keys())[list(dictionary.values()).index('800BC-600AD')])
print("key set: "+ str(list(dictionary.keys())))
print("value set: "+ str(list(dictionary.values())))

"""
a = [2**i for i in range (17)]
b = [x*x for x in range (1,5)]
c = [a[x] for x in b if x % 2 == 0]
"""