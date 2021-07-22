def isPalindrome(textIn):
    text = [char for char in textIn.lower()]
    for i in range(len(text)):
        start = i
        end = len(text) - i - 1
        if(text[start] != text[end]):
            return "False"
    return "True"


def test_IsPalindrome():
    print(isPalindrome('KoDok'))
    print(isPalindrome('kasur'))
    print(isPalindrome('iBu'))


test_IsPalindrome()
