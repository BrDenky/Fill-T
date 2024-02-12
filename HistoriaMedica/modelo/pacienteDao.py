from conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET fecha = "{persona.fecha}", nombre = "{persona.nombre}",
            apellidoPaterno = "{persona.apellidoPaterno}", ci = "{persona.ci}", edad = "{persona.edad}",
            telefono = "{persona.telefono}", domicilio = "{persona.domicilio}", correo = "{persona.correo}",
            motivo = "{persona.motivo}", activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "Editar Paciente"
        mensaje = "Paciente Editado Exitosamente"
        messagebox.showinfo(title,mensaje)
    except:
        title = "Editar Paciente"
        mensaje = "Error al editar Paciente"
        messagebox.showerror(title,mensaje)


def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (fecha, nombre, apellidoPaterno, ci, edad, telefono, domicilio, correo,
            motivo, activo) VALUES ("{persona.fecha}","{persona.nombre}","{persona.apellidoPaterno}","{persona.ci}",
            "{persona.edad}","{persona.telefono}","{persona.domicilio}","{persona.correo}","{persona.motivo}",1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "Registrar Paciente"
        mensaje = "Paciente Registrado Exitosamente"
        messagebox.showinfo(title,mensaje)
    except:
        title = "Registrar Paciente"
        mensaje = "Error al Registrar Paciente"
        messagebox.showerror(title,mensaje)

def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = "SELECT * FROM Persona WHERE activo = 1"

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = "Datos"
        mensaje = "Registros No Existen"
        messagebox.showwarning(title,mensaje)
    return listaPersona

def listarPacienteCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f"SELECT * FROM Persona {where}"

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = "Datos"
        mensaje = "Registros No Existen"
        messagebox.showwarning(title,mensaje)
    return listaPersona



def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "Eliminar Paciente"
        mensaje = "Paciente Eliminado Exitosamente"
        messagebox.showinfo(title,mensaje)
    except:
        title = "Eliminar Paciente"
        mensaje = "Error al eliminar Paciente"
        messagebox.showwarning(title,mensaje)



class Persona:
    def __init__(self, fecha, nombre, apellidoPaterno, ci, edad, telefono, domicilio, correo, motivo):
        self.idPersona = None
        self.fecha = fecha
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.ci = ci
        self.edad = edad
        self.telefono = telefono
        self.domicilio = domicilio
        self.correo = correo
        self.motivo = motivo

    def __str__(self):
        return f"Persona[{self.fecha},{self.nombre},{self.apellidoPaterno},{self.ci},{self.edad},{self.telefono},{self.domicilio},{self.correo},{self.motivo}]"