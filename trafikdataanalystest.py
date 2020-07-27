import unittest

from trafikdataanalys import *


class TestUppgift3(unittest.TestCase):
    def test_årsgruppering_accepterar_inte_strängar(self):
        with self.assertRaises(ValueError) as context:
            Årsgruppering('sträng')
        self.assertTrue('Ogiltigt år' in str(context.exception))

    def test_årsgruppering_accepterar_inte_ogiltiga_år(self):
        with self.assertRaises(ValueError) as context:
            Årsgruppering('1800')
        self.assertTrue('Ogiltigt år' in str(context.exception))

    def test_datarader_måste_ha_rätt_antal_kolumner(self):
        åg = Årsgruppering("2000")
        self.assertRaises(ValueError, åg.lägg_till_kvartalsrad, [1, 2, 3, 4, 5, 6, 7])
        with self.assertRaises(ValueError) as context:
            åg.lägg_till_kvartalsrad([1, 2, 3, 4, 5])
        self.assertTrue('hade 5')


if __name__ == '__main__':
    unittest.main()
