import unittest
from tkinter import Tk
from main import ModularCalculatorApp

class TestModularCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = ModularCalculatorApp(self.root)

    def test_complex_expression_1(self):
        self.app.gui.expression_var.set("(7^3 + 4 * 5) * 2")
        self.app.gui.p_var.set("23")
        self.app.calculate()
        self.assertEqual(self.app.gui.result_var.get(), "Resultado: 13")

    def test_complex_expression_2(self):
        self.app.gui.expression_var.set("((15 + 7) * 3 - 2^4) / 5")
        self.app.gui.p_var.set("29")
        self.app.calculate()
        self.assertEqual(self.app.gui.result_var.get(), "Resultado: 10")

    def test_complex_expression_3(self):
        self.app.gui.expression_var.set("(3^4 * 2 + 7) / (11 - 5^2)")
        self.app.gui.p_var.set("31")
        self.app.calculate()
        self.assertIn("inverso modular", self.app.gui.error_var.get())

    def test_complex_expression_4(self):
        self.app.gui.expression_var.set("(8 * (13 + 5^2) - 3^3) / (2^4 + 1)")
        self.app.gui.p_var.set("37")
        self.app.calculate()
        self.assertEqual(self.app.gui.result_var.get(), "Resultado: 31")

    def test_complex_expression_5(self):
        self.app.gui.expression_var.set("((6^2 * 3 + 7) / (2^3 - 5)) * (11 + 4^3) - 9")
        self.app.gui.p_var.set("41")
        self.app.calculate()
        self.assertEqual(self.app.gui.result_var.get(), "Resultado: 37")

    def test_division_by_zero(self):
        self.app.gui.expression_var.set("1 / 0")
        self.app.gui.p_var.set("31")
        self.app.calculate()
        self.assertIn("División por cero", self.app.gui.error_var.get())

    def test_no_modular_inverse(self):
        self.app.gui.expression_var.set("1 / 3")
        self.app.gui.p_var.set("6")
        self.app.calculate()
        self.assertIn("inverso modular", self.app.gui.error_var.get())

if __name__ == '__main__':
    unittest.main()