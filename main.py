from copy import deepcopy
from typing import List, Any

from ihm.mainwindow import *
import instance_creation
import resolution.dpll
import global_module


def main():
    x = 'uf20-0996.cnf'
    formula = instance_creation.Formule(x)
    fenetre_ouverture()

def fenetre_ouverture():
    # Instanciation de QApp
    myApp = QApplication(sys.argv)

    window = MainWindow()

    available_geometry = myApp.desktop().availableGeometry(window)
    window.resize(available_geometry.width() * 2 / 3, available_geometry.height() * 2 / 3)

    window.show()
    myApp.exec_()
    sys.exit()

if __name__ == "__main__":
    main()
