
from tkinter import Tk
from gui import CalculatorGUI
from operations import suma_modular, resta_modular, multiplicacion_modular, division_modular, potencia_modular
from utils import validar_entrada_numerica, manejar_error

def main():
    root = Tk()
    app = CalculatorGUI(root)
    
    def realizar_operacion(operacion, a, b, p):
        if not all(validar_entrada_numerica(x) for x in (a, b, p)):
            manejar_error("Entradas inválidas")
            return
        
        a, b, p = map(int, (a, b, p))
        
        if operacion == "suma":
            resultado = suma_modular(a, b, p)
        elif operacion == "resta":
            resultado = resta_modular(a, b, p)
        # ... otras operaciones ...
        
        app.mostrar_resultado(resultado)
    
    app.configurar_callbacks(realizar_operacion)
    root.mainloop()

if __name__ == "__main__":
    main()