"""
Crear una función calc_primes_up_to(max_value) que nos muestra todos los números primos
disponibles desde 0 hasta ese número
"""

def calc_primes_up_to(max_value):
    primes_set = set()
    for i in range(1, max_value):
        prime = True
        for j in range(1, i):
            if i % j == 0 and j != 1:
                prime = False
                break
        if prime == False:
            continue
        else:
            primes_set.add(i)
    return primes_set


"""
Dos números primos con una diferencia de dos unidades se consideran gemelos (3: 5) 
aquellos que tienen una diferencia de 4, se consideran primos (3:7)
y los que tienen una diferencia de 6, se consideran sexy (6: 11)
Calcular todos los que tienen estas características hasta un input_max
"""

def gemelo_primo_sexy(max_value):
    prime_numbers = list(calc_primes_up_to(max_value))
    factores = {'gemelos': 2, 'primos': 4, 'sexy': 6}
    resultados = {'gemelos': set(), 'primos': set(), 'sexy': set()}

    for k, v in factores.items():
        for i in prime_numbers:
            if i + v in prime_numbers:
                resultados[k].add((i, i + v))

    return resultados