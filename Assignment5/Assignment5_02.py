

def CheckVowel(ch):
    
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E'or ch == 'I' or ch == 'O' or ch == 'U':
        return True
    else:
        return False


def main():
    print("enter the character : ")
    cValue = input()

    bRet = CheckVowel(cValue)

    if bRet == True:
        print("Its vowel")
    else:
        print("Its not a Vowel")


if __name__ == "__main__":
    main()