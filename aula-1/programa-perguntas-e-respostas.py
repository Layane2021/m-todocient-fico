#Nota Inicial

nota = 0

# Avaliação sobre a vacinação contra a Covid-19 no Brasil:

#Questão 1

print("Questão 1: Qual dessas vacinas foi a última a chegar no Brasil? ")
print("A: Coronavac ")
print("B: Janssen ")
print("C: AstraZeneca ")
print("D: Pfizer ")

pergunta_1 = input("Digite a letra que corresponde à resposta certa: ")
if pergunta_1 == "B" or pergunta_1 == "b":
  nota = nota + 1
  print("Resposta certa!")
else:
  print("Ops, você errou!")
print(f" Sua nota foi: {nota} ")
print(" ")


#Questão 2:

print("Questão 2: Qual é o nome da primeira brasileira a receber a vacina no Brasil? ")
print("A: Terezinha da Conceição")
print("B: Mônica Calazans")
print("C: Ludhmila Hajjar")
print("D: Luana Araújo ")

pergunta_2 = input("Digite a letra que corresponde à resposta correta: ")
if pergunta_2 == "B" or pergunta_2 == "b":
  nota = nota + 1
  print("Resposta certa!")
else:
  print("Ops, você errou!")
print(f" Sua nota foi: {nota} ")
print(" ")


#Questão 3: 

print("Questão 3: Qual é o nome da instituição que produziu a primeira vacina aplicada no Brasil contra a Covid-19? ")
print("A: Instituto Butantã")
print("B: Instituto Pasteur")
print("C: Fiocruz")
print("D: Bio-Manguinhos")

pergunta_3 = input("Digite a letra que corresponde à resposta correta: ")
if pergunta_3 == "A" or pergunta_3 == "a":
  nota = nota + 1
  print("Resposta certa!")
else:
  print("Ops, você errou!")
print(f" Sua nota foi: {nota} ")
print(" ")


#Questão 4:

print("Questão 4: Quantos anos tinha a primeira brasileira que recebeu a vacina contra a Covid-19")
print("A: 54 anos")
print("B: 50 anos")
print("C: 80 anos")
print("D: 81 anos")

pergunta_4 = input("Digite a letra que corresponde à resposta correta: ")
if pergunta_4 == "A" or pergunta_4 == "a":
  nota = nota + 1
  print("Resposta certa!")
else:
  print("Ops, você errou!")
print(f" Sua nota foi: {nota} ")
print(" ")


#Questão 5: 

print("Questão 5: Qual região aplicou a primeira vacina contra a Covid-19 no Brasil? ")       
print("A:Norte")
print("B:Nordeste")
print("C:Sul")
print("D:Sudeste")

pergunta_5 = input("Digite a letra que corresponde à resposta correta: ")
if pergunta_5 == "D" or pergunta_5 == "d":
  nota = nota + 1
  print("Resposta certa!")
else:
  print("Ops, você errou!")
print(f" Sua nota foi: {nota} ")
print(" ")


# Resultado final:

if nota <= 2:
  print("Você não foi muito bem. Tente novamente! 😓")
if nota == 3:
  print("Você acertou mais que a metade! Muito bom!🙂")
elif nota == 4:
  print("Parabéns, você passou! 🤩")
else:
  print("Parabéns, você acertou tudo! Arrasou!😍")

print(f"Sua nota final foi: {nota}")
print(" ")
