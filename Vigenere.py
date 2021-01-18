class Vigenere:
    keys = "abcdefghijklmnopqrstuvwxyz"
    key_repeat = ""
    def encrypt(self,key,plaintext):
        result = ""
        for i in range(len(plaintext)):
            self.key_repeat += key[i % len(key)]
        for i in range(len(plaintext)):
            j = (self.keys.index(self.key_repeat[i]) + self.keys.index(plaintext[i])) % len(self.keys)
            result += self.keys[j]
        return result
if __name__ == '__main__':
    plaintext = input()
    key = input()
    Vigenere = Vigenere()
    print(Vigenere.encrypt(key , plaintext))
