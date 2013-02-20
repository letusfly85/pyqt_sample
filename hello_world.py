import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui  as QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    main_window  = QtGui.QMainWindow()
    hello_button = QtGui.QPushButton("Hello! World!")
    main_window.setCentralWidget(hello_button)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()

