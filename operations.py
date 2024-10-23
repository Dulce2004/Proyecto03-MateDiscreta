import re

class Operations:
    def __init__(self, calculator):
        # Constructor que recibe una instancia de la calculadora modular.
        # Se inicializa también la variable `last_operation` para guardar la última operación realizada.
        self.calculator = calculator
        self.last_operation = None

    def evaluate(self, expression, p):
        # Método que evalúa una expresión en aritmética modular Z_p, donde p debe ser un número primo.
        
        # Validar que el valor de 'p' sea un número primo.
        if not self.calculator.is_prime(p):
            # Si 'p' no es primo, lanza un error de tipo ValueError.
            raise ValueError("El módulo p debe ser un número primo.")

        # Elimina espacios en blanco de la expresión para facilitar la evaluación.
        expression = expression.replace(" ", "")

        # Evalúa la expresión utilizando el módulo 'p' y guarda el resultado.
        result = self._evaluate_expression(expression, p)

        # Almacena la última operación (expresión, módulo y resultado) para poder deshacerla si es necesario.
        self.last_operation = (expression, p, result)

        # Devuelve el resultado de la operación modular.
        return result

    def _evaluate_expression(self, expression, p):
        # Método privado que evalúa la expresión aritmética paso a paso en orden de operaciones.
        
        # Primero, se evalúan las expresiones dentro de paréntesis de adentro hacia afuera.
        while '(' in expression:
            expression = re.sub(r'\(([^()]+)\)', lambda m: str(self._evaluate_expression(m.group(1), p)), expression)

        # Luego, se evalúan los exponentes utilizando el operador '^'.
        while '^' in expression:
            expression = re.sub(r'(-?\d+)\^(-?\d+)', lambda m: str(self.calculator.exponenciacion_modular(int(m.group(1)), int(m.group(2)), p)), expression)

        # A continuación, se evalúan las multiplicaciones y divisiones (* y /).
        while '*' in expression or '/' in expression:
            expression = re.sub(r'(-?\d+)([*/])(-?\d+)', lambda m: str(self._evaluate_md(int(m.group(1)), m.group(2), int(m.group(3)), p)), expression)

        # Finalmente, se evalúan las sumas y restas (+ y -).
        # Se utiliza `re.search` para encontrar restas que no sean parte de una operación de multiplicación o división.
        while '+' in expression or (re.search(r'[^*/]-', expression) is not None):
            expression = re.sub(r'(-?\d+)([+-])(-?\d+)', lambda m: str(self._evaluate_as(int(m.group(1)), m.group(2), int(m.group(3)), p)), expression)

        # Devuelve el resultado final de la expresión evaluada en aritmética modular Z_p.
        return int(expression) % p

    def _evaluate_md(self, a, op, b, p):
        # Método privado para evaluar multiplicaciones (*) y divisiones (/).
        try:
            if op == '*':
                # Si la operación es multiplicación, utiliza la función modular correspondiente.
                return self.calculator.multiplicacion_modular(a, b, p)
            else:  # Si la operación es división.
                return self.calculator.division_modular(a, b, p)
        except ValueError as e:
            # Si ocurre un error en la operación (ej. división entre cero), lanza un ValueError.
            raise ValueError(f"Error en la operación {a} {op} {b} mod {p}: {str(e)}")

    def _evaluate_as(self, a, op, b, p):
        # Método privado para evaluar sumas (+) y restas (-).
        if op == '+':
            # Si la operación es suma, utiliza la función modular correspondiente.
            return self.calculator.suma_modular(a, b, p)
        else:  # Si la operación es resta.
            return self.calculator.resta_modular(a, b, p)