import random
import time

NUM_EXECUTIONS = 5

def sequential_search(sequence, key):
    for i in range(len(sequence)):
        if sequence[i] == key:
            return i
    return -1

def optimized_sequential_search(sequence, key):
    for i in range(len(sequence)):
        if sequence[i] > key:
            return -1
        if sequence[i] == key:
            return i
    return -1

def binary_search(sequence, key):
    left, right = 0, len(sequence) - 1
    while left <= right:
        middle = (left + right) // 2
        if sequence[middle] == key:
            return middle
        elif sequence[middle] < key:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def main():
    sizes_n = [10**4, 10**5, 10**6, 10**7]
    sizes_q = [10**2, 10**3, 10**4, 10**5]

    for n in sizes_n:
        for q in sizes_q:
            # Geração da sequência e das chaves
            sequences = [random.randint(1, 10*n) for _ in range(n)]
            keys = [random.randint(1, 10*n) for _ in range(q)]

            # Sequential Search
            sequential_search_times = []
            for _ in range(NUM_EXECUTIONS):
                start = time.time()
                for key in keys:
                    sequential_search(sequences, key)
                end = time.time()
                sequential_search_times.append(end - start)
            average_time_sequential_search = (sum(sequential_search_times) / NUM_EXECUTIONS) * 1000

            # Ordenação da sequência para buscas otimizadas
            sorted_sequences = sorted(sequences)

            # Optimized Sequential Search
            optimized_sequential_search_times = []
            for _ in range(NUM_EXECUTIONS):
                start = time.time()
                for key in keys:
                    optimized_sequential_search(sorted_sequences, key)
                end = time.time()
                optimized_sequential_search_times.append(end - start)
            average_time_opt_seq_search = (sum(optimized_sequential_search_times) / NUM_EXECUTIONS) * 1000

            # Binary Search
            binary_search_times = []
            for _ in range(NUM_EXECUTIONS):
                start = time.time()
                for key in keys:
                    binary_search(sorted_sequences, key)
                end = time.time()
                binary_search_times.append(end - start)
            average_time_binary_search = (sum(binary_search_times) / NUM_EXECUTIONS) * 1000

            print("-----------------------------------")
            print("n = {}, q = {}".format(n, q))
            print("Busca Sequencial: {:.4f} ms".format(average_time_sequential_search))
            print("Busca Seq. Otimizada: {:.4f} ms".format(average_time_opt_seq_search))
            print("Busca Binária: {:.4f} ms".format(average_time_binary_search))
            print("-----------------------------------")

if __name__ == "__main__":
    main()

