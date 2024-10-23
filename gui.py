import tkinter as tk
from tkinter import ttk

class ModularCalculatorGUI:
    def __init__(self, master, calculate_callback, clear_callback, undo_callback):
        # Constructor que inicializa la ventana principal (master) y configura la interfaz gráfica.
        # Se reciben callbacks para las acciones de calcular, limpiar y deshacer.
        self.master = master
        self.master.title("Calculadora Aritmética Modular")  # Título de la ventana.
        self.setup_gui(calculate_callback, clear_callback, undo_callback)  # Configura los componentes gráficos.

    def setup_gui(self, calculate_callback, clear_callback, undo_callback):
        # Método encargado de configurar y posicionar los elementos de la interfaz gráfica.

        # Crea un marco que contiene todos los widgets, con algo de padding para mejorar la apariencia.
        self.frame = ttk.Frame(self.master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Campo de entrada para la expresión aritmética
        ttk.Label(self.frame, text="Expresión:").grid(row=0, column=0, sticky=tk.W)
        self.expression_var = tk.StringVar()  # Variable para almacenar el valor ingresado en el campo de expresión.
        self.expression_entry = ttk.Entry(self.frame, textvariable=self.expression_var, width=50)  # Campo de entrada.
        self.expression_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))  # Posicionamiento del campo.

        # Campo de entrada para el módulo (p)
        ttk.Label(self.frame, text="Módulo (p):").grid(row=1, column=0, sticky=tk.W)
        self.p_var = tk.StringVar()  # Variable para almacenar el valor del módulo.
        self.p_entry = ttk.Entry(self.frame, textvariable=self.p_var)  # Campo de entrada para el módulo.
        self.p_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Botones para realizar acciones
        # Botón para calcular la expresión ingresada.
        ttk.Button(self.frame, text="Calcular", command=calculate_callback).grid(row=2, column=0, pady=10)
        # Botón para limpiar los campos de entrada y resultado.
        ttk.Button(self.frame, text="Limpiar", command=clear_callback).grid(row=2, column=1, pady=10)
        # Botón para deshacer la última operación realizada.
        ttk.Button(self.frame, text="Deshacer", command=undo_callback).grid(row=2, column=2, pady=10)

        # Etiqueta para mostrar el resultado de la operación
        self.result_var = tk.StringVar()  # Variable para almacenar y mostrar el resultado.
        ttk.Label(self.frame, textvariable=self.result_var).grid(row=3, column=0, columnspan=3)  # Posiciona la etiqueta del resultado.

        # Etiqueta para mostrar mensajes de error en caso de que ocurra algún problema.
        self.error_var = tk.StringVar()  # Variable para almacenar mensajes de error.
        self.error_label = ttk.Label(self.frame, textvariable=self.error_var, foreground="red")  # Mensaje de error en rojo.
        self.error_label.grid(row=4, column=0, columnspan=3)  # Posiciona la etiqueta de error.

    def set_result(self, result):
        # Establece el texto del resultado en la etiqueta correspondiente.
        self.result_var.set(result)

    def set_error(self, error):
        # Establece el texto del mensaje de error en la etiqueta correspondiente.
        self.error_var.set(error)

    def clear_error(self):
        # Limpia el mensaje de error.
        self.error_var.set("")

    def clear_all_fields(self):
        # Limpia todos los campos de entrada, el resultado y el mensaje de error.
        self.expression_var.set("")
        self.p_var.set("")
        self.result_var.set("")
        self.error_var.set("")

    def set_fields(self, expression, p, result):
        # Establece los valores en los campos de expresión y módulo, y muestra el resultado anterior.
        self.expression_var.set(expression)
        self.p_var.set(str(p))
        self.result_var.set(f"Resultado anterior: {result}")
        self.error_var.set("")