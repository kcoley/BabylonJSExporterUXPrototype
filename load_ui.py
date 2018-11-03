import os
import sys
 
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QCheckBox

import site
site.addsitedir("E:\\GitHub\\BabylonJSExporterUXPrototype")
import exporter_window
from exporter_window.exporter_window import ExporterWindow
 
 
if __name__ == "__main__":
    ui_file=os.path.join("E:\\GitHub\\BabylonJSExporterUXPrototype","ui", "babylonjsExporter.ui")
    print(ui_file)
    w = ExporterWindow(ui_file)
    geometry_properties = w.get_geometry_properties()
    print(geometry_properties)
    settings_properties = w.get_settings_properties()

    
    print(settings_properties)

    w.show()
