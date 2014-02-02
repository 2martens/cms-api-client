import configparser
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QGridLayout

class Config:
    'Config accessor class'
    def __init__(self, configfile='config.ini'):
        self.__configfile = configfile
        self.__config = self.__read()

    def get(self, section, key):
        'Returns a config value'
        return self.__config[section][key]

    def set(self, section, key, value):
        'Sets a config value'
        self.__config[section][key] = value

    def write(self):
        'Writes the settings'
        self.__write()

    def __read(self):
        'Returns the config parser for the config file'
        config = configparser.ConfigParser()
        with open(self.__configfile, 'r') as configfile:
            config.read_file(configfile)
        return config

    def __write(self):
        'Writes the config file for the given config'
        with open(self.__configfile, 'w') as configfile:
            self.__config.write(configfile)

class ConfigDialog(QDialog):
    'Dialog class for configuration dialog'
    def __init__(self, parent=0):
        'Initializes the dialog'
        super(ConfigDialog, self).__init__(parent)

        self.__config = Config()
        # create form elements
        apiLabel = QLabel('API-Key')
        self.apiLine = QLineEdit()
        self.apiLine.setText(self.__config.get('General', 'apikey'))
        domainLabel = QLabel('Domain')
        self.domainLine = QLineEdit()
        self.domainLine.setText(self.__config.get('General', 'domain'))
        appPathLabel = QLabel('Path to API')
        self.appPathLine = QLineEdit()
        self.appPathLine.setText(self.__config.get('General', 'resource'))
        gitDirLabel = QLabel('Git directory')
        self.gitDirLine = QLineEdit()
        self.gitDirLine.setText(self.__config.get('Git', 'dir'))
        self.submitButton = QPushButton('&Save')

        # create form layout
        formLayout = QGridLayout()
        formLayout.addWidget(apiLabel, 0, 0)
        formLayout.addWidget(self.apiLine, 0, 1)
        formLayout.addWidget(domainLabel, 1, 0)
        formLayout.addWidget(self.domainLine, 1, 1)
        formLayout.addWidget(appPathLabel, 2, 0)
        formLayout.addWidget(self.appPathLine, 2, 1)
        formLayout.addWidget(gitDirLabel, 3, 0)
        formLayout.addWidget(self.gitDirLine, 3, 1)

        # create main layout
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(self.submitButton)
        # connect submit button with submit action
        self.submitButton.clicked.connect(self.__submitForm)

        self.setLayout(mainLayout)
        self.setWindowTitle('Configuration')

    def __submitForm(self):
        'Submits the form'
        apiKey = self.apiLine.text()
        domain = self.domainLine.text()
        resource = self.appPathLine.text()
        gitDir = self.gitDirLine.text()

        self.__config.set('Git', 'dir', gitDir)
        self.__config.set('General', 'apikey', apiKey)
        self.__config.set('General', 'domain', domain)
        self.__config.set('General', 'resource', resource)
        self.__config.write()
        self.hide()
