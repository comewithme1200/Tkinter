class singlechar:
    keys = "abcdefghijklmnopqrstuvwxyz"
    def encrypt(self,key,plaintext):
        result = ""
        for l in plaintext:
            result += key[self.keys.index(l)]
        return result
if __name__ == '__main__':
    plaintext = input()
    key = input()
    singlechar = singlechar()
    print(singlechar.encrypt(key, plaintext))
