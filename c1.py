import sys

MSGS = ( '' )
ciphers= (
"315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e",
"234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f",
"32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb",
"32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa",
"3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070",
"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4",
"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce",
"315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3",
"271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027",
"466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83",
"32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
)

char_dist=dict()
char_dist['E']=529117365
char_dist['T']=390965105
char_dist['A']=374061888
char_dist['O']=326627740
char_dist['I']=320410057
char_dist['N']=313720540
char_dist['S']=294300210
char_dist['R']=277000841
char_dist['H']=216768975
char_dist['L']=183996130
char_dist['D']=169330528
char_dist['C']=138416451
char_dist['U']=117295780
char_dist['M']=110504544
char_dist['F']=95422055
char_dist['G']=91258980
char_dist['P']=90376747
char_dist['W']=79843664
char_dist['Y']=75294515
char_dist['B']=70195826
char_dist['V']=46337161
char_dist['K']=35373464
char_dist['J']=9613410
char_dist['X']=8369915
char_dist['Z']=4975847
char_dist['Q']=4550166
char_dist[' ']=4000000
char_dist[')']=4000000
char_dist['(']=4000000
char_dist['-']=4000000
char_dist['\'']=4000000
char_dist['.']=4000000
char_dist[',']=4000000
char_dist[':']=4000000

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print(c.encode('hex'))
    return c

def crypt():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

def main():
    print("Hello!")

    ba_cip_list=[]

    for cip in ciphers :
        a=bytearray.fromhex(cip)
        ba_cip_list.append(a)
        for c in a:
            print(hex(c),end=',')
        print()
    max_len=0
    for cip in ba_cip_list:
        l=len(cip)
        print(l)
        if( l>max_len ):
            max_len=l
    print(f'{max_len=}')


    common_list=[]
    for i,cip in enumerate(ba_cip_list):
        for j,cip2 in enumerate(ba_cip_list):
            if(i != j):
                c=bytearray()
                for k in range(max(len(cip),len(cip2))):
                    if(cip[k]==cip2[k]):
                        c.append(cip[k])
                    else:
                        d=dict()
                        d['ba']=c
                        d['len']=len(c)
                        new=True
                        for dd in common_list:
                            if(dd['ba'] == d['ba']):
                                new=False
                                dd['freq']=dd['freq']+1
                                break
                        if new:
                            d['freq']=1
                            common_list.append(d)
                        break
    for c in common_list:
        zz=c["ba"].hex(' ').upper()
        print(f'{zz=},{c["freq"]=},{c["len"]=}')

    secret_len=len(ba_cip_list[-1])
    key=[-1 for element in range(secret_len)]

    forced_key=dict()

    key[0]=(ord("T")^0x32)
    forced_key[0]=key[0]
    key[1]=(ord("h")^0x51)
    forced_key[1]=key[1]
    key[2]=(ord("e")^0xb)
    forced_key[2]=key[2]
    key[10]=ord('t')^0x41
    forced_key[10]=key[10]
    key[21]=ord('c')^0x1c
    forced_key[21]=key[21]
    key[26]=ord('n')^0x05
    forced_key[26]=key[26]
    key[32]=ord('g')^0x0e
    forced_key[32]=key[32]
    key[39]=ord('e')^0x25
    forced_key[39]=key[39]
    key[40]=ord('a')^0x7b
    forced_key[40]=key[40]
    key[41]=ord('m')^0xf1
    forced_key[41]=key[41]

#    kkey=ord("T")^0x32


    for cip in (ba_cip_list):
        i=39
        print((cip[i]^key[i]),end='')
        print()
    print("Done.")

#    exit()


    good_keys=list()
    for i in range(len(ba_cip_list[-1])):
        good_keys.append(list())
        for key in range(256):
            good_key=True
            for cip in ba_cip_list:
                t=cip[i]^key
                if( not ( ((t>=65) and (t<=90)) or ((t>=97) and (t<=122)) or t==32 or t==40 or t==41 or t==45 or t==39 or t==44 or t==46 or t==58 or t==63 or t==53 or t==48 or t==42 or(t>=48 and t<=57)) ):
                #if( not ( ((t>=97) and (t<=122)) or t==32 ) ):
                #if( not ( ((t>=32) and (t<=122)) ) ):
                    good_key=False
            if good_key:
                good_keys[i].append(key)
    for key in good_keys:
        print(len(key))

    
    best_keys=[-1 for element in range(secret_len)]

    for i in range(secret_len):
        best_score=0
        for key in good_keys[i]:
            score=0
            for cip in (ba_cip_list):
                CHAR=chr(cip[i]^key).upper() 
                if(CHAR in char_dist.keys()):
                    score=score+char_dist[CHAR]
                else:
                    score=score+4000000
            if score > best_score:
                best_score=score
                best_keys[i]=key

    print(good_keys[0])
    print(best_keys[0])


    print()
    print('xx',end='')
    for i in range(secret_len):
        print(f"{i:02d}",end='')
    print()
    for j,cip in enumerate(ba_cip_list):
        print(f"{j:02d}",end='')
        for i in range(secret_len):
            print(f"{cip[i]:02x}",end='')
        print()

    print()


    print('xx',end='')
    for i in range(secret_len):
        print(f"{i:02d}",end='')
    print()
    for j,cip in enumerate(ba_cip_list):
        print(f"{j:02d}",end='')
        for i in range(secret_len):
        #for i in range(1):
            if( i in forced_key.keys() ):
                best_keys[i]=forced_key[i]

            if( best_keys[i]!=-1 ):
                print(chr(cip[i]^best_keys[i]),end='')
                print(' ',end='')
            else:
                print('x',end='')
                print(' ',end='')
        print()

    cip=ba_cip_list[-1]
    for i in range(secret_len):
        if( i in forced_key.keys() ):
            best_keys[i]=forced_key[i]

        if( best_keys[i]!=-1 ):
            print(chr(cip[i]^best_keys[i]),end='')
            #print(f"{cip[i]:02x}")
        else:
            print('x',end='')
    print()



main()
