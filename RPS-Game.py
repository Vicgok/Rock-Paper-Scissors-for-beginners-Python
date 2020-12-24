from random import randint

Equip = ['Rock', 'Paper', 'Scissors']
HoomanPoints = 0
BotPoints = 0

PlayAgain = 'Y'

while PlayAgain.upper() == 'Y':

    Bot = Equip[randint(0,2)]

    Hooman = input('Rock, Paper, Scissor ?\n').capitalize()

    if Hooman == Bot:
        print('Omai Gawd it\'s a Draw')

    elif Hooman == 'Rock':
        if Bot == 'Paper':
            BotPoints+=1
            PlayAgain = input('You lost to a bot RIP XD\nBot_Points= ' + str(BotPoints) + '\nYour_Points= '+ str(HoomanPoints) + '\nWanna try again?(Y/N)')
            if PlayAgain.upper() == 'N':
                break
        else:
            HoomanPoints+=1
            PlayAgain = input('Woah you won amgioo\nBot_Points= ' + str(BotPoints) + '\nYour_Points= '+ str(HoomanPoints) + '\n Wanna try again?(Y/N)')
            if PlayAgain.upper() == 'N':
                break
    
    elif Hooman == 'Paper':
        if Bot == 'Scissor':
            BotPoints+=1
            PlayAgain = input('You lost to a bot RIP XD\nBot_Points= ' + str(BotPoints) + '\nYour_Points= '+ str(HoomanPoints) + '\nWanna try again?(Y/N)')
            if PlayAgain.upper() == 'N':
                break
        else:
            HoomanPoints+=1
            PlayAgain = input('Woah you won amgioo\nBot_Points= ' + str(BotPoints) + '\nYour_Points= '+ str(HoomanPoints) + '\n Wanna try again?(Y/N)')
            if PlayAgain.upper() == 'N':
                break

    elif Hooman == 'Scissor':
        if Bot == 'Rock':
            BotPoints+=1
            PlayAgain = input('You lost to a bot RIP XD\nBot_Points= ' + str(BotPoints) + '\nYour_Points= '+ str(HoomanPoints) + '\nWanna try again?(Y/N)')
            if PlayAgain.upper() == 'N':
                break
        else:
            HoomanPoints+=1
            PlayAgain = input('Woah you won amgioo\nBot_Points= ' + str(BotPoints) + '\nYour_Points= '+ str(HoomanPoints) + '\n Wanna try again?(Y/N)')
            if PlayAgain.upper() == 'N':
                break


