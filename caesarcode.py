class Caesar:
    key = "abcdefghijklmnopqrstuvwxyz"
    def encrypt(self, k, plaintext):
        result = ""
        for l in plaintext:
            i = (self.key.index(l) + k) % len(self.key)
            result += self.key[i]
        return result
    def decrypt(self,k,ciphertext):
        result = ""
        for l in ciphertext:
            i = (self.key.index(l) - k) % len(self.key)
            result += self.key[i]
        return result
if __name__ == '__main__':
    Caesar = Caesar()
    plaintext=input()
    k = int(input())
    print(Caesar.encrypt(k, plaintext))
    print(Caesar.decrypt(k,Caesar.encrypt(k, plaintext)))
