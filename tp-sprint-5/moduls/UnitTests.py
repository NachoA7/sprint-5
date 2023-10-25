import unittest

class CalcularMontoTotal(unittest.TestCase):
    def test_calcular_monto_total(self, Monto_Dolares = 500):
        Impuesto_Pais = Monto_Dolares * 0.25
        Impuesto_Ganancias = Monto_Dolares * 0.35
        Total = Monto_Dolares + Impuesto_Pais + Impuesto_Ganancias
        self.assertEqual(Total, 800.0)
        self.assertIsInstance(Total, float)
        self.assertNotIsInstance(Total, int)
        self.assertNotIsInstance(Total, str)

    def test_descontar_comision(self, monto = 1683, comision_porcentaje = 11):
        comision = comision_porcentaje / 100
        descuento = monto * comision
        descontar_comision = monto - descuento
        self.assertEqual(descontar_comision, 1497.87)
        self.assertIsInstance(descontar_comision, float)
        self.assertNotIsInstance(descontar_comision, int)
        self.assertNotIsInstance(descontar_comision, str)

    def test_calcular_monto_plazo_fijo(self, monoto_plazo_fijo = 35900):
        tasa = 133
        dias = 60
        intereses = monoto_plazo_fijo * ((tasa/100) * dias / 365)
        self.assertEqual(round(intereses, 2), 7848.82)
        self.assertIsInstance(intereses, float)
        self.assertNotIsInstance(intereses, int)
        self.assertNotIsInstance(intereses, str)

if __name__ == '__main__':
 unittest.main()