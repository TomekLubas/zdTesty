from zd_testy import NwdNww, auto
import unittest

class TestNwwNwd(unittest.TestCase):
    def test1(self):
        self.assertTrue(NwdNww.nwd(5,15) == 5)
        self.assertTrue(NwdNww.nww(5, 15) == 15)

    def test2(self):
        with self.assertRaises(TypeError):
            NwdNww.nwd('a',5)
        with self.assertRaises(TypeError):
            NwdNww.nww('a',5)


class TestAuta(unittest.TestCase):
    auto.dodaj_auto('Zaporozec')
    auto.dodaj_auto('Audi')
    auto.dodaj_auto('Fiat')
    auto.dodaj_auto('BMW')
    auto.dodaj_auto('Kia')
    def test1(self):
        auto.sortuj_auta()
        self.assertTrue(auto._auta == ['Audi', 'BMW', 'Fiat', 'Kia', 'Zaporozec'])


    def test2(self):
        auto.dodaj_auto('Fiat')
        self.assertTrue(auto.znajdz_duplikaty() == ['Fiat'])

    def test3(self):
        auto.usun_duplikaty()
        auto.sortuj_auta()
        self.assertTrue(auto._auta == ['Audi', 'BMW', 'Fiat', 'Kia', 'Zaporozec'])
