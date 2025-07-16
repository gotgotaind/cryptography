from Cryptodome.Cipher import AES

k1=bytes.fromhex("140b41b22a29beb4061bda66b6747e14")
c1=bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
iv=c1[0:15]
print("".join(list(map(hex,iv))))
c1=c1[16:]
print("".join(list(map(hex,c1))))


cipher = AES.new(k1, AES.MODE_CBC)

plaintext = cipher.decrypt(c1)

try:
#    cipher.verify(tag)
    print("The message is authentic:", plaintext)
except ValueError:
    print("Key incorrect or message corrupted")
