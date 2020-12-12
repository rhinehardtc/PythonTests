#%%
msg = "hello world"

print("peepee", msg.split())

w = 2
h = 2

print((w+h) ** w)

print(r'C:\some\name') #use r to escape special char after \

print(3 * 'squeewoo weewoo ') #can multiple number of times a string is created

s = 'This is a string, bro'
print(len(s)) #len() is the Py length

a, b = 0, 1
while a < 30:
    print(a)
    a, b = b, a+b

def tetrate(n):
    print(n ** n)  

tetrate(3)
# %%
