import math

class ModularCalculator:
    def is_prime(self, n):
        # Método para verificar si un número n es primo.
        # Se usa el método de prueba de divisibilidad hasta la raíz cuadrada de n.
        if n < 2:
            return False  # Números menores que 2 no son primos.
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:  # Si n es divisible por algún número entre 2 y sqrt(n), no es primo.
                return False
        return True  # Si no se encuentra divisor, es primo.

    def suma_modular(self, a, b, p):
        # Método para realizar la suma modular (a + b) mod p.
        # Se asegura de que tanto a como b se reduzcan módulo p antes de la suma.
        return (a % p + b % p) % p

    def resta_modular(self, a, b, p):
        # Método para realizar la resta modular (a - b) mod p.
        # Se asegura de que tanto a como b se reduzcan módulo p antes de la resta.
        return (a % p - b % p) % p

    def multiplicacion_modular(self, a, b, p):
        # Método para realizar la multiplicación modular (a * b) mod p.
        # Se asegura de que tanto a como b se reduzcan módulo p antes de la multiplicación.
        return (a % p * b % p) % p

    def division_modular(self, a, b, p):
        # Método para realizar la división modular (a / b) mod p.
        # Calcula (a * inverso_modular(b, p)) mod p, es decir, a * b⁻¹ mod p.
        if b == 0:
            raise ZeroDivisionError("División por cero.")  # No se puede dividir por cero.
        try:
            inv = self.inverso_modular(b, p)  # Busca el inverso modular de b.
            return (a * inv) % p  # Realiza la multiplicación modular con el inverso.
        except ValueError:
            raise ValueError(f"El inverso modular de {b} no existe módulo {p}.")  # Error si no hay inverso modular.

    def exponenciacion_modular(self, a, b, p):
        # Método para realizar la exponenciación modular (a^b) mod p.
        # Usa el algoritmo rápido de exponenciación modular (pow en Python).
        a = a % p  # Reduce a mod p.
        if b < 0:
            # Si el exponente es negativo, primero se calcula el inverso modular de a.
            a = self.inverso_modular(a, p)
            b = -b  # El exponente se convierte en positivo.
        return pow(a, b, p)  # Usa pow(a, b, p) que calcula (a^b) % p eficientemente.

    def inverso_modular(self, a, p):
        # Método para calcular el inverso modular de a mod p usando el algoritmo extendido de Euclides.
        # Si a tiene inverso modular, retorna el inverso tal que (a * inv) % p == 1.

        def egcd(a, b):
            # Algoritmo extendido de Euclides para calcular el máximo común divisor (gcd) de a y b,
            # y además encontrar los coeficientes x e y tales que ax + by = gcd(a, b).
            if a == 0:
                return (b, 0, 1)  # Caso base: gcd(b, 0) = b.
            else:
                # Llama recursivamente a egcd para obtener el gcd y los coeficientes.
                g, y, x = egcd(b % a, a)
                return (g, x - (b // a) * y, y)

        # Usa egcd para calcular gcd(a, p) y los coeficientes x e y.
        g, x, _ = egcd(a % p, p)
        if g != 1:
            # Si gcd(a, p) no es 1, entonces no existe el inverso modular.
            raise ValueError(f"El inverso modular de {a} no existe módulo {p}.")
        else:
            # Si gcd(a, p) es 1, x es el inverso modular de a mod p.
            return x % p