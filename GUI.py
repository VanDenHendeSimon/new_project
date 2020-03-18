from PySide2 import QtCore, QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)


class GUI(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self)
        self.parent = parent

        self.setWindowTitle("New Project")
        self.setMinimumSize(400, 220)
        self.setWindowIcon(QtGui.QIcon("github_logo.png"))
        self.setFont(QtGui.QFont('Serif', 13))

        self.layout = QtWidgets.QVBoxLayout()

        self.project_name_input = QtWidgets.QLineEdit()
        self.project_description_input = QtWidgets.QTextEdit()

        self.layout.addWidget(QtWidgets.QLabel("Project Name"))
        self.layout.addWidget(self.project_name_input)
        self.layout.addWidget(QtWidgets.QLabel("Project Description"))
        self.layout.addWidget(self.project_description_input)

        self.btm_box = QtWidgets.QHBoxLayout()

        self.private_bool = QtWidgets.QCheckBox("Private")
        self.submit_btn = QtWidgets.QPushButton("Create")
        self.submit_btn.clicked.connect(self.submit)

        self.btm_box.addWidget(self.private_bool)
        self.btm_box.addStretch(1)
        self.btm_box.addWidget(self.submit_btn)

        self.layout.addLayout(self.btm_box)

        self.setLayout(self.layout)

    def submit(self):
        self.parent.create_repo(
            self.project_name_input.text(),
            self.project_description_input.toPlainText(),
            self.private_bool.isChecked()
        )
        self.close()

    def open(self):
        self.show()
        sys.exit(app.exec_())
