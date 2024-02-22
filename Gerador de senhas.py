import random
import string

def gerador_de_senha(len_senha = 8):
  ascii_options = string.ascii_letters
  number_options = string.digits
  punt_options = string.punctuation
  options = ascii_options + number_options + punt_options

  senha_usuário = ""

  for i in range(0, len_senha):
    digit = random.choice(options)
    senha_usuário = senha_usuário + digit

  return senha_usuário

escolha_usuário = input("Quantidade de dígitos na senha: ")

if escolha_usuário.isdigit():
  escolha_usuário = int(escolha_usuário)
else:
  print("Entrada inválida")
  quit()

response = gerador_de_senha(len_senha = escolha_usuário)
print(f"senha gerada: \n{response}")