from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QLinearGradient
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        x = input("http://google.com")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(x))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar 
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back button
        back_btn = QAction("<<",self) 
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        #forward button 
        for_btn = QAction(">>",self)
        for_btn.triggered.connect(self.browser.forward)
        navbar.addAction(for_btn)


        #refresh button
        reload_btn = QAction('@',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        #home button
        home_btn = QAction("home",self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        #create search bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        #updating the search_box
        self.browser.urlChanged.connect(self.update_url)


        #create a method for navigate_home
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

        # create a method for navigate_to_url
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


        #creating method to updte the url in search_box
    def update_url(self,url):
        self.url_bar.setText(url.toString())
         
app = QApplication(sys.argv)
QApplication.setApplicationName("Google 2.0")

window = MainWindow()
app.exec_()