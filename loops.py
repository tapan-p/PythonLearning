for name in ['firstname','secondname']:
    print(name)
    
print('for loop with pass')
names=['n1','n2','n3']
for name in names:
    if name=='n2':
        continue
    print(name)
#starting number, ending number
for index in range(0,5):
    print(index)

print('while loop')
index =0
while index<5:
    print(index)
    index=index+1