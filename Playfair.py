class Playfair:
    keys = "abcdefghiklmnopqrstuvwxyz"
    def makematrix(self,key):
        str = self.keys
        for x in key:
            str = str.replace(x, "")
        D = {}
        str1 = ""
        for x in key:
            if x not in D.keys():
                str1 += x
                D[x] = True
        str = str1 + str
        return str
    def replacement(self, plaintext):
        for x in plaintext:
            if x == "j":
                plaintext = plaintext.replace(x, "i")
        return plaintext
    def cuttext(self,plaintext):
        textcutted = ''
        tempstr = ''
        i = 0
        while i < len(plaintext):
            if  i == len(plaintext)-1:
                tempstr = plaintext[i] + 'x'
                textcutted += tempstr
                i += 1
            elif plaintext[i] == plaintext[i+1]:
                tempstr = plaintext[i] + 'x'
                textcutted += tempstr
                i += 1
            elif plaintext[i] != plaintext[i+1]:
                tempstr = plaintext[i] + plaintext[i+1]
                textcutted += tempstr
                i += 2
            #textcutted += " "
        return textcutted

    def encrypt(self,matrix,textcutted):
        np1 = 0 #natural part
        np2 = 0
        rmd1 = 0 #remainder
        rmd2 = 0
        result = ""
        for i in range(0,len(textcutted),2):
            if int(matrix.index(textcutted[i+1])/5) == int(matrix.index(textcutted[i])/5):
                #print(matrix.index(textcutted[i + 1]), end=" ")
                #print(matrix.index(textcutted[i]))
                if matrix.index(textcutted[i + 1]) % 5 == 4:
                    result += matrix[matrix.index(textcutted[i]) + 1] + matrix[matrix.index(textcutted[i+1]) -4]
                else:
                    result += matrix[matrix.index(textcutted[i])+1] + matrix[matrix.index(textcutted[i+1])+1]
            elif matrix.index(textcutted[i+1]) % 5 == matrix.index(textcutted[i]) % 5:
                if int(matrix.index(textcutted[i + 1]) / 5) == 4:
                    result += matrix[matrix.index(textcutted[i]) + 5] + matrix[matrix.index(textcutted[i+1])%5]
                else:
                    result += matrix[matrix.index(textcutted[i])+5] + matrix[matrix.index(textcutted[i+1])+5]
            elif int(matrix.index(textcutted[i+1])/5) != int(matrix.index(textcutted[i])/5):
                np1 = int(matrix.index(textcutted[i])/5)
                np2 = int(matrix.index(textcutted[i+1])/5)
                #if np2>np1:
                result += matrix[matrix.index(textcutted[i+1])-(np2-np1)*5] + matrix[matrix.index(textcutted[i])+(np2-np1)*5]
                #elif np1>np2:
                    #result += matrix[matrix.index(textcutted[i + 1]) - (np1 - np2) * 5] + matrix[matrix.index(textcutted[i]) + (np1 - np2) * 5]
        return result

if __name__ == '__main__':
    plaintext=input()
    key=input()
    Playfair = Playfair()
    plaintext = Playfair.replacement(plaintext)
    matrix = Playfair.makematrix(key)
    print(Playfair.makematrix(key))
    print(Playfair.cuttext(plaintext))
    print(Playfair.encrypt(matrix, Playfair.cuttext(plaintext)))
