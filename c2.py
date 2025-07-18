try:
    from Cryptodome.Cipher import AES
except ImportError:
    from Crypto.Cipher import AES

k=list()
c=list()
k.append(bytes.fromhex("140b41b22a29beb4061bda66b6747e14"))
c.append(bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"))
k.append(bytes.fromhex("140b41b22a29beb4061bda66b6747e14"))
c.append(bytes.fromhex("5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"))
k.append(bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2"))
c.append(bytes.fromhex("69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"))
k.append(bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2"))
c.append(bytes.fromhex("770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"))



def decr(k,c,mode):
    
    if(mode==AES.MODE_CBC):
        iv=c[0:16]
        print("".join(list(map(hex,iv))))
        c1=c[16:]
        print("".join(list(map(hex,c1))))
        cipher = AES.new(k, mode,iv=iv)
    else:
        iv=c[0:8]
        print("".join(list(map(hex,iv))))
        counter=c[8:16]
        c1=c[16:]
        print("".join(list(map(hex,c1))))
        cipher = AES.new(k, mode,nonce=iv,counter=counter)

    
    plaintext = cipher.decrypt(c1)
    #print("The message is authentic:", plaintext.decode("cp437"))
    #print("The message is authentic:", plaintext.decode("utf-8"))
    print("The message is authentic:", plaintext)


for i in range(len(k)):
    print(len(k[i]))

for i in range(len(k)):
    if(i<2):
        mode=AES.MODE_CBC
    else:
        mode=AES.MODE_CTR
    decr(k[i],c[i],mode)
