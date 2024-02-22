import time
import random

# Solicitar ao usuário o tempo de duração desejado
tempo_total = int(input("Digite o tempo de duração em segundos: "))

def mostrar_golpes(tempo):
    lista_de_golpes = ['Jab', 'Direto', 'Gancho de esquerda', 'Gancho de direita', 'Upper', 'Hook']

    start_time = time.time()
    while time.time() - start_time < tempo:
        golpe = random.choice(lista_de_golpes)
        print(golpe)
        time.sleep(2)



# Chama a função para mostrar os golpes durante o tempo especificado
mostrar_golpes(tempo_total)