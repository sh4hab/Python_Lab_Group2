import io

#import PIL.Image
import requests

port=8080

ADDR = ('localhost', port)


Data = {'picname':"hel.jpg" , 'func':"Serial"} #"𝐹𝑎𝑐𝑒𝐷𝑒𝑡𝑒𝑐𝑡𝑖𝑜𝑛"
r = requests.get('http://localhost:8080',Data)
print(r.text)
print(r.content[110:-14])

with open("AS.jpg", 'wb') as f:

    f.write(r.content[110:-14])
    f.close()
print('Successfully get the file')
print(r)




