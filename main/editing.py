from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QVBoxLayout, QWidget

class EditPanel(QWidget):
    'Represents the editing panel on the right side'
    def __init__(self, layoutName, parent=None):
        'Initializes the editing panel'
        super(EditPanel, self).__init__(parent)
        self.__populateLayoutsDictionary()
        self.useLayout(layoutName)

    # wrapper for setLayout, use this instead of setLayout
    def useLayout(self, layoutName):
        'Uses the layout with the given name'
        self.__currentLayout = layoutName
        self.setLayout(self.__layouts['general']['layout'][layoutName])

    def save(self):
        'Call to save the changes'
        if (self.__layoutName == 'content'):
            pass

    def __populateLayoutsDictionary(self):
        'Populates the layouts dictionary'
        # TODO: change hardcoded solution into dynamic one
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

        # category specific form fields

        # etc ...

        # creating layouts

        self.__layouts['general']['layout'] = {}

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
        
        self.__layouts['general']['layout']['content']  = contentLayout  
