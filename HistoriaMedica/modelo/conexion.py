import sqlite3

class ConexionDB:
    def __init__(self):
        self.baseDatos = "C:\\Users\\ASUS\\Desktop\\Trax\\Fill-T\\HistoriaMedica\\database\\dbhistorial.db"
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()