import sys
 
from PySide2 import QtGui
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

class ExporterWindow(object):
    """Creates an exporter window
    
    Arguments:
        object {object} -- Python object
    """

    def __init__(self, ui_file):
        """Initialize the exporter window
        
        Arguments:
            ui_file {str} -- Path to the Qt ui file
        """

        file = QFile(ui_file)
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(file)

    def show(self):
        """Show the exporter window
        """

        self.window.show()

    def get_geometry_properties(self):
        """Returns the geometry properties
        """
        data = {}
        data['optimize_vertices'] = self.window.btn_optimize_vertices.isChecked()
        data['export_hidden_objects'] = self.window.btn_export_hidden_objects.isChecked()
        data['skinning'] = self.window.btn_skinning.isChecked()
        data['blendshapes'] = self.window.btn_blendshapes.isChecked()

        return data
        
    def get_settings_properties(self):
        """Returns the settings properties
        """
        data = {}
        data['auto_save_maya_file'] = self.window.chk_auto_save_maya_file.isChecked()
        data['export_hidden_objects'] = self.window.chk_export_hidden_objects.isChecked()
        data['animation'] = self.window.chk_animation.isChecked()
        data['generate_manifest'] = self.window.chk_generate_manifest.isChecked()
        data['embed_media'] = self.window.chk_embed_media.isChecked()

        return data
        







