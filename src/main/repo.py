from PyQt5.QtWidgets import QTreeView, QFileSystemModel
from PyQt5.QtCore import Qt, QVariant
from main.config import Config
from main.io.files import read_file
import json

class TreeView(QTreeView):
    'Represents the categories, contents, etc in the git repository'
    def __init__(self, parent=0):
        'Initializes the tree view'
        super(TreeView, self).__init__(parent)
        self.__config = Config()
        self.__gitDir = self.__config.get('Git', 'dir')
        self.__model = TitleFileSystemModel()
        self.__model.setRootPath(self.__gitDir)
        self.setModel(self.__model)
        self.setRootIndex(self.__model.index(self.__gitDir))
        headerView = self.header()
        headerView.hideSection(1)
        headerView.hideSection(2)
        headerView.hideSection(3)
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
            self.__currentFile = self.__model.filePath(currentIndex)
            for key in self.__listener:
                self.__listener[key](self.__currentFile)

class TitleFileSystemModel(QFileSystemModel):
    'Modified FileSystemModel to display titles of categories, contents, etc.'
    def __init__(self, parent=None):
        super(TitleFileSystemModel, self).__init__(parent)

    def data(self, index, role):
        'Overwritten data function'
        if (not index.isValid()):
            return QVariant()

        initialValue = super(TitleFileSystemModel, self).data(index, role)
        if (role == Qt.DisplayRole and not self.isDir(index)):
            filePath = self.filePath(index)
            jsonData = read_file(filePath)
            decodedData = json.loads(jsonData)
            initialValue = decodedData['id'] + ' - ' + decodedData['title']

        return initialValue
