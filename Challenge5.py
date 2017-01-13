//Implement repeating-key XOR
//Here is the opening stanza of an important work of the English language:
//Burning 'em, if you ain't quick and nimble
//I go crazy when I hear a cymbal
//Encrypt it, under the key "ICE", using repeating-key XOR.
//In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.
//It should come out to:

//0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
//a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f


def repXOR(str):
        key = "ICE"
        r = ""
        x=0
        for c in str:
                if x == len(key):
                        x=0
                r += chr(ord(c)^ord(key[x]))
                x+=1
        print r.encode("hex")


str = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
str = str.split("\n")
for x in range(len(str)):
        repXOR(str[x].strip()
        
// output:
// 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f2043
// 0a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

// The strings are not equal to what the they should be according to the challenge.
// a282b2f2043 in the end of the first string should be in the beginning of the second string, but if you put them together they are equal

// 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
// a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

// The script below doesn't care about any newline

def repXOR(str):
        key = "ICE"
        r = ""
        x = 0
        for c in str:
                if x == len(key):
                        x = 0
                r += chr(ord(c)^ord(key[x]))
                x += 1
        return r.encode("hex")


str = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
print repXOR(str)

// output:
// 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
// Which is identical with the strings from the challenge when put together
// 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
