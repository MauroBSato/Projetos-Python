import time

t = input('Insira o tempo: ')
def countdown(t):
  while t: 
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -=1

  print('Timer finalizado!')


countdown(int(t))
  

#02d (formato de string) d --> valor inteiro, f --> seria float, 0 --> considerar 0 a esquerda, 2 --> informa que são 2 digitos
#time.sleep --> deixar 1s entre o tempo dos prints 
#\r --> reescrever o print anterior