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
            novo_usuario = {
                "nome": self.ui.lineEdit_Nome.text(),
                "idade": self.ui.lineEdit_idade.text(),
                "sexo": self.ui.lineEdit_sexo.text(),
                "peso": self.ui.lineEdit_peso.text(),
                "altura": self.ui.lineEdit_altura.text(),
                "objetivo": self.ui.lineEdit_objetivo.text(),
            }

        arquivo_json = "cadastro.json"

        try:
            with open(arquivo_json, "r", encoding="utf-8") as file:
                dados = json.load(file)
                if not isinstance(dados, list):
                    dados = [dados]
        except (FileNotFoundError, json.JSONDecodeError):
            dados = []

        dados.append(novo_usuario)
        with open(arquivo_json, "w", encoding="utf-8") as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)

        QtWidgets.QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())