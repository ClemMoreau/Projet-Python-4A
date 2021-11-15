from PyQt5 import QtWidgets
import settings, sys

class Main:
    
    def main():
        #launch the application
        mainApp = QtWidgets.QApplication(sys.argv)
        
        #get the screen size used for the lenght of drawn polygons 
        maxScreenSize = (mainApp.primaryScreen().size().width(),
                         mainApp.primaryScreen().size().height())
        
        #call the first widget on the windows : settings
        settingWidget = settings.settings(maxScreenSize)
        
        #used to kill everything
        sys.exit(mainApp.exec_())
        

if __name__ == "__main__":
    Main.main()