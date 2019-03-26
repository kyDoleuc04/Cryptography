"""
cryptography.py
Author: kyDoleuc04
Credit: Matt, Andrew, Google, Youtube

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

help = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
a == "yes"
num=0

while a == "yes":
    if b == "e":
        msg=input("Message: ")
        msglist=list(msg)
        key=input("Key: ")
        keylist=list(key)
        nummsg=[]
        msglength=len(msglist)
        for char in msglist:
            nummsg.append(associations.find(char))
        keystr = key
        keylength=len(keystr)
        while keylength<msglength:
            keystr=keystr+key
            keylength=len(keystr)
        while keylength>msglength:
            keystr=keystr[:-1]
            keylength=len(keystr)
        numkey = []
        for char in keystr:
            numkey.append(associations.find(char))
        num=0
        listsum=[]
        while num<msglength:
            sumlist.append(nummsg[num]+numkey[num])
            num+=1
        num=0
        while num<msglength:
            if sumlist[num]>84:
                sumlist[num]-=85
            num+=1
        num=0
        endlist=[]
                while num<msglength:
            endlist.append(associations[listsum[num]])
            num+=1
        print(''.join(endlist))
        num=0
        
        redo = 'yes'
    
        
        
    