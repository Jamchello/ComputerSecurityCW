import gmpy2
import libnum
from gmpy2 import is_prime,sub, div, isqrt
#Information given in the question:
ciphertext = 18063246826823446713398078449430032593084930507409521788808416840217864673121320737373325625956435238153341254905030318704313284850916476108745171188534516950624698806166749518575172168523034912078039283985192038034882715166870855248238044709540673107074124411448815619703897569225327115541875261715475159
e = 65537
n = 480152036660377389229792245602832867751390640643177374442124623593753741994751651501531186621781800283934767859178283582432804705716500836608561741389361274582467791712615057427766902151022593193252623808574501073302093601549164906199493090011494422332162638158149273853866019812952706699448349682015745257
#Using gmpy2 sqrt function because the built in python function doesnt work correctly for such large integers.
root = int(isqrt(n))
#Set p and q to 0 so the condition later will only hold true if a value for p and q are found.
p=0
q=0
#Iterate through each possible p in the range, if it is a factor check if both p and q are primes.
for i in range(root-10000,root+10000):
    if n%i == 0:
        p = i
        q = int(div(n,p))
        if is_prime(p) and is_prime(q):
            print("Prime factors Found!")
            print(f"p:{p}")
            print(f"q:{q}")
            print(f"n:{n}")
            break
#p and q are now known - reverse engineering the value of the secret key, d:
if p and q:
    phi = (p-1)*(q-1)
    d=(libnum.invmod(e, phi))
    plaintext=pow(ciphertext,d,n)
    print(f"d: {d}")
    print(f"Decrypted text is: {plaintext}")