
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from lista import Ui_MainWindow

class main_ba2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
        self.pushButton.clicked.connect(self.addMeta)
        self.pushButton_2.clicked.connect(self.removeMeta)
    
    def addMeta(self):
            meta = self.lineEdit_2.text()
            if meta:
                
                item = QListWidgetItem(meta)
                item.setCheckState(0)
                
                self.listWidget.addItem(item)
                
                self.lineEdit_2.clear()

    def removeMeta(self):
            item = self.listWidget.currentRow()
            if item >= 0:
                self.listWidget.takeItem(item)        
            

if __name__ == "__main__":
    app = QApplication([])
    janela = main_ba2()
    janela.show()
    app.exec_()
