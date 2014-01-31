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
    def __init__(self, parent=None):
        'Initializes the dialog'
        super(ConfigDialog, self).__init__(parent)

        self.__config = Config()
        # create form elements
        apiLabel = QLabel('API-Key')
        self.apiLine = QLineEdit()
        self.apiline.setText(self.__config.get('General', 'apikey'))
        gitDirLabel = QLabel('Git directory')
        self.gitDirLine = QLineEdit()
        self.gitDirLine.setText(self.__config.get('Git', 'dir'))
        self.submitButton = QPushButton('&Submit')

        # create layout
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(apiLabel)
        buttonLayout.addWidget(self.apiLine)
        buttonLayout.addWidget(gitDirLabel)
        buttonLayout.addWidget(self.gitDirLine)
        buttonLayout.addWidget(self.submitButton)
        # connect submit button with submit action
        self.submitButton.clicked.connect(self.submitForm)

        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonLayout, 0, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle('Configuration')

    def submitForm(self):
        'Submits the form'
        apiKey = self.apiLine.text()
        gitDir = self.gitDirLine.text()

        self.__config.set('Git', 'dir', gitDir)
        self.__config.set('General', 'apikey', apiKey)
        self.__config.write()
