import re

class Operations:
    def __init__(self, calculator):
        self.calculator = calculator
        self.last_operation = None

    def evaluate(self, expression, p):
        # Validar que p sea primo
        if not self.calculator.is_prime(p):
            raise ValueError("El módulo p debe ser un número primo.")

        # Eliminar espacios en blanco
        expression = expression.replace(" ", "")

        # Evaluar la expresión
        result = self._evaluate_expression(expression, p)

        # Guardar la última operación
        self.last_operation = (expression, p, result)

        return result

    def _evaluate_expression(self, expression, p):
        # Evaluar paréntesis primero
        while '(' in expression:
            expression = re.sub(r'\(([^()]+)\)', lambda m: str(self._evaluate_expression(m.group(1), p)), expression)

        # Evaluar exponentes
        while '^' in expression:
            expression = re.sub(r'(-?\d+)\^(-?\d+)', lambda m: str(self.calculator.exponenciacion_modular(int(m.group(1)), int(m.group(2)), p)), expression)

        # Evaluar multiplicación y división
        while '*' in expression or '/' in expression:
            expression = re.sub(r'(-?\d+)([*/])(-?\d+)', lambda m: str(self._evaluate_md(int(m.group(1)), m.group(2), int(m.group(3)), p)), expression)

        # Evaluar suma y resta
        while '+' in expression or (re.search(r'[^*/]-', expression) is not None):
            expression = re.sub(r'(-?\d+)([+-])(-?\d+)', lambda m: str(self._evaluate_as(int(m.group(1)), m.group(2), int(m.group(3)), p)), expression)

        return int(expression) % p

    def _evaluate_md(self, a, op, b, p):
        try:
            if op == '*':
                return self.calculator.multiplicacion_modular(a, b, p)
            else:  # op == '/'
                return self.calculator.division_modular(a, b, p)
        except ValueError as e:
            raise ValueError(f"Error en la operación {a} {op} {b} mod {p}: {str(e)}")

    def _evaluate_as(self, a, op, b, p):
        if op == '+':
            return self.calculator.suma_modular(a, b, p)
        else:  # op == '-'
            return self.calculator.resta_modular(a, b, p)