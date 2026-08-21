import queue
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print('Iniciando thread %s ' % self.name)
        processando_fila()
        print('Encerrando thread %s ' % self.name)

my_queue = queue.Queue()

def fatoracao(x):
    name_thread = threading.current_thread().name
    resultado = 'Fatores positivos de %i sao: ' % x
    for i in range(1, x + 1):
        if x % i == 0:
            resultado += str(i) + ' '
    resultado += '\n' + '_' * 30
    print(f'[{name_thread}] {resultado}')

def processando_fila():
    while True:
        try:
            x = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            fatoracao(x)
        time.sleep(5)

input_ = [532, 947, 55, 632, 437, 123, 822, 794]

for x in input_:
    my_queue.put(x)

thread_01 = MyThread('A')
thread_02 = MyThread('B')
thread_03 = MyThread('C')

thread_01.start()
thread_02.start()
thread_03.start()

thread_01.join()
thread_02.join()
thread_03.join()

print('Algoritimo finalizado!')