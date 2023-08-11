str="hello"
print(str);

#accessing the chracter in string
str="hello"
print(str[0])
print(str[2])


#to delete character
str="hello"
print(str)
str1=str[0:2]+str[3:0]
print(str)
#to delete string
str="hello"
print(str)
del str
print(str)

#string character updation
original_string ="hello"
"""replace charater  is w ,and it is present at the 2nd index so storing its index """
index =5

#'p' is replace 'w'
new_character ="p"
original_string = original_string[:index]+new_character + original_string[index]
print(original_string)


                                                                    
