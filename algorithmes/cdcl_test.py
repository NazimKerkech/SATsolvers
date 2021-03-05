import os
import unittest
import algorithmes.resolution.cdcl_SN3.cdcl as cdcl
from algorithmes.resolution import dpll
from instance_creation import Formule


class MyTestCase(unittest.TestCase):
    def test_cdcl_50(self):

        for file in os.listdir('/home/thedoctor/Documents/Python/PycharmProjects/SN2/UF50-218-1000'):
            file_name = '/home/thedoctor/Documents/Python/PycharmProjects/SN2/UF50-218-1000/' + file
            formule = Formule(file_name)
            resultat = cdcl.main(file_name)
            self.assertEqual(resultat, True)

    def test_cdcl_20(self):
        for file in os.listdir('/home/thedoctor/Documents/Python/PycharmProjects/SN2/uf20-91'):
            file_name = '/home/thedoctor/Documents/Python/PycharmProjects/SN2/uf20-91/' + file
            formule = Formule(file_name)
            resultat = cdcl.main(file_name)
            self.assertEqual(resultat, True)

    def test_cdcl_50_negatif(self):
        i = 0
        for file in os.listdir('/home/thedoctor/Documents/Python/PycharmProjects/SN2/UUF50.218.1000'):
            file_name = '/home/thedoctor/Documents/Python/PycharmProjects/SN2/UUF50.218.1000/' + file
            formule = Formule(file_name)
            resultat = cdcl.main(file_name)
            self.assertEqual(resultat, True)
            i += 1
            if i == 1:
                break

    def test_dpll_50(self):
        for file in os.listdir('/home/thedoctor/Documents/Python/PycharmProjects/SN2/UF50-218-1000'):
            file_name = '/home/thedoctor/Documents/Python/PycharmProjects/SN2/UF50-218-1000/' + file
            formule = Formule(file_name)
            resultat = dpll.main(file_name)
            self.assertEqual(resultat, True)

    def test_dpll_20(self):
        for file in os.listdir('/home/thedoctor/Documents/Python/PycharmProjects/SN2/uf20-91'):
            file_name = '/home/thedoctor/Documents/Python/PycharmProjects/SN2/uf20-91/' + file
            formule = Formule(file_name)
            resultat = dpll.main(file_name)
            self.assertEqual(resultat, True)

    def test_dpll_50_negatif(self):
        i = 0
        for file in os.listdir('/home/thedoctor/Documents/Python/PycharmProjects/SN2/UUF50.218.1000'):
            file_name = '/home/thedoctor/Documents/Python/PycharmProjects/SN2/UUF50.218.1000/' + file
            formule = Formule(file_name)
            resultat = dpll.main(file_name)
            self.assertEqual(resultat, False)
            i += 1
            if i == 100:
                break

if __name__ == '__main__':
    unittest.main()
