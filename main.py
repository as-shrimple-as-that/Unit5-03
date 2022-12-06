from random import shuffle
from time import sleep

while True:
  ynAgain = str('y')
  Launch = str(input('Which program do you want to launch? (Q1, Q2) \n'))
  CAs = 0
  
  if Launch == str('Q1'):
    while True:
      Q1 = str(input('What do you want to name your file? \n') + ".txt")
      fileName = str(Q1 )
      print(Q1)
      Q2 = str(input('What is your question? \n') + '\n')
      A1 = str(input('What is your first answer? \n') + '\n')
      A2 = str(input('What is your second answer? \n') + '\n')
      A3 = str(input('What is your third answer? \n') + '\n')
      A4 = str(input('What is your fourth answer? \n') + '\n')
      CA = str(input('What is the correct answer? \n') + '\n')
      filehandle = open(Q1, 'w')
      filehandle.write(Q2 + A1 + A2 + A3 + A4 + CA)
      filehandle.close()
      ynAgain1 = str(input('Do you want to run the program again? (y/n)\n'))
      if ynAgain1 == str('n'):
        print('\n')
        break
      else:
        print('\n')
        continue
  if ynAgain == str('n'):
    continue
  if Launch == str('Q2'):
    FileOpen = str(input('Which file do you want to open? Don\'t forget the file type.\n'))
    inFile = open(FileOpen, 'r')
    QaA = inFile.readlines()
    Question = str(QaA[0].strip('\n'))
    A = str(QaA[1].strip('\n'))
    B = str(QaA[2].strip('\n'))
    C = str(QaA[3].strip('\n'))
    D = str(QaA[4].strip('\n'))
    E = str(QaA[5].strip('\n'))

    Questions = [A, B, C, D, E]
    shuffle(Questions)
    
    print('\n' + Question + '(A/B/C/D/E)\n\n')
    QuestionNumber = ['A','B','C','D','E']
    for i in range(5):
      print(QuestionNumber[i] + ". " + Questions[i] + '\n')
    userAnswer = str(input())
    if userAnswer == E:
      CAs = CAs + 1
      print("Your answer is...")
      sleep(3)
      print("Correct!! \n Congratulations! You got" + CAs + "questions right!")
    else:
      CAs = 0
      print('Your answer is...')
      sleep(3)
      print("Incorrect!! \n Oooh, sorry. You got" + CAs + "questions right before you failed.")
    ynAgain1 = str(input('Do you want to run the program again? (y/n)\n'))
    if ynAgain1 == str('n'):
      print('\n')
      break
    else:
      print('\n')
      continue
  if ynAgain == str('n'):
    continue