//Write a function that takes two equal-length buffers and produces their XOR combination.
//If your function works properly, then when you feed it the string:
//1c0111001f010100061a024b53535009181c
//... after hex decoding, and when XOR'd against:
//686974207468652062756c6c277320657965
//... should produce:
//746865206b696420646f6e277420706c6179

import sys
def fixedXOR(x,y):
    if len(x) != len(y):
        sys.exit("buffers must be equal")
    r = ""
    x = x.decode("hex")
    y = y.decode("hex")
    for i in range(len(x)):
        r += (chr(ord(x[i]) ^ ord(y[i])))
    print r.encode("hex")
   
fixedXOR("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")
