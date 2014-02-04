from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QShortcut, QWidget, QStackedWidget
from PyQt5.QtGui import QKeySequence
from main.io.files import read_file, write_file
import json

class EditPanel():
    'Represents the editing panel on the right side'
    def __init__(self, parent=0):
        'Initializes the editing panel'
        self.__panel = QStackedWidget(parent)
        self.__populateLayoutsDictionary()
        self.__useWidget('none')
        self.__saveShortcut = QShortcut(QKeySequence.Save, self.__panel)
        self.__saveShortcut.activated.connect(self.save)

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
        self.__panel.parent().parent().setWindowModified(False)
        if (self.__currentWidgetName == 'content'):
            self.__currentWidget.setModified(False)

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

    def setModified(self, modified):
        'Sets the document modified state to modified'
        self.__document.setModified(modified)

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
        self.__textEdit.setPlainText(data['text'])
        
    def __createFormFields(self):
        'Creates the form fields'
        self.__idLine = QLabel()
        
        self.__titleLine = QLineEdit()
        self.__titleLine.textEdited.connect(self.__setModified)
        
        self.__descriptionLine = QLineEdit()
        self.__descriptionLine.textEdited.connect(self.__setModified)

        self.__slugLine = QLineEdit()
        self.__slugLine.textEdited.connect(self.__setModified)

        self.__metaDescriptionLine = QLineEdit()
        self.__metaDescriptionLine.textEdited.connect(self.__setModified)

        self.__metaKeywordsLine = QLineEdit()
        self.__metaKeywordsLine.textEdited.connect(self.__setModified)

        self.__tagsLine = QLineEdit()
        self.__tagsLine.textEdited.connect(self.__setModified)

        self.__text = QLabel('Text')
        self.__textEdit = QTextEdit()
        self.__document = self.__textEdit.document()
        self.__document.modificationChanged.connect(self.__documentModified)

        contentLayout = QFormLayout()
        contentLayout.addRow('ID', self.__idLine)
        contentLayout.addRow('Title', self.__titleLine)
        contentLayout.addRow('Description', self.__descriptionLine)
        contentLayout.addRow('Slug', self.__slugLine)
        contentLayout.addRow('Meta description', self.__metaDescriptionLine)
        contentLayout.addRow('Meta keywords', self.__metaKeywordsLine)
        contentLayout.addRow('Tags', self.__tagsLine)
        contentLayout.addRow('Text', self.__textEdit)
        self.setLayout(contentLayout)

    def __setModified(self, modified=True):
        'Sets the windowModified property of the main window to modified'
        self.parent().parent().parent().setWindowModified(modified)

    def __documentModified(self):
        'Called when the document has been modified'
        self.__setModified(self.__document.isModified())

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
        self.__idLine = QLabel()
        
        self.__titleLine = QLineEdit()
        self.__titleLine.textEdited.connect(self.__markAsModified)
        
        self.__descriptionLine = QLineEdit()
        self.__descriptionLine.textEdited.connect(self.__markAsModified)

        self.__slugLine = QLineEdit()
        self.__slugLine.textEdited.connect(self.__markAsModified)

        categoryLayout = QFormLayout()
        categoryLayout.addRow('ID', self.__idLine)
        categoryLayout.addRow('Title', self.__titleLine)
        categoryLayout.addRow('Description', self.__descriptionLine)
        categoryLayout.addRow('Slug', self.__slugLine)
        self.setLayout(categoryLayout)

    def __markAsModified(self):
        'Marks this widget as modified'
        self.parent().parent().parent().setWindowModified(True)

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
        self.__idLine = QLabel()
        
        self.__titleLine = QLineEdit()
        self.__titleLine.textEdited.connect(self.__markAsModified)
        
        self.__descriptionLine = QLineEdit()
        self.__descriptionLine.textEdited.connect(self.__markAsModified)

        self.__slugLine = QLineEdit()
        self.__slugLine.textEdited.connect(self.__markAsModified)

        self.__contentIDLine = QLineEdit()
        self.__contentIDLine.textEdited.connect(self.__markAsModified)

        pageLayout = QFormLayout()
        pageLayout.addRow('ID', self.__idLine)
        pageLayout.addRow('Title', self.__titleLine)
        pageLayout.addRow('Description', self.__descriptionLine)
        pageLayout.addRow('Slug', self.__slugLine)
        pageLayout.addRow('Content-ID', self.__contentIDLine)
        self.setLayout(pageLayout)

    def __markAsModified(self):
        'Marks this widget as modified'
        self.parent().parent().parent().setWindowModified(True)