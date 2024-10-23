import tkinter as tk
from gui import ModularCalculatorGUI
from calculator import ModularCalculator
from operations import Operations
import logging

# Configuración del logging
logging.basicConfig(filename='calculator.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ModularCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.calculator = ModularCalculator()
        self.evaluator = Operations(self.calculator)
        self.gui = ModularCalculatorGUI(master, self.calculate, self.clear_fields, self.undo_operation)

    def calculate(self):
        try:
            expression = self.gui.expression_var.get()
            p = int(self.gui.p_var.get())
            
            result = self.evaluator.evaluate(expression, p)
            self.gui.set_result(f"Resultado: {result}")
            self.gui.clear_error()
            logging.info(f"Operación exitosa: {expression} mod {p} = {result}")

        except ValueError as e:
            self.gui.set_error(str(e))
            logging.error(f"ValueError: {str(e)}")
        except ZeroDivisionError as e:
            self.gui.set_error(str(e))
            logging.error(f"ZeroDivisionError: {str(e)}")
        except OverflowError as e:
            self.gui.set_error(str(e))
            logging.error(f"OverflowError: {str(e)}")
        except Exception as e:
            self.gui.set_error(f"Error inesperado: {str(e)}")
            logging.exception("Error inesperado")

    def clear_fields(self):
        self.gui.clear_all_fields()
        logging.info("Campos limpiados")

    def undo_operation(self):
        if self.evaluator.last_operation:
            expression, p, result = self.evaluator.last_operation
            self.gui.set_fields(expression, p, result)
            logging.info(f"Operación deshecha: {expression} mod {p} = {result}")
        else:
            self.gui.set_error("No hay operación previa para deshacer.")
            logging.info("Intento de deshacer sin operación previa.")

def main():
    root = tk.Tk()
    app = ModularCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()