
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
MODULE: word wrapper
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#MAX 158 (minus 8 --> 150)

def word_wrap(string):
    #mirror = string + ' ' #new
    #index = 0 #new
    counter = 0
    word = ''
    list = []
    #while (index < len(mirror)): #new
        #letter = mirror[index] #new
    for letter in (string + ' '):
        if counter == 165:
            #print(word + ': ' + str(counter)) #debugging
            #debugging
            #if letter == ' ':
            #    print('here')
            #else:
            #    print(letter)
                
            if letter == ' ':
                list.append(word + ' ')
                word = '' #reset
                
            if counter != len(string):
                list.append('\n\n\t')
            word += letter
            #counter = 0 #reset letter counter
            counter = len(word)
        elif letter == ' ':
            word += letter
            list.append(word)
            word = '' #reset
            counter += 1
        else:
            word += letter
            counter += 1
        #index += 1 #new
    
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
    #return new_word[:-1]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def word_wrap_single_space(string):
    #mirror = string + ' ' #new
    #index = 0 #new
    counter = 0
    word = ''
    list = []
    #while (index < len(mirror)): #new
        #letter = mirror[index] #new
    for letter in (string + ' '):
        if counter == 165:
            #print(word + ': ' + str(counter)) #debugging
            #debugging
            #if letter == ' ':
            #    print('here')
            #else:
            #    print(letter)
                
            if letter == ' ':
                list.append(word + ' ')
                word = '' #reset
            
            list.append('\n\t')
            word += letter
            #counter = 0 #reset letter counter
            counter = len(word)
        elif letter == ' ':
            word += letter
            list.append(word)
            word = '' #reset
            counter += 1
        else:
            word += letter
            counter += 1
        #index += 1 #new

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
    #return new_word[:-1]
