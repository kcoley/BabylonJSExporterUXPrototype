import sys
 
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

import site
site.addsitedir("E:\\")
import qtExamples
from qtExamples.exporter_window import ExporterWindow
 
 
if __name__ == "__main__":
    ui_file="E:\\qtDesignerProjects\\test\\untitled\\babylonjsExporter.ui"
    w = ExporterWindow(ui_file)
    geometry_properties = w.get_geometry_properties()
    print(geometry_properties)
    settings_properties = w.get_settings_properties()
    print(settings_properties)

    w.show()
