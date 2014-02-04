from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtWidgets import QTextEdit
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
        if (not self.__currentWidgetName == 'none'):
            self.save()

        self.__currentFile = file
        jsonData = read_file(self.__currentFile)
        data = json.loads(jsonData)
        self.__useWidget(data['type'])
        self.__updateFormFields(data)

    def save(self):
        'Call to save the changes'
        data = self.__currentWidget.getData()
        jsonEncoded = json.dumps(data, indent=4, sort_keys=True)
        write_file(self.__currentFile, jsonEncoded)

    def getWidget(self):
        'Returns the panel'
        return self.__panel

    def __useWidget(self, widgetName):
        'Uses the widget with the given name'
        self.__panel.setCurrentIndex(self.__layouts[widgetName])
        self.__currentWidget = self.__panel.currentWidget()
        self.__currentWidgetName = widgetName

    def __updateFormFields(self, data):
        'Updates the form fields'
        self.__currentWidget.updateFormFields(data)

    def __populateLayoutsDictionary(self):
        'Populates the layouts dictionary'
        self.__layouts = {}
        categoryWidget = CategoryEditPanel(self.__panel)
        contentWidget = ContentEditPanel(self.__panel)
        pageWidget = PageEditPanel(self.__panel)

        self.__layouts['content']  = self.__panel.addWidget(contentWidget)
        self.__layouts['none'] = self.__panel.addWidget(QWidget())
        self.__layouts['category'] = self.__panel.addWidget(categoryWidget)
        self.__layouts['page'] = self.__panel.addWidget(pageWidget)

class ContentEditPanel(QWidget):
    def __init__(self, parent=0):
        super(ContentEditPanel, self).__init__(parent)
        self.__createFormFields()

    def getData(self):
        'Returns the contents of the form fields'
        data = {
            'type': 'content',
            'id': self.__idLine.text(),
            'title': self.__titleLine.text(),
            'description': self.__descriptionLine.text(),
            'slug': self.__slugLine.text(),
            'metaDescription': self.__metaDescriptionLine.text(),
            'metaKeywords': self.__metaKeywordsLine.text(),
            'tags': self.__tagsLine.text(),
            'text': self.__textEdit.toPlainText()
        }
        return data

    def updateFormFields(self, data):
        'Updates the form fields'
        self.__idLine.setText(data['id'])
        self.__titleLine.setText(data['title'])
        self.__descriptionLine.setText(data['description'])
        self.__slugLine.setText(data['slug'])
        self.__metaDescriptionLine.setText(data['metaDescription'])
        self.__metaKeywordsLine.setText(data['metaKeywords'])
        self.__tagsLine.setText(data['tags'])
        
    def __createFormFields(self):
        'Creates the form fields'
        self.__idLabel = QLabel('ID')
        self.__idLine = QLineEdit()
        self.__idLine.setReadOnly(True)
        
        self.__title = QLabel('Title')
        self.__titleLine = QLineEdit()
        
        self.__description = QLabel('Description')
        self.__descriptionLine = QLineEdit()
        
        self.__slug = QLabel('Slug')
        self.__slugLine = QLineEdit()
        
        self.__metaDescription = QLabel('Meta description')
        self.__metaDescriptionLine = QLineEdit()
        
        self.__metaKeywords = QLabel('Meta keywords')
        self.__metaKeywordsLine = QLineEdit()
        
        self.__tags = QLabel('Tags')
        self.__tagsLine = QLineEdit()

        self.__text = QLabel('Text')
        self.__textEdit = QTextEdit()
        
        contentLayout = QGridLayout()
        contentLayout.addWidget(self.__idLabel, 0, 0)
        contentLayout.addWidget(self.__idLine, 0, 1)
        contentLayout.addWidget(self.__title, 1, 0)
        contentLayout.addWidget(self.__titleLine, 1, 1)
        contentLayout.addWidget(self.__description, 2, 0)
        contentLayout.addWidget(self.__descriptionLine, 2, 1)
        contentLayout.addWidget(self.__slug, 3, 0)
        contentLayout.addWidget(self.__slugLine, 3, 1)
        contentLayout.addWidget(self.__metaDescription, 4, 0)
        contentLayout.addWidget(self.__metaDescriptionLine, 4, 1)
        contentLayout.addWidget(self.__metaKeywords, 5, 0)
        contentLayout.addWidget(self.__metaKeywordsLine, 5, 1)
        contentLayout.addWidget(self.__tags, 6, 0)
        contentLayout.addWidget(self.__tagsLine, 6, 1)
        contentLayout.addWidget(self.__text, 7, 0)
        contentLayout.addWidget(self.__textEdit, 7, 1)
        self.setLayout(contentLayout)

class CategoryEditPanel(QWidget):
    def __init__(self, parent=0):
        super(CategoryEditPanel, self).__init__(parent)
        self.__createFormFields()
    
    def getData(self):
        'Returns the contents of the form fields'
        data = {
            'type': 'category',
            'id': self.__idLine.text(),
            'title': self.__titleLine.text(),
            'description': self.__descriptionLine.text(),
            'slug': self.__slugLine.text()
        }
        return data

    def updateFormFields(self, data):
        'Updates the form fields'
        self.__idLine.setText(data['id'])
        self.__titleLine.setText(data['title'])
        self.__descriptionLine.setText(data['description'])
        self.__slugLine.setText(data['slug'])

    def __createFormFields(self):
        'Creates the form fields'
        self.__idLabel = QLabel('ID')
        self.__idLine = QLineEdit()
        self.__idLine.setReadOnly(True)
        
        self.__title = QLabel('Title')
        self.__titleLine = QLineEdit()
        
        self.__description = QLabel('Description')
        self.__descriptionLine = QLineEdit()
        
        self.__slug = QLabel('Slug')
        self.__slugLine = QLineEdit()

        categoryLayout = QGridLayout()
        categoryLayout.addWidget(self.__idLabel, 0, 0)
        categoryLayout.addWidget(self.__idLine, 0, 1)
        categoryLayout.addWidget(self.__title, 1, 0)
        categoryLayout.addWidget(self.__titleLine, 1, 1)
        categoryLayout.addWidget(self.__description, 2, 0)
        categoryLayout.addWidget(self.__descriptionLine, 2, 1)
        categoryLayout.addWidget(self.__slug, 3, 0)
        categoryLayout.addWidget(self.__slugLine, 3, 1)
        self.setLayout(categoryLayout)

class PageEditPanel(QWidget):
    def __init__(self, parent=0):
        super(PageEditPanel, self).__init__(parent)
        self.__createFormFields()
    
    def getData(self):
        'Returns the contents of the form fields'
        data = {
            'type': 'page',
            'id': self.__idLine.text(),
            'title': self.__titleLine.text(),
            'description': self.__descriptionLine.text(),
            'slug': self.__slugLine.text(),
            'contentID': self.__contentIDLine.text()
        }
        return data

    def updateFormFields(self, data):
        'Updates the form fields'
        self.__idLine.setText(data['id'])
        self.__titleLine.setText(data['title'])
        self.__descriptionLine.setText(data['description'])
        self.__slugLine.setText(data['slug'])
        self.__contentIDLine.setText(data['contentID'])

    def __createFormFields(self):
        'Creates the form fields'
        self.__idLabel = QLabel('ID')
        self.__idLine = QLineEdit()
        self.__idLine.setReadOnly(True)
        
        self.__title = QLabel('Title')
        self.__titleLine = QLineEdit()
        
        self.__description = QLabel('Description')
        self.__descriptionLine = QLineEdit()
        
        self.__slug = QLabel('Slug')
        self.__slugLine = QLineEdit()

        self.__contentID = QLabel('Content-ID')
        self.__contentIDLine = QLineEdit()

        pageLayout = QGridLayout()
        pageLayout.addWidget(self.__idLabel, 0, 0)
        pageLayout.addWidget(self.__idLine, 0, 1)
        pageLayout.addWidget(self.__title, 1, 0)
        pageLayout.addWidget(self.__titleLine, 1, 1)
        pageLayout.addWidget(self.__description, 2, 0)
        pageLayout.addWidget(self.__descriptionLine, 2, 1)
        pageLayout.addWidget(self.__slug, 3, 0)
        pageLayout.addWidget(self.__slugLine, 3, 1)
        pageLayout.addWidget(self.__contentID, 4, 0)
        pageLayout.addWidget(self.__contentIDLine, 4, 1)
        self.setLayout(pageLayout)
