from qgis.PyQt.QtWidgets import QAction
from qgis.utils import iface
from qgis.core import QgsProject


class Plugin:
    name = "import_all"

    def __init__(self):
        self.action = None

    def initGui(self):
        self.action = QAction("import_all", iface.mainWindow())
        self.action.setShortcut("Ctrl+R")
        self.action.triggered.connect(self.run)
        iface.addPluginToMenu(self.name, self.action)

    def unload(self):
        iface.removePluginMenu(self.name, self.action)

    def run(self):
        p = QgsProject.instance().fileName()
        if p:
            QgsProject.instance().read(p)
            print("Project reloaded")
