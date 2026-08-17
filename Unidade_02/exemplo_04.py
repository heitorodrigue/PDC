import threading
import time

def primeira_funcao():
    print(threading.current_thread().name + str(' Esta Iniciando \n'))
    time.sleep(5)
    print(threading.current_thread().name + str(' Esta Finalizando \n'))
    return

def segunda_funcao():
    print(threading.current_thread().name + str(' Esta Iniciando \n'))
    time.sleep(5)
    print(threading.current_thread().name + str(' Esta Finalizando \n'))
    return

def terceira_funcao():
    print(threading.current_thread().name + str(' Esta Iniciando \n'))
    time.sleep(5)
    print (threading.current_thread().name + str(' Esta Finalizando \n'))
    return

if __name__ == "__main__":
    t1 = threading.Thread(name='primeira_funcao', target=primeira_funcao)
    t2 = threading.Thread(name='segunda_funcao', target=segunda_funcao)
    t3 = threading.Thread(name='terceira_funcao', target=terceira_funcao)
    t1.start()
    t2.start()
    t3.start()
