def replace_word():

    str = input('Enter a sentence of your choice : ')
    word_to_replace = input('Enter the word you wish to replace : ')
    word_replacement = input('Enter the word replacement : ')
    print(f'The sentence you entered is {str}')
    if word_to_replace in str:
        replaced_str = str.replace(word_to_replace, word_replacement)
        print(f'The modified sentence is : {replaced_str}')
    else:
        print('This word is not present in the sentence you entered !')


replace_word()