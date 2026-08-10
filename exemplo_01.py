from math import sqrt
import concurrent.futures
import multiprocessing
from timeit import default_timer as timer

def eh_primo(x):
    """"
    Retorna o propio numero se for primo, None caso contrario.
    """
    if x < 2:
        return  None
    if x == 2:
        return None
    if x % 2 == 0:
        return None

    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return None
    return x

def encontrar_primos_no_intervalo(inicio, quantidade, n_workes):
    """
    Encontra numeros primos em um intervalo usando ProcessPollExecutor
    Retorna: (lista de primos, tempo de coleta de resultados, tempo total)
    """
    intervalo = range(inicio, inicio + quantidade)
    start_total = timer()
    primos = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_workes) as executor:
    #Submete todas tarefas
        futures = [executor.submit(eh_primo,num) for num in intervalo]

        start_coleta = timer()

        for future in concurrent.futures.as_completed(futures):
            resultado = future.result()
            if resultado is not None:
                primos.append(resultado)

            tempo_coleta = timer() - start_coleta        

        tempo_total = timer() - start_total

        return primos, tempo_coleta, tempo_total

def main():
    #Configuracoes do teste
    _inicio = 10**13
    _quantidade = 50000
    _max_workers = multiprocessing.cpu_count()

    print(f"Testando intervalo: {_inicio:,} ate {_inicio + _quantidade:,}")
    print(f"Numero maximo de workes disponiveis: {_max_workers}\n")

    for n_workes in range(1, _max_workers + 1):
        print(f"\nTestando com {n_workes} processo(s)")

        primos, t_coleta, t_total = encontrar_primos_no_intervalo(
            _inicio, _quantidade, n_workes
            )
        print(f"Primos encontrados: {len(primos)}")
        if primos:
            print(f" Menor primo: {min(primos):,}")
            print(f" Maior primos: {max(primos):,}")

        print(f" Tempo apenas coleta de resultados: {t_coleta:8.4f} s")
        print(f" Tempo total (submissao + execucao + coleta): {t_total:8.4f} s")
        print("-" * 30)

if __name__ == "__main__":
    main()        

                               
