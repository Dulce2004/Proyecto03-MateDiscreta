import math

class ModularCalculator:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def suma_modular(self, a, b, p):
        return (a % p + b % p) % p

    def resta_modular(self, a, b, p):
        return (a % p - b % p) % p

    def multiplicacion_modular(self, a, b, p):
        return (a % p * b % p) % p

    def division_modular(self, a, b, p):
        if b == 0:
            raise ZeroDivisionError("División por cero.")
        try:
            inv = self.inverso_modular(b, p)
            return (a * inv) % p
        except ValueError:
            raise ValueError(f"El inverso modular de {b} no existe módulo {p}.")

    def exponenciacion_modular(self, a, b, p):
        a = a % p
        if b < 0:
            a = self.inverso_modular(a, p)
            b = -b
        return pow(a, b, p)

    def inverso_modular(self, a, p):
        def egcd(a, b):
            if a == 0:
                return (b, 0, 1)
            else:
                g, y, x = egcd(b % a, a)
                return (g, x - (b // a) * y, y)

        g, x, _ = egcd(a % p, p)
        if g != 1:
            raise ValueError(f"El inverso modular de {a} no existe módulo {p}.")
        else:
            return x % p