toEncrypt = input("Enter What to Encrypt: ")
passwordFile = open("password.txt","w+")

toEncrypt.lower()

def shift(input):
    fullShift = 0
    shifts = 0
    for i in input:
        fullShift += ord(i) + shifts
        shifts += 1
    return fullShift

def key1(input):
    return len(input)

def caesar(word, key, shifts): #Function to code a text with caeser chyper.
    for x in range(shifts):
        word.lower()
        encryptedstring = ""
        for i in word:
            charvalue = ord(i) + key
            if ( charvalue > 122):
                charvalue = ord('a') + (charvalue -123)
                encryptedstring += str(chr(int(charvalue)))
            else:
                encryptedstring += chr(int(charvalue))
    return encryptedstring

def key2(word):
    tempKey = []
    for i in word:
        tempKey.append(ord(i))
    tempKey.sort()
    data_length_2 = len(tempKey)
    if data_length_2 >= 6:
        tempKey.remove(tempKey[data_length_2 - 1])
        tempKey.remove(tempKey[0])
        data_length_2 -= 2
        tempKey.sort()
    while data_length_2 >= 1:
        for x in tempKey:
            data_length = int(len(tempKey))
            while data_length >= 1:
                index = data_length - 1
                number_one = tempKey[index]
                number_two = tempKey[index - 1]
                difference = abs(number_one - number_two)
                tempKey.sort()
                if difference >= 0.1:
                    number_average = (number_one + number_two) / 2
                    data_length -= 1
                    tempKey.remove(number_one)
                    tempKey.remove(number_two)
                    tempKey.append(number_average)
                    tempKey.sort()
                data_length -= 1
                tempKey.sort()
        data_length_2 -= 1
        tempKey.sort()
        result = tempKey[0] // 1
    return result

def replacments(word, key, shifts):
    array = []
    sum = 0
    keyNoDec = round(key,0)
    strKey = str(keyNoDec)
    for i in strKey:
        array.append(i)
    for x in array:
        if x != ".":
            sum += float(x)
    average = sum / len(array)
    number = round((average*10),0)
    return caesar(word, number, shifts)

def makeNumKey(input):
    final = 0
    for letter in input:
        final += ord(letter)
    return final

numKey = makeNumKey(toEncrypt)

def encryptor(phrase):
    phrase.lower()
    times = 0
    result = ""
    for letter in phrase:
        times += numKey
        result += chr((ord(letter) + times - 97) % 26 + 97)
    return result

final = encryptor(encryptor(encryptor(replacments( caesar(encryptor(toEncrypt), key1(encryptor(toEncrypt)), shift(encryptor(toEncrypt))), key2(encryptor(toEncrypt)), shift(encryptor(toEncrypt))))))
print(final)
passwordFile.write(final)
passwordFile.close()