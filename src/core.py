#! /usr/bin/env python3.3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QMenu, QMenuBar, QSplitter
from PyQt5.QtGui import QKeySequence
from main.editing import EditPanel
from main.repo import TreeView
from main.config import ConfigDialog

class Main:
    'Main class of the application'
    def __init__(self):
        'Initializes the application'
        self.__application = QApplication(sys.argv)
        self.__application.setApplicationName('CMS API Client')
        self.__mainWindow = QMainWindow()
        # set up main window
        self.__contentPane = self.__createContentPane()
        self.__menuBar = self.__createMenuBar()
        self.__mainWindow.setCentralWidget(self.__contentPane)
        self.__mainWindow.setMenuBar(self.__menuBar)
        self.__mainWindow.show()
        self.__application.exec()

    def __createContentPane(self):
        'Creates the central content pane'
        contentPane = QWidget()
        splitter = QSplitter(contentPane)
        treeView = TreeView(splitter)
        splitter.addWidget(treeView)

        editPanel = EditPanel(contentPane)
        treeView.addListener('core', editPanel.setCurrentFile)
        gridLayout = QGridLayout()
        gridLayout.addWidget(splitter, 0, 0)
        gridLayout.addWidget(editPanel.getWidget(), 0, 1)
        contentPane.setLayout(gridLayout)
        return contentPane

    def __createMenuBar(self):
        'Creates the menu bar'
        # create menus
        menuBar = QMenuBar()
        # create file menu
        fileMenu = QMenu('&File', menuBar)
        closeAction = fileMenu.addAction('&Quit')
        closeAction.triggered.connect(self.__close)
        closeAction.setShortcut(QKeySequence.Quit)
        # create edit menu
        editMenu = QMenu('&Edit', menuBar)
        configDialog = ConfigDialog(self.__mainWindow)
        configAction = editMenu.addAction('&Preferences')
        configAction.triggered.connect(configDialog.show)
        # create help menu
        helpMenu = QMenu('&Help', menuBar)
        aboutQtAction = helpMenu.addAction('About &Qt')
        aboutQtAction.triggered.connect(self.__application.aboutQt)

        menuBar.addMenu(fileMenu)
        menuBar.addMenu(editMenu)
        menuBar.addMenu(helpMenu)
        return menuBar
    
    def __close(self):
        'Closes the application'
        self.__application.closeAllWindows()

if __name__ == '__main__':
    import core
    core.Main()