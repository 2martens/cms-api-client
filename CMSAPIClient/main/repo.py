from PyQt5.QtWidgets import QTreeView, QFileSystemModel
from CMSAPIConfig.main.config import Config

class TreeView(QTreeView):
    'Represents the categories, contents, etc in the git repository'
    def __init__(self, parent=0):
        'Initializes the tree view'
        super(TreeView, self).__init__(parent)
        self.__config = Config()
        self.__gitDir = self.__config.get('Git', 'dir')
        self.__model = QFileSystemModel()
        self.__model.setRootPath(self.__gitDir)
        self.setModel(self.__model)
        self.setRootIndex(self.__model.index(self.__gitDir))
        self.__selectionModel = self.selectionModel()
        self.__selectionModel.currentChanged.connect(self.__update)

        # initialize listener
        self.__listener = {}

    def getSelectedFile(self):
        'Returns the currently selected file'
        return self.__currentFile

    def addListener(self, key, function):
        'Adds a listener function to the list of listener'
        self.__listener[key] = function

    def removeListener(self, key):
        'Removes a listener from the list of listener'
        self.__listener[key] = None

    def __update(self, currentIndex, previousIndex):
        'Called when the current item in the tree view changes'
        if (not self.__model.isDir(currentIndex)):
            self.__currentFile = self.__model.fileName(currentIndex)
            for listener in self.__listener:
                listener(self.__currentFile)
