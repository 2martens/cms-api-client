from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QVBoxLayout, QWidget, QStackedWidget
from main.io.files import read_file, write_file
import json

class EditPanel():
    'Represents the editing panel on the right side'
    def __init__(self, parent=0):
        'Initializes the editing panel'
        self.__panel = QStackedWidget(parent)
        self.__populateLayoutsDictionary()
        self.__useWidget('none')

    def setCurrentFile(self, file):
        'Updates the layout and reads existing values'
        # load file content
        self.__currentFile = file
        jsonData = read_file(self.__currentFile)
        self.__data = json.loads(jsonData)
        self.__useWidget(self.__data['type'])
        self.__updateFormFields()

    def save(self):
        'Call to save the changes'
        jsonEncoded = json.dumps(self.__data)
        write_file(self.__currentFile, jsonEncoded)

    def getWidget(self):
        'Returns the panel'
        return self.__panel

    def __useWidget(self, widgetName):
        'Uses the widget with the given name'
        self.__currentWidget = widgetName
        self.__panel.setCurrentIndex(self.__layouts[widgetName])

    def __updateFormFields(self):
        'Updates the form fields'
        pass

    def __populateLayoutsDictionary(self):
        'Populates the layouts dictionary'
        self.__layouts = {}
        categoryWidget = CategoryEditPanel(self.__panel)
        contentWidget = ContentEditPanel(self.__panel)

        self.__layouts['content']  = self.__panel.addWidget(contentWidget)
        self.__layouts['none'] = self.__panel.addWidget(QWidget())
        self.__layouts['category'] = self.__panel.addWidget(categoryWidget)

class ContentEditPanel(QWidget):
    def __init__(self, parent=0):
        super(ContentEditPanel, self).__init__(parent)
        self.__createFormFields()

    def updateFormFields(self, data):
        'Updates the form fields'
        pass
        
    def __createFormFields(self):
        'Creates the form fields'
        self.__layouts = {}
        # general form fields
        self.__layouts['general'] = {}
        self.__layouts['general']['label'] = {}
        self.__layouts['general']['fields'] = {}

        idLabel = QLabel('ID')
        self.__layouts['general']['label']['id'] = idLabel
        idLine = QLineEdit()
        idLine.setReadOnly(True)
        self.__layouts['general']['fields']['id'] = idLine

        title = QLabel('Title')
        self.__layouts['general']['label']['title'] = title
        titleLine = QLineEdit()
        self.__layouts['general']['fields']['title'] = titleLine

        description = QLabel('Description')
        self.__layouts['general']['label']['description'] = description
        descriptionLine = QLineEdit()
        self.__layouts['general']['fields']['description'] = descriptionLine

        slug = QLabel('Slug')
        self.__layouts['general']['label']['slug'] = slug
        slugLine = QLineEdit()
        self.__layouts['general']['fields']['slug'] = slugLine

        metaDescription = QLabel('Meta description')
        self.__layouts['general']['label']['metaDescription'] = metaDescription
        metaDescriptionLine = QLineEdit()
        self.__layouts['general']['fields']['metaDescription'] = metaDescriptionLine

        metaKeywords = QLabel('Meta keywords')
        self.__layouts['general']['label']['metaKeywords'] = metaKeywords
        metaKeywordsLine = QLineEdit()
        self.__layouts['general']['fields']['metaKeywords'] = metaKeywordsLine

        tags = QLabel('Tags')
        self.__layouts['general']['label']['tags'] = tags
        tagsLine = QLineEdit()
        self.__layouts['general']['fields']['tags'] = tagsLine

        # content specific form fields
        self.__layouts['contents'] = {}
        self.__layouts['contents']['label'] = {}
        self.__layouts['contents']['fields'] = {}

        contentLayout = QGridLayout()
        contentLayout.addWidget(self.__layouts['general']['label']['id'], 0, 0)
        contentLayout.addWidget(self.__layouts['general']['fields']['id'], 0, 1)
        contentLayout.addWidget(self.__layouts['general']['label']['title'], 1, 0)
        contentLayout.addWidget(self.__layouts['general']['fields']['title'], 1, 1)
        contentLayout.addWidget(self.__layouts['general']['label']['description'], 2, 0)
        contentLayout.addWidget(self.__layouts['general']['fields']['description'], 2, 1)
        contentLayout.addWidget(self.__layouts['general']['label']['slug'], 3, 0)
        contentLayout.addWidget(self.__layouts['general']['fields']['slug'], 3, 1)
        contentLayout.addWidget(self.__layouts['general']['label']['metaDescription'], 4, 0)
        contentLayout.addWidget(self.__layouts['general']['fields']['metaDescription'], 4, 1)
        contentLayout.addWidget(self.__layouts['general']['label']['metaKeywords'], 5, 0)
        contentLayout.addWidget(self.__layouts['general']['fields']['metaKeywords'], 5, 1)
        contentLayout.addWidget(self.__layouts['general']['label']['tags'], 6, 0)
        contentLayout.addWidget(self.__layouts['general']['fields']['tags'], 6, 1)
        self.setLayout(contentLayout)

class CategoryEditPanel(QWidget):
    def __init__(self, parent=0):
        super(CategoryEditPanel, self).__init__(parent)
        self.__createFormFields()
    
    def updateFormFields(self, data):
        'Updates the form fields'
        pass    

    def __createFormFields(self):
        'Creates the form fields'
        self.__layouts = {}
        # general form fields
        self.__layouts['general'] = {}
        self.__layouts['general']['label'] = {}
        self.__layouts['general']['fields'] = {}

        idLabel = QLabel('ID')
        self.__layouts['general']['label']['id'] = idLabel
        idLine = QLineEdit()
        idLine.setReadOnly(True)
        self.__layouts['general']['fields']['id'] = idLine

        title = QLabel('Title')
        self.__layouts['general']['label']['title'] = title
        titleLine = QLineEdit()
        self.__layouts['general']['fields']['title'] = titleLine

        description = QLabel('Description')
        self.__layouts['general']['label']['description'] = description
        descriptionLine = QLineEdit()
        self.__layouts['general']['fields']['description'] = descriptionLine

        slug = QLabel('Slug')
        self.__layouts['general']['label']['slug'] = slug
        slugLine = QLineEdit()
        self.__layouts['general']['fields']['slug'] = slugLine

        categoryLayout = QGridLayout()
        categoryLayout.addWidget(self.__layouts['general']['label']['id'], 0, 0)
        categoryLayout.addWidget(self.__layouts['general']['fields']['id'], 0, 1)
        categoryLayout.addWidget(self.__layouts['general']['label']['title'], 1, 0)
        categoryLayout.addWidget(self.__layouts['general']['fields']['title'], 1, 1)
        categoryLayout.addWidget(self.__layouts['general']['label']['description'], 2, 0)
        categoryLayout.addWidget(self.__layouts['general']['fields']['description'], 2, 1)
        categoryLayout.addWidget(self.__layouts['general']['label']['slug'], 3, 0)
        categoryLayout.addWidget(self.__layouts['general']['fields']['slug'], 3, 1)
        self.setLayout(categoryLayout)
