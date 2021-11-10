TRANSLATE = []
def L_Data() :
    with open("translate.txt" , 'r') as f: 
        b_text = f.read()
        words = b_text.split('\n')
    for i in range(0, len(words), 2) :  
        TRANSLATE.append({'english' : words[i] , 'farsi' : words[i+1]})       
def S_New_Data():
    n_word= []
    continue_choice = 1
    while continue_choice :
        n_word.append(input('type english sentence'))
        n_word.append(input('type farsi translate ')) 
        with open("translate.txt" , 'a') as f:
            f.write('\n' + n_word[0] + '\n' + n_word[1])
        n_word.clear()        
        continue_choice= input('if you like to add extra word yes elif no ')
        if continue_choice == 'No':
            continue_choice= 0  
def Translate_En2fa():
    input_text= input('please type your text: ')
    user_words= input_text.split(' ')
    output_text= ' '
    for user_word in user_words:
        for word in TRANSLATE:
            if user_word == word['english']:
                output_text += word['farsi'] + ' '
                break
        else:
            output_text += user_word + ' '
    print(output_text)     
def Translate_Fa2en():
    input_text= input('please type your text: ')
    user_words= input_text.split(' ')
    output_text= ''
    for user_word in user_words:
        for word in TRANSLATE:
            if user_word == word['farsi']:
                output_text += word['english'] + ' '
                break
        else:
            output_text += user_word + ' '
    print(output_text)    
def Show_menu():
    print('1. English to farsi')
    print('2. Persian to English')
    print('3.Add new words')
    print('4.exit')    
L_Data()        
while True:
    Show_menu()
    choice= input('enter a number')
    if choice == '1' : 
        Translate_En2fa()
    elif choice == '2': 
        Translate_Fa2en()
    elif choice == '3' : 
        S_New_Data()
    elif choice == '4': 
        break
    else:
        print('Eroor!')
        print("bye")