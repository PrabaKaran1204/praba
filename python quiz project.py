print('Hi sir welcome to python quiz')
s=0
playing = input('Do you want play?:')
if playing not in 'yesyahmm':
      quit()
print("Let's play")
answer=input('''1.who developed python programming?
              a)Rasmus
              b)guido van rossum
              c)storm
              option:''')
if answer=='b':
    print('correct')
    s+=1
else:
    print('wrong')
answer=input('''2.which keyword is used for function in python?
              a)function 
              b)fun
              c)def
              option:''')
if answer=='c':
    print('correct')
    s+=1
else:
    print('wrong')    
answer=input('''3.what is pep8 full form?
              a)python encourage proposal
              b)python enhancement proposal
              c)python energy py
              option:''')
if answer=='b':
    print('correct')
    s+=1
else:
    print('wrong')
answer=input('''4.select built in function in python?
              a)futorial()
              b)print()
              c)def
              option:''')
if answer=='b':
    print('correct')
    s+=1
else:
    print('wrong')    

print('your score is',s,'/4')
