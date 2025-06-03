#Jogo quiz em Python

import os

questions = (
   "Quando a linguagem Python foi criada? > ",
   "Quais das opções cria uma função em Python? > ", 
   "Qual dessas cores estão presentes no simbolo de Python? > ", 
   "Qual o nome do criador do Python? > ",
   "Como acessar o Zen de Python > ")

options = (("A. 1989", "B. 1990", "C. 1981","D. 1985"),
           ("A. function()", "B. let()", "C. class())","D. def()"),
           ("A. Azul", "B. Vermelho", "C. branco","D. Preto"),
           ("A. Guido", "B. James Gosling", "C. Dennis Ritchie","D. David Wheeler"),
           ("A. import zen", "B. import zen of python", "C. import this","D. from python import zen"))


answers = ("A", "D", "A", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("--------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  
  guess = input("Enter (A,B, C, D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("Correct.")
  else:
    print("Incorrect.")
    print(f"{answers[question_num]} is the correct answer")
  question_num += 1

print('-----------------')
print('      RESULTS    ')
print('-----------------')

print('answers: ', end='')

for answer in answers:
  print(answer, end= ' ')
print()

print('guesses: ', end='')
for guess in guesses:
  print(guess, end= ' ')
print()

score = int(score / len(questions) * 100)

print(f'Sua pontuação foi {score}%')
if score >= 60:
  print(f'Você passou!')
else:
  print(f'Você nao passou!')