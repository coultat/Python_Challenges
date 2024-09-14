from my_project.schemes.maths import NumeroPrimo, Relations, SetPrimeNumbers


class CalcularNumerosPrimos:
    def __init__(self, input_max: int):
        self.input_max = input_max

    async def calcular_primos(self) -> SetPrimeNumbers:
        """
        Crear una función calc_primes_up_to(max_value) que nos muestra todos los números primos
        disponibles desde 0 hasta ese número
        """
        primes_set = set()
        for i in range(1, self.input_max + 1):
            prime: bool = True
            for j in range(1, i):
                if i % j == 0 and j != 1:
                    prime = False
                    break
            if not prime:
                continue
            else:
                primes_set.add(NumeroPrimo(number=i))
        return SetPrimeNumbers(set_prime_numbers=primes_set)

    async def gemelo_primo_sexy_test(self) -> Relations:
        """
        Dos números primos con una diferencia de dos unidades se consideran gemelos (3: 5)
        aquellos que tienen una diferencia de 4, se consideran primos (3:7)
        y los que tienen una diferencia de 6, se consideran sexy (6: 11)
        Calcular todos los que tienen estas características hasta un input_max
        """
        resultados = {"gemelos": 2, "primos": 4, "sexy": 6}
        relation: dict[str, list[dict[str, tuple[dict[str, int], dict[str, int]]]]] = {
            "gemelos": [],
            "primos": [],
            "sexy": [],
        }  # Todo change this for a proper pydantic object
        prime_numbers = await self.calcular_primos()
        for res in prime_numbers.set_prime_numbers:
            for familia, diferencia in resultados.items():
                if res.number % 2 == 0 and res.number != 2:
                    continue
                if NumeroPrimo(number=res.number + diferencia) in prime_numbers.set_prime_numbers:
                    relation[familia].append(  # dict[str, tuple[dict[str, int]]
                        {
                            "parejas": (
                                {"number": res.number},
                                {"number": res.number + diferencia},
                            )
                        }
                    )

        return Relations(**relation)
