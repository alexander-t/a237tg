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
        self.assertTrue('hade 5', str(context.exception))

    def test_aggregering_kräver_fyra_rader(self):
        åg = Årsgruppering("2013")
        åg.lägg_till_kvartalsrad(["2013", "kvartal 1", "10202", "3", "8", "23"])
        åg.lägg_till_kvartalsrad(["2013", "kvartal 2", "10231", "3", "8", "22"])
        åg.lägg_till_kvartalsrad(["2013", "kvartal 3", "8736", "2", "7", "21"])
        with self.assertRaises(Exception) as context:
            åg.aggregera()
        self.assertTrue("inte innehåller fyra kvartal" in str(context.exception))

    def test_aggregering_happy_path(self):
        åg = Årsgruppering("2013")
        åg.lägg_till_kvartalsrad(["2013", "kvartal 1", "10202", "3", "8", "23"])
        åg.lägg_till_kvartalsrad(["2013", "kvartal 2", "10231", "3", "8", "22"])
        åg.lägg_till_kvartalsrad(["2013", "kvartal 3", "8736", "2", "7", "21"])
        åg.lägg_till_kvartalsrad(["2013", "kvartal 4", "11263", "3", "8", "24"])
        agg = åg.aggregera()
        self.assertEqual("2013", agg[0])
        self.assertEqual(40432.0, agg[1])
        self.assertEqual(2.75, agg[2])
        self.assertEqual(2.0, agg[3])
        self.assertEqual(3.0, agg[4])
        self.assertEqual(7.75, agg[5])
        self.assertEqual(7.0, agg[6])
        self.assertEqual(8.0, agg[7])
        self.assertEqual(22.5, agg[8])
        self.assertEqual(21.0, agg[9])
        self.assertEqual(24.0, agg[10])


if __name__ == '__main__':
    unittest.main()
