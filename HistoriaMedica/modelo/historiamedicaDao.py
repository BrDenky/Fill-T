from conexion import ConexionDB
from tkinter import messagebox


def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f"SELECT h.idHistoriaMedica, p.apellidoPaterno as Apellidos, h.fechaHistoria, h.motivo, h.tratamiento, h.detalle FROM historiaMedica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}"

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except:
        title = "Listar Historia"
        mensaje = "Error al Listar Historia Médica"
        messagebox.showerror(title,mensaje)
    
    return listaHistoria
    
    

#GUARDAR HISTORIA EN TOPAGREGARHISTORIA
def guardarHistoria(idPersona, fechaHistoria, motivo, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaMedica (idPersona, fechaHistoria, motivo, tratamiento, detalle) VALUES
            ({idPersona},"{fechaHistoria}","{motivo}","{tratamiento}","{detalle}")"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "Registro Historia Médica"
        mensaje = "Historia Registrada"
        messagebox.showinfo(title,mensaje)
    except:
        title = "Registro Historia Médica"
        mensaje = "Error al registrar Historia Médica"
        messagebox.showerror(title,mensaje)

#ELIMINAR HISTORIA EN TOPAGREGARHISTORIA
def eliminarHistoria(idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"DELETE FROM historiaMedica WHERE idHistoriaMedica = {idHistoriaMedica}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "Eliminar Historia"
        mensaje = "Historia médica eliminada exitosamente"
        messagebox.showinfo(title,mensaje)
    except Exception as e:
        title = "Eliminar Historia"
        mensaje = f"Error al eliminar: {str(e)}"
        messagebox.showerror(title, mensaje)
        
#EDITAR HISTORIA EN TOPAGREGARHISTORIA
def editarHistoria(fechaHistoria, motivo, tratamiento, detalle, idHistoriaMedica):
    conexion= ConexionDB()
    sql = f"""UPDATE historiaMedica SET fechaHistoria = "{fechaHistoria}", motivo = "{motivo}", tratamiento = "{tratamiento}", detalle = "{detalle}" WHERE idHistoriaMedica = {idHistoriaMedica}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "Editar Historia"
        mensaje = "Editada Exitosamente"
        messagebox.showinfo(title,mensaje)
    except:
        title = "Editar Historia"
        mensaje = "Error al Editar"
        messagebox.showerror(title,mensaje)




class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, tratamiento, detalle):
        self.idHistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.tratamiento = tratamiento
        self.detalle = detalle

    def __str__(self):
        return f"historiaMedica[{self.idPersona},{self.fechaHistoria},{self.motivo},{self.tratamiento},{self.detalle}]"
    