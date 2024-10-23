import tkinter as tk
from gui import ModularCalculatorGUI
from calculator import ModularCalculator
from operations import Operations
import logging

# Configuración del logging
# Este bloque configura el sistema de logging para almacenar mensajes en un archivo llamado 'calculator.log'.
# Se registrarán mensajes de depuración (DEBUG), con formato que incluye la fecha y hora, el nivel del mensaje y el contenido.
logging.basicConfig(filename='calculator.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ModularCalculatorApp:
    def __init__(self, master):
        # Inicializa la ventana principal de la aplicación y los componentes necesarios.
        # 'master' es la ventana de nivel superior (raíz) para la interfaz gráfica (Tkinter).
        self.master = master
        self.calculator = ModularCalculator()  # Instancia de la calculadora modular.
        self.evaluator = Operations(self.calculator)  # Instancia para evaluar las operaciones modulares.
        self.gui = ModularCalculatorGUI(master, self.calculate, self.clear_fields, self.undo_operation)  # GUI de la calculadora.

    def calculate(self):
        # Método encargado de manejar el cálculo de la operación modular.
        try:
            # Obtiene la expresión matemática y el valor primo 'p' desde la GUI.
            expression = self.gui.expression_var.get()
            p = int(self.gui.p_var.get())
            
            # Evalúa la expresión en aritmética modular Z_p (donde p es un número primo).
            result = self.evaluator.evaluate(expression, p)
            
            # Muestra el resultado en la GUI.
            self.gui.set_result(f"Resultado: {result}")
            self.gui.clear_error()
            
            # Registra el resultado exitoso en el archivo de logging.
            logging.info(f"Operación exitosa: {expression} mod {p} = {result}")

        # Manejo de posibles excepciones que pueden ocurrir durante el cálculo.
        except ValueError as e:
            # Error cuando la entrada no es válida (ej. no se puede convertir a entero).
            self.gui.set_error(str(e))
            logging.error(f"ValueError: {str(e)}")
        except ZeroDivisionError as e:
            # Error cuando se intenta dividir entre cero.
            self.gui.set_error(str(e))
            logging.error(f"ZeroDivisionError: {str(e)}")
        except OverflowError as e:
            # Error cuando el cálculo resulta en un número demasiado grande.
            self.gui.set_error(str(e))
            logging.error(f"OverflowError: {str(e)}")
        except Exception as e:
            # Manejo de cualquier otro error no previsto.
            self.gui.set_error(f"Error inesperado: {str(e)}")
            logging.exception("Error inesperado")

    def clear_fields(self):
        # Método para limpiar todos los campos de la interfaz gráfica.
        self.gui.clear_all_fields()
        
        # Registra que los campos han sido limpiados en el archivo de logging.
        logging.info("Campos limpiados")

    def undo_operation(self):
        # Método para deshacer la última operación realizada.
        if self.evaluator.last_operation:
            # Si existe una operación previa, se restauran los valores de la expresión y 'p' en la GUI.
            expression, p, result = self.evaluator.last_operation
            self.gui.set_fields(expression, p, result)
            
            # Registra la operación deshecha en el archivo de logging.
            logging.info(f"Operación deshecha: {expression} mod {p} = {result}")
        else:
            # Si no hay operación previa, muestra un error en la GUI.
            self.gui.set_error("No hay operación previa para deshacer.")
            
            # Registra el intento fallido de deshacer en el archivo de logging.
            logging.info("Intento de deshacer sin operación previa.")

def main():
    # Función principal que inicializa la ventana principal de Tkinter y lanza la aplicación.
    root = tk.Tk()
    app = ModularCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Si el script es ejecutado directamente, se llama a la función principal.
    main()