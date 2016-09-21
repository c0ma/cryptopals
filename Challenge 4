
//Detect single-character XOR
//One of the 60-character strings in this file has been encrypted by single-character XOR.
//Find it.
//(Your code from #3 should help.)

import string
import re
def bruteforce(key):
        file = open("4.txt",'r')
        for line in file:
                line = line.strip()
                line = line.decode("hex")

                r = ""
                for x in range(len(line)):
                        r += chr( ord(key) ^ ord(line[x]))

                if re.findall("[a-zA-Z ]",r)==list(r.strip()):
                        print r
                        print "key is ",key
                        return 1

keys = string.printable
keys = keys.strip()
for key in keys:
        s=bruteforce(key)
        if s == 1:
                break
                
// Now that the party is jumping                
// key is  5              
