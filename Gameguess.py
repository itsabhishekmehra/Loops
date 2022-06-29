# i=0
# while i<=5:
#     a=int(input('Guess the number: '))
#     i+=1
#     if a==5:
#         print('Wow you guessed the correct number')
#         break
#     elif a>5:
#         print('Number entered by you is greater, try one more time ')
#     else:
#         print('Number entered by you is small, try one more time ')


i=0
while i<=5:
    a=int(input('Guess the number: '))
    i+=1
    if a==5:
        print('You WON!')
        break
    else:
        print('Guess Again')