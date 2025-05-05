import time

def regressiva(t):
    while t:
        mins, seg = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, seg)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Regressiva completa')

t = input('Informe o tempo em segundos ')

regressiva(int(t))