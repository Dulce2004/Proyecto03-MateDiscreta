import tkinter as tk
from tkinter import ttk

class ModularCalculatorGUI:
    def __init__(self, master, calculate_callback, clear_callback, undo_callback):
        self.master = master
        self.master.title("Calculadora Aritmética Modular")
        self.setup_gui(calculate_callback, clear_callback, undo_callback)

    def setup_gui(self, calculate_callback, clear_callback, undo_callback):
        self.frame = ttk.Frame(self.master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Entrada de expresión
        ttk.Label(self.frame, text="Expresión:").grid(row=0, column=0, sticky=tk.W)
        self.expression_var = tk.StringVar()
        self.expression_entry = ttk.Entry(self.frame, textvariable=self.expression_var, width=50)
        self.expression_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

        # Entrada del módulo
        ttk.Label(self.frame, text="Módulo (p):").grid(row=1, column=0, sticky=tk.W)
        self.p_var = tk.StringVar()
        self.p_entry = ttk.Entry(self.frame, textvariable=self.p_var)
        self.p_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Botones
        ttk.Button(self.frame, text="Calcular", command=calculate_callback).grid(row=2, column=0, pady=10)
        ttk.Button(self.frame, text="Limpiar", command=clear_callback).grid(row=2, column=1, pady=10)
        ttk.Button(self.frame, text="Deshacer", command=undo_callback).grid(row=2, column=2, pady=10)

        # Resultado y mensajes de error
        self.result_var = tk.StringVar()
        ttk.Label(self.frame, textvariable=self.result_var).grid(row=3, column=0, columnspan=3)
        self.error_var = tk.StringVar()
        self.error_label = ttk.Label(self.frame, textvariable=self.error_var, foreground="red")
        self.error_label.grid(row=4, column=0, columnspan=3)

    def set_result(self, result):
        self.result_var.set(result)

    def set_error(self, error):
        self.error_var.set(error)

    def clear_error(self):
        self.error_var.set("")

    def clear_all_fields(self):
        self.expression_var.set("")
        self.p_var.set("")
        self.result_var.set("")
        self.error_var.set("")

    def set_fields(self, expression, p, result):
        self.expression_var.set(expression)
        self.p_var.set(str(p))
        self.result_var.set(f"Resultado anterior: {result}")
        self.error_var.set("")