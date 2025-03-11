import sys, json
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from cadastro.telaCadastro import Ui_MainWindow

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_cadastrar.clicked.connect(self.cadastrar)

        self.campos = [
            self.ui.lineEdit_Nome,
            self.ui.lineEdit_idade,
            self.ui.lineEdit_sexo,
            self.ui.lineEdit_peso,
            self.ui.lineEdit_altura,
            self.ui.lineEdit_objetivo
        ]

        self.show()

    def cadastrar(self):
        if any(campo.text().strip() == "" for campo in self.campos):
            QtWidgets.QMessageBox.warning(self, "Erro", "Preencha todos os campos")
            return
        
        else:
            data = {
                "nome": self.ui.lineEdit_Nome.text(),
                "idade": self.ui.lineEdit_idade.text(),
                "sexo": self.ui.lineEdit_sexo.text(),
                "peso": self.ui.lineEdit_peso.text(),
                "altura": self.ui.lineEdit_altura.text(),
                "objetivo": self.ui.lineEdit_objetivo.text(),
            }

            pasta = "cadastro.json"
    
            with open(pasta, "w") as file:
                json.dump(data, file, indent=4)    

            

            QtWidgets.QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())