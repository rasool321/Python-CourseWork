data = {
    'laptopA':{'available':True,'price':23435,'color':'green'},
    'laptopB':{'available':False,'price':92354,'color':'black'},
    'laptopC':{'available':True,'price':276545,'color':'black'},
    'laptopD':{'available':False,'price':87654,'color':'green'},
    'laptopE':{'available':True,'price':73456,'color':'green'},
    'laptopF':{'available':False,'price':46545,'color':'white'}
    
}

l=list(filter(lambda i:data[i]['available'],data))
k=list(filter(lambda i:data[i]['price']>40000,data))
c =list(filter(lambda i:data[i]['color']=='black',data))
print(l,k,c)