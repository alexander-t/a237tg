import unittest

from uppgift1_4 import *

class TestUppgift1(unittest.TestCase):
    def test_medeltal_av_ett_tal(self):
        self.assertEqual(5, mean_value([5]))

    def test_medeltal_av_två_tal(self):
        self.assertEqual(5.0, mean_value([9.99, 0.01]))

    def test_min_lista(self):
        self.assertEqual(-99.3, min_value([0, 1, -3.4, 17, 44.4, -99.3, -5]))

    def test_min_ett_tal(self):
            self.assertEqual(3, min_value([3]))

    def test_max_lista(self):
        self.assertEqual(44.4, max_value([0, 1, -3.4, 17, 44.4, -99.3, -5]))

    def test_max_ett_tal(self):
        self.assertEqual(3, max_value([3]))



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
