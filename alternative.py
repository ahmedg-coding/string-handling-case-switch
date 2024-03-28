#The following program has two functions, the first reads in a string and switches each alternate
#character into an upper case character and each other alternate character into a lower case. 
#The second function switches each alternative word to a lower and upper case.

#First function definition for switching the case of characters
def switch_character_case(char_switch_example):
    output = '' #Variable 'output' initialization
    
    #Creating a for loop which will loop through every single character within the string
    for i in range(len(char_switch_example)):
        #if block
        if i % 2 == 0:
            output += char_switch_example[i].upper()
        #else block
        else:
            output += char_switch_example[i].lower()
    
    return output

#Second function definition for switching the case of words
def switch_word_case(word_switch_example):
    word_list = word_switch_example.split() #Using split() function 
    output = []
    
    #Creating a for loop which will loop through every single word within the string
    for i in range(len(word_list)):
        #if block
        if i % 2 != 0:
            output.append(word_list[i].upper())
        #else block
        else:
            output.append(word_list[i].lower())
    
    return ' '.join(output) #Using join() function

#Example to demonstrate switching the case of characters 
char_switch_example = "Hello World"
character_result = switch_character_case(char_switch_example)
print(character_result)

#Example to demonstrate switching the case of words 
word_switch_example = "I am learning to code"
word_result = switch_word_case(word_switch_example)
print(word_result)
