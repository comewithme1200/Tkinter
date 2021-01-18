class Vigenere_auto:
    keys = "abcdefghijklmnopqrstuvwxyz"
    key_auto = ""
    def encrypt(self,key,plaintext):
        result = ""
        self.key_auto = key+plaintext
        for i in range(len(plaintext)):
            j = (self.keys.index(self.key_auto[i]) + self.keys.index(plaintext[i])) % len(self.keys)
            result += self.keys[j]
        return result
if __name__ == '__main__':
    plaintext = input()
    key = input()
    Vigenere_auto = Vigenere_auto()
    print(Vigenere_auto.encrypt(key,plaintext))