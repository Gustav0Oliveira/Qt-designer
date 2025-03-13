import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from telaInicio.telaInicio import Ui_MainWindow

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_cadastroPaciente.clicked.connect(self.cadastro)

        # self.ui.pushButton_registroPaciente.clicked.connect(self.registro)

       
    def cadastro(self):
        from cadastro.mainCadastro import Main
        self.cadastro = Main()
        self.cadastro.show()

    # def registro(self):
    #     from registro.mainRegistro import Main
    #     self.registro = Main()
    #     self.registro.show()


            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())