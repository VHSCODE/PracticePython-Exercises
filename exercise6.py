string = str(input("Enter a word: "))


def palindrome(word):
    if word == word[::-1]:
        print("the word is a palindrome")
    else:
        print("The word is not a palindrome")
    

palindrome(string)