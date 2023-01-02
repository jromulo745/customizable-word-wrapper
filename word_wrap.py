
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
MODULE: word wrapper
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def space_value():
    word_wrap_value = 0
    print()
    print("\t1 - 165")
    print("\t2 - 100")
    num_input = int(input("\n\tSelect a choice (1 - 2): "))
    if num_input == 1:
        return 165
    elif num_input == 2:
        return 100

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def line_printer(num):
    string = ""
    if num == 165:
        string = "\n\t--------------------------------------------------------------------------------------------------------\
-------------------------------------------------------"
    elif num == 100:
        string = "\n\t--------------------------------------------------------------------------------------------------------"
    return string

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def word_wrap(string, value):
    counter = 0
    word = ''
    list = []
    for letter in (string + ' '):
        if counter == value:
                
            if letter == ' ':
                list.append(word + ' ')
                word = '' #reset
                
            if counter != len(string):
                list.append('\n\n\t')
            word += letter
            counter = len(word)
        elif letter == ' ':
            word += letter
            list.append(word)
            word = '' #reset
            counter += 1
        else:
            word += letter
            counter += 1
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    counter = 0 #recycled variable
    new_word = ''
    for word in list:
        if counter == len(list) - 1:
            if word[0] == ' ':
                new_word += word[1:-1]
            else:
                new_word += word[:-1]
        elif word[0] == ' ':
            new_word += word[1:]
        else:
            new_word += word
        counter += 1

    return new_word

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def word_wrap_single_space(string, value):
    counter = 0
    word = ''
    list = []
    for letter in (string + ' '):
        if counter == value:
            if letter == ' ':
                list.append(word + ' ')
                word = '' #reset
            
            list.append('\n\t')
            word += letter
            counter = len(word)
        elif letter == ' ':
            word += letter
            list.append(word)
            word = '' #reset
            counter += 1
        else:
            word += letter
            counter += 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    counter = 0 #recycled variable
    new_word = ''
    for word in list:
        if counter == len(list) - 1:
            if word[0] == ' ':
                new_word += word[1:-1]
            else:
                new_word += word[:-1]
        elif word[0] == ' ':
            new_word += word[1:]
        else:
            new_word += word
        counter += 1

    return new_word
