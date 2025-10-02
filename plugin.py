import os
from qgis.PyQt.QtWidgets import QAction, QFileDialog
from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer


class Plugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):
        self.action = QAction("Import All Layers", self.iface.mainWindow())
        self.action.setShortcut("Ctrl+R")
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("import_all", self.action)

    def unload(self):
        self.iface.removePluginMenu("import_all", self.action)

    def run(self):
        folder = QFileDialog.getExistingDirectory(
            self.iface.mainWindow(), "Select Folder with Layers"
        )
        if not folder:
            return

        exts = {".shp", ".geojson", ".kml", ".tif"}
        for root, _, files in os.walk(folder):
            for f in files:
                path = os.path.join(root, f)
                ext = os.path.splitext(f)[1].lower()
                if ext in exts:
                    if ext == ".tif":
                        layer = QgsRasterLayer(path, os.path.basename(path))
                    else:
                        layer = QgsVectorLayer(path, os.path.basename(path), "ogr")
                    if layer.isValid():
                        QgsProject.instance().addMapLayer(layer)
