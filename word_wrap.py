
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
MODULE: word wrapper
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def word_wrap(string):
    counter = 0
    word = ''
    list = []
    for letter in (string + ' '):
        if counter == 165:
                
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

def word_wrap_single_space(string):
    counter = 0
    word = ''
    list = []
    for letter in (string + ' '):
        if counter == 165:
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
