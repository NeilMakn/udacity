# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(letter,n):
    result = ''
    for char in letter:
        if char != ' ':
            result += shift_letter(char,n)
        else:
            result += ' '
    return result


def shift_letter(letter, n):
    offset = ord(letter) - ord('a')
    shifted = offset + n
    result = shifted % 26
    return chr(result + ord('a'))



print shift_letter('a',3)
# #'d'
print rotate('sarah', 13)
# #>>> 'fnenu'
print rotate('fnenu',13)
# #>>> 'sarah'
print rotate('dave',5)
# #>>>'ifaj'
print rotate('ifaj',-5)
# #>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???