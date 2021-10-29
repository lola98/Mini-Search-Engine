from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
from search_engine import Search_Engine

class Ui_Form(object):
    files = []
    _translate = QtCore.QCoreApplication.translate

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)

        # define font size
        custom_font = QFont()
        custom_font.setPointSize(20)
        QApplication.setFont(custom_font, "QLabel")

        # create header
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 30, 500, 180))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # create file upload button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 150, 200, 100))
        self.pushButton.setStyleSheet("background-color:white;\n"
                                      "color: black;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 16px;\n"
                                      "padding :10px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        # create empty block to print input file names
        self.label_filenames = QtWidgets.QPlainTextEdit(Form) 
        self.label_filenames.setGeometry(QtCore.QRect(200, 275, 200, 100))
        self.label_filenames.setReadOnly(True)
        self.label_filenames.setBackgroundVisible(False)
        self.label_filenames.setObjectName("label_filenames")

        # create confirmation button
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(150, 400, 300, 100))
        self.pushButton2.setStyleSheet("background-color:white;\n"
                                      "color: black;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 16px;\n"
                                      "padding :10px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton2.setObjectName("pushButton2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(self._translate("Form", "Search Engine"))
        self.label.setText(self._translate("Form", "Load My Engine"))
        self.pushButton.setText(self._translate("Form", "Choose Files"))
        self.pushButton2.setText(self._translate("Form", "Construct Inverted Indicies"))

        # set on-click events
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton2.clicked.connect(self.pushButton2_handler)


    def pushButton_handler(self):
        paths = QFileDialog.getOpenFileNames()
        self.files = paths[0]
        self.label.setText(self._translate("Form", "Load My Engine"))

        for f in self.files:
            self.label_filenames.appendPlainText(self._translate("Form", f.split("/")[-1]))

        self.pushButton2.setText(self._translate("Form", "Load Engine"))

    # upload selected files to GCP bucket
    def pushButton2_handler(self):
        Search_Engine.upload_to_bucket(self.files)
        self.update_page()

    def update_page(self):
        # update header
        if (len(self.files) ==0):
            self.label.setText(self._translate("Form", "Please Select Files First"))
        else:
            self.label.setText(self._translate("Form", "Engine was loaded \n & \n " \
                + "Inverted indicies were constructed successfully! \n \n \n " \
                    + "Please Select Action"))

            # update GUI, delete old elements
            self.pushButton.move(200, 220)
            self.pushButton.setText(self._translate("Form", "Search for Term"))

            # self.pushButton2.move(200, 370)
            self.pushButton2.setGeometry(QtCore.QRect(200, 350, 200, 100))
            self.pushButton2.setText(self._translate("Form", "Top-N"))

            self.label_filenames.deleteLater()

            # update on-click events
            # self.pushButton.clicked.connect(self.search_handler("search"))
            # self.pushButton2.clicked.connect(self.search_handler("topn"))


    # def search_handler(self, action):
    #     if action == "search":
    #         self.label.setText(self._translate("Form", "Enter Your Search Term"))
    #     elif action == "topn":
    #         self.label.setText(self._translate("Form", "Enter Your N Value"))
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())