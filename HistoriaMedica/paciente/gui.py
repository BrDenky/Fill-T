import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel,messagebox, LabelFrame
import sys
sys.path.append("C:\\Users\\ASUS\\Desktop\\Trax\\Fill-T\\HistoriaMedica\\modelo")
from pacienteDao import Persona, guardarDatoPaciente, listarPacienteCondicion, listar, editarDatoPaciente, eliminarPaciente
from historiamedicaDao import historiaMedica, guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria

import tkcalendar as tc
from tkcalendar import *
from datetime import datetime


class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root,width=1280,height=720)
        self.root = root
        self.pack()
        self.config(bg="#15274b")
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idhistoriaMedica = None
        self.idhistoriaMedicaEditar = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()


    def camposPaciente(self):
        #LABELS DEL PACIENTE
        self.lblFecha = tk.Label(self, text="Fecha: ")
        self.lblFecha.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblFecha.grid(column=0,row=0,padx=10,pady=5)

        self.lblNombre = tk.Label(self, text="Nombre: ")
        self.lblNombre.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblNombre.grid(column=0,row=1,padx=10,pady=5)

        self.lblApellidoPaterno = tk.Label(self, text="Apellido: ")
        self.lblApellidoPaterno.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblApellidoPaterno.grid(column=0,row=2,padx=10,pady=5)

        self.lblCi = tk.Label(self, text="Cédula: ")
        self.lblCi.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblCi.grid(column=0,row=3,padx=10,pady=5)

        self.lblEdad = tk.Label(self, text="Edad: ")
        self.lblEdad.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblEdad.grid(column=0,row=4,padx=10,pady=5)

        self.lblTeléfono = tk.Label(self, text="Teléfono: ")
        self.lblTeléfono.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblTeléfono.grid(column=0,row=5,padx=10,pady=5)
                
        self.lblDomicilio = tk.Label(self, text="Domicilio: ")
        self.lblDomicilio.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblDomicilio.grid(column=0,row=6,padx=10,pady=5)

        self.lblCorreo = tk.Label(self, text="Correo: ")
        self.lblCorreo.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblCorreo.grid(column=0,row=7,padx=10,pady=5)

        self.lblMotivo = tk.Label(self, text="Motivo Consulta: ")
        self.lblMotivo.config(font=("Arial",15,"bold"), bg="#c2d1ff", width=15) #podemos añadir el color al bg
        self.lblMotivo.grid(column=0,row=8,padx=10,pady=5)


        #CREANDO ENTRYES PARA CADA LABEL DEL PACIENTE
        self.svFecha = tk.StringVar()
        self.entryFecha = tk.Entry(self,textvariable=self.svFecha)
        self.entryFecha.config(width=10,font=("Arial",15))
        self.entryFecha.grid(column=1,row=0,padx=10,pady=5)

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self,textvariable=self.svNombre)
        self.entryNombre.config(width=40,font=("Arial",15))
        self.entryNombre.grid(column=1,row=1,padx=10,pady=5,columnspan=2)

        self.svApellidoPaterno = tk.StringVar()
        self.entryApellidoPaterno = tk.Entry(self,textvariable=self.svApellidoPaterno)
        self.entryApellidoPaterno.config(width=40,font=("Arial",15))
        self.entryApellidoPaterno.grid(column=1,row=2,padx=10,pady=5,columnspan=2)

        self.svCi = tk.StringVar()
        self.entryCi = tk.Entry(self,textvariable=self.svCi)
        self.entryCi.config(width=40,font=("Arial",15))
        self.entryCi.grid(column=1,row=3,padx=10,pady=5,columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self,textvariable=self.svEdad)
        self.entryEdad.config(width=40,font=("Arial",15))
        self.entryEdad.grid(column=1,row=4,padx=10,pady=5,columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self,textvariable=self.svTelefono)
        self.entryTelefono.config(width=40,font=("Arial",15))
        self.entryTelefono.grid(column=1,row=5,padx=10,pady=5,columnspan=2)

        self.svDomicilio = tk.StringVar()
        self.entryDomicilio = tk.Entry(self,textvariable=self.svDomicilio)
        self.entryDomicilio.config(width=40,font=("Arial",15))
        self.entryDomicilio.grid(column=1,row=6,padx=10,pady=5,columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self,textvariable=self.svCorreo)
        self.entryCorreo.config(width=40,font=("Arial",15))
        self.entryCorreo.grid(column=1,row=7,padx=10,pady=5,columnspan=2)

        self.svMotivo = tk.StringVar()
        self.entryMotivo = tk.Entry(self,textvariable=self.svMotivo)
        self.entryMotivo.config(width=40,font=("Arial",15))
        self.entryMotivo.grid(column=1,row=8,padx=10,pady=5,columnspan=2)

        #AGREGANDO BOTONES INTERACTIVOS
        self.btnNuevo = tk.Button(self,text="Nuevo", command=self.habilitar)
        self.btnNuevo.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#1658A2", cursor="hand2",
                            activebackground="#41599f")
        self.btnNuevo.grid(column=0,row=9,pady=5)

        self.btnGuardar = tk.Button(self,text="Guardar", command = self.guardarPaciente)
        self.btnGuardar.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#005600", cursor="hand2",
                            activebackground="#003A00")
        self.btnGuardar.grid(column=1,row=9,pady=5)

        self.btnCancelar = tk.Button(self,text="Cancelar", command=self.deshabilitar)
        self.btnCancelar.config(width=20,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#770907", cursor="hand2",
                            activebackground="#560605")
        self.btnCancelar.grid(column=2,row=9,pady=5)
        


        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarCi = tk.Label(self, text = "Buscar Cédula: ")
        self.lblBuscarCi.config(font=("Arial",15,"bold"),bg="#CDD8FF",width=14)
        self.lblBuscarCi.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido = tk.Label(self, text = "Buscar Apellido: ")
        self.lblBuscarApellido.config(font=("Arial",15,"bold"),bg="#CDD8FF", width=14)
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #ENTRYS BUSCADOR
        self.svBuscarCi = tk.StringVar()
        self.entryBuscarCi = tk.Entry(self, textvariable=self.svBuscarCi)
        self.entryBuscarCi.config(width=20, font=("Arial",15))
        self.entryBuscarCi.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20, font=("Arial",15))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        #BOTON PARA EL BUSCADOR Y LIMPIADOR
        self.btnBuscarCondicion = tk.Button(self,text="Buscar", command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=10,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#1658A2", cursor="hand2",
                            activebackground="#41599f")
        self.btnBuscarCondicion.grid(column=3,row=2,padx=10, pady=5, columnspan=2)

        self.btnLimpiarBuscador = tk.Button(self,text="Limpiar", command=self.LimpiarBuscador)
        self.btnLimpiarBuscador.config(width=10,font=("Arial",12,"bold"),fg="#DAD5D6",bg="#770907", cursor="hand2",
                            activebackground="#560605")
        self.btnLimpiarBuscador.grid(column=4,row=2,padx=10, pady=5, columnspan=2)


        #BOTON CALENDARIO
        self.btnCalendario = tk.Button(self,text="Calendario", command=self.vistaCalendario)
        self.btnCalendario.config(width=10,font=("Arial",12,"bold"),bg="#c2d1ff", cursor="hand2",
                            activebackground="#41599f")
        self.btnCalendario.grid(column=2,row=0,padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        # Top Level Crea una ventana flotante
        self.calendario = Toplevel()
        self.calendario.title("FECHA")
        self.calendario.resizable(0, 0)
        self.calendario.config(bg="#CDD8FF")
        
        # Creamos el calendario con sus fechas
        self.svCalendario = StringVar()

        # Inicializamos self.svCalendario con una fecha válida
        fecha_valida = datetime.now().strftime("%d-%m-%Y")
        self.svCalendario.set(fecha_valida)

        calendar = tc.Calendar(self.calendario,
                                    selectmode="day",
                                    locale="es_ES",
                                    bg="#777777", fg="#FFFFFF", headersbackground="#B6DDFE",
                                    date_pattern="dd-mm-Y")
        calendar.pack()

        # Se configura el textvariable después de crear el calendario
        calendar.config(textvariable=self.svCalendario, cursor="hand2")

        #TRACE ENVIAR FECHA
        self.svCalendario.trace("w",self.enviarFecha)

    def enviarFecha(self, *args):
        self.svFecha.set("" + self.svCalendario.get())


    def LimpiarBuscador(self):
        self.svBuscarApellido.set("")
        self.svBuscarCi.set("")
        self.tablaPaciente()


    def buscarCondicion(self):
        if len(self.svBuscarCi.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if len(self.svBuscarCi.get()) > 0:
                where += " AND ci = '" + self.svBuscarCi.get() + "'"
            if len(self.svBuscarApellido.get()) > 0:
                where += " AND apellidoPaterno LIKE '" + self.svBuscarApellido.get() + "%' AND activo = 1"

            self.tablaPaciente(where)
        else:
            self.tablaPaciente()




    def guardarPaciente(self):
        persona = Persona( 
            self.svFecha.get(),
            self.svNombre.get(),
            self.svApellidoPaterno.get(),
            self.svCi.get(),
            self.svEdad.get(),
            self.svTelefono.get(),
            self.svDomicilio.get(),
            self.svCorreo.get(),
            self.svMotivo.get()
        )
        
        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

        
        self.deshabilitar()
        self.tablaPaciente()

    def habilitar(self):
        #self.idPersona == None        
        self.svFecha.set(" ")
        self.svNombre.set(" ")
        self.svApellidoPaterno.set(" ")
        self.svEdad.set(" ")
        self.svTelefono.set(" ")
        self.svDomicilio.set(" ")
        self.svCi.set(" ")
        self.svCorreo.set(" ")
        self.svMotivo.set(" ")

        self.entryFecha.config(state="normal")
        self.entryNombre.config(state="normal")
        self.entryApellidoPaterno.config(state="normal")
        self.entryEdad.config(state="normal")
        self.entryTelefono.config(state="normal")
        self.entryDomicilio.config(state="normal")
        self.entryCi.config(state="normal")
        self.entryCorreo.config(state="normal")
        self.entryMotivo.config(state="normal")

        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnCalendario.config(state="normal")



    def deshabilitar(self):
        self.idPersona = None
        self.svFecha.set(" ")
        self.svNombre.set(" ")
        self.svApellidoPaterno.set(" ")
        self.svEdad.set(" ")
        self.svTelefono.set(" ")
        self.svDomicilio.set(" ")
        self.svCi.set(" ")
        self.svCorreo.set(" ")
        self.svMotivo.set(" ")

        self.entryFecha.config(state="disabled")
        self.entryNombre.config(state="disabled")
        self.entryApellidoPaterno.config(state="disabled")
        self.entryEdad.config(state="disabled")
        self.entryTelefono.config(state="disabled")
        self.entryDomicilio.config(state="disabled")
        self.entryCi.config(state="disabled")
        self.entryCorreo.config(state="disabled")
        self.entryMotivo.config(state="disabled")

        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")
        self.btnCalendario.config(state="disabled")


    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarPacienteCondicion(where)
        else:
            self.listaPersona = listar()
            #self.listaPersona.reverse()
        
        self.tabla = ttk.Treeview(self, column=("Fecha","Nombre","Apellido","Edad","Telefono","Domicilio","Cédula","Correo","Motivo"))
        self.tabla.grid(column=0, row=10, columnspan=9,sticky="nsew")
        self.scroll = ttk.Scrollbar(self, orient="vertical", command = self.tabla.yview)
        self.scroll.grid(row=10,column=11,sticky="nse")

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure("evenrow", background="#C5EAFE")

        self.tabla.heading("#0",text="ID")
        self.tabla.heading("#1",text="Fecha")
        self.tabla.heading("#2",text="Nombre")
        self.tabla.heading("#3",text="Apellido")
        self.tabla.heading("#4",text="Cédula")
        self.tabla.heading("#5",text="Edad")
        self.tabla.heading("#6",text="Teléfono")
        self.tabla.heading("#7",text="Domicilio")
        self.tabla.heading("#8",text="Correo")
        self.tabla.heading("#9",text="Motivo")

        self.tabla.column("#0",anchor=W, width=20)
        self.tabla.column("#1",anchor=W, width=50)
        self.tabla.column("#2",anchor=W, width=50)
        self.tabla.column("#3",anchor=W, width=50)
        self.tabla.column("#4",anchor=W, width=60)
        self.tabla.column("#5",anchor=W, width=20)
        self.tabla.column("#6",anchor=W, width=50)
        self.tabla.column("#7",anchor=W, width=50)
        self.tabla.column("#8",anchor=W, width=160)
        self.tabla.column("#9",anchor=W, width=150)



        for p in self.listaPersona:
            self.tabla.insert("",0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10]), tags=("evenrow",))

        self.btnEditarPaciente = tk.Button(self, text="Editar Paciente", command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=("Arial",15,"bold"),fg="#DAD5D6",bg="#170095", activebackground="#9379E0",cursor="hand2")
        self.btnEditarPaciente.grid(row=11, column=0,padx=10,pady=5)

        self.btnEliminarPaciente = tk.Button(self, text="Eliminar Paciente", command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=("Arial",15,"bold"),fg="#DAD5D6",bg="#170095", activebackground="#9379E0",cursor="hand2")
        self.btnEliminarPaciente.grid(row=11, column=1,padx=10,pady=5)

        self.btnHistorialPaciente = tk.Button(self, text="Historial Paciente", command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20,font=("Arial",15,"bold"),fg="#DAD5D6",bg="#170095", activebackground="#9379E0",cursor="hand2")
        self.btnHistorialPaciente.grid(row=11, column=2,padx=10,pady=5)

        
        self.btnHistorialPaciente = tk.Button(self, text="Salir", command=self.root.destroy)
        self.btnHistorialPaciente.config(width=20,font=("Arial",15,"bold"),fg="#DAD5D6",bg="#770907", cursor="hand2", activebackground="#560605")
        self.btnHistorialPaciente.grid(row=11, column=4,padx=10,pady=5)

    def historiaMedica(self):

        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())["text"]
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())["text"]
            
            if (self.idPersona > 0):
                idPersona = self.idPersona

            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title("HISTORIAL MÉDICO")
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.config(bg="#CDD8FF")

            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=("Apellido","fechaHistoria","motivo","tratamiento","detalle"))
            self.tablaHistoria.grid(row=0,column=0, columnspan=6, sticky="nse")
            #CREAMOS SCROLLBAR
            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaMedica, orient="vertical", command = self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0,column=7,sticky="nse")

            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading("#0", text = "ID")
            self.tablaHistoria.heading("#1", text = "Apellidos")
            self.tablaHistoria.heading("#2", text = "Fecha y Hora")
            self.tablaHistoria.heading("#3", text = "Motivo")
            self.tablaHistoria.heading("#4", text = "Tratamiento")
            self.tablaHistoria.heading("#5", text = "Detalle")

            self.tablaHistoria.column("#0", anchor=W, width=50)
            self.tablaHistoria.column("#1", anchor=W, width=100)
            self.tablaHistoria.column("#2", anchor=W, width=100)
            self.tablaHistoria.column("#3", anchor=W, width=250)
            self.tablaHistoria.column("#4", anchor=W, width=250)
            self.tablaHistoria.column("#5", anchor=W, width=250)

            for p in self.listaHistoria:
                self.tablaHistoria.insert("",0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5]))

            self.btnGuardarHistoria = tk.Button(self.topHistoriaMedica, text="Agregar Historia", command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20,font=("Arial",12,"bold"), fg="#DAD5D6",bg="#005600", cursor="hand2", activebackground="#003A00")
            self.btnGuardarHistoria.grid(row=2,column=0,padx=10,pady=5)

            self.btnEditarHistoria = tk.Button(self.topHistoriaMedica, text="Editar Historia", command=self.topeditarHistorialMedico)
            self.btnEditarHistoria.config(width=20,font=("Arial",12,"bold"), fg="#DAD5D6", bg="#002771", cursor="hand2", activebackground="#7198E0")
            self.btnEditarHistoria.grid(row=2,column=1,padx=10,pady=5)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaMedica, text="Eliminar Historia", command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20,font=("Arial",12,"bold"), fg="#DAD5D6",bg="#770907", cursor="hand2", activebackground="#560605")
            self.btnEliminarHistoria.grid(row=2,column=2,padx=10,pady=5)

            #self.btnSalirHistoria = tk.Button(self.topHistoriaMedica, text="Salir", command=self.salirTop)
            #self.btnSalirHistoria.config(width=20,font=("Arial",12,"bold"), fg="#DAD5D6", bg="#000000", cursor="hand2", activebackground="#1E1E1E")
            #self.btnSalirHistoria.grid(row=2,column=3,padx=10,pady=5)
        except:
            title = "Historia Médica"
            mensaje = "Seleccione un Paciente"
            messagebox.showerror(title,mensaje)


    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title("Agregar Historia")
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.config(bg="#15274b")

        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg="#15274b")
        self.frameDatosHistoria.pack(fill="both",expand="yes", pady=10, padx=20)


        #CREAMOS LABELS PARA  HISTORIA MÉDICA
        self.lblMotivoHistoria = tk.Label(self.frameDatosHistoria, text="Motivo de la consulta", width=20, font=("Arial",12,"bold"), bg="#CDD8FF")
        self.lblMotivoHistoria.grid(row=0,column=0, padx=5, pady=3, sticky="nse")

        self.lblTratamientoHistoria = tk.Label(self.frameDatosHistoria, text="Tratamiento", width=20, font=("Arial",12,"bold"), bg="#CDD8FF")
        self.lblTratamientoHistoria.grid(row=2,column=0, padx=5, pady=3, sticky="nse")

        self.lblDetalleHistoria = tk.Label(self.frameDatosHistoria, text="Detalle", width=20, font=("Arial",12,"bold"), bg="#CDD8FF")
        self.lblDetalleHistoria.grid(row=4,column=0, padx=5, pady=3, sticky="nse")


        #ENTRYS PARA LOS LABELS DE HISTORIA MÉDICA
        self.svMotivoHistoria = tk.StringVar()
        self.motivoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivoHistoria)
        self.motivoHistoria.config(width=48, font=("Arial",15))
        self.motivoHistoria.grid(row=1, column=0, padx=5, pady=3, columnspan=2)

        self.svTratamientoHistoria = tk.StringVar()
        self.tratamientoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamientoHistoria)
        self.tratamientoHistoria.config(width=48, font=("Arial",15))
        self.tratamientoHistoria.grid(row=3, column=0, padx=5, pady=3, columnspan=2)

        self.svDetalleHistoria = tk.StringVar()
        self.detalleHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svDetalleHistoria)
        self.detalleHistoria.config(width=48, font=("Arial",15))
        self.detalleHistoria.grid(row=5, column=0, padx=5, pady=3, columnspan=2)

        #FRAME 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg="#15274b")
        self.frameFechaHistoria.pack(fill="both", expand="yes", padx=20, pady=20)

        #LABEL FECHA AGREGAR HISTORIA
        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text="Fecha y Hora", width="20", font=("Arial",15,"bold"),bg="#CDD8FF")
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)

        #ENTRY FECHA AGREGAR HISTORIA
        self.svFechaHistoria = tk.StringVar()
        self.entryfechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryfechaHistoria.config(width=15, font=("Arial",15))
        self.entryfechaHistoria.grid(row=1, column=1, padx=5, pady=3)

        #TRAER FECHA Y HORA ACTUAL
        self.svFechaHistoria.set(datetime.today().strftime("%d-%m-%Y %H:%M"))

        #BOTÓN AGREGAR HISTORIA
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text="Guardar Historia", command=self.agregaHistorialMedico)
        self.btnAgregarHistoria.config(width=20, font=("Arial",15, "bold"),fg="#DAD5D6",bg="#005600", cursor="hand2", activebackground="#003A00")
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text="Salir", command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=("Arial",15, "bold"),fg="#DAD5D6",bg="#770907", cursor="hand2", activebackground="#560605")
        self.btnSalirAgregarHistoria.grid(row=2, column=1, padx=10, pady=5)

    #DEFINIMOS FUNCIONALIDAD AL BOTON AGREGAR HISTORIA EN TOPAGREGARHISTORIA
    def agregaHistorialMedico(self):
        try:
            if self.idhistoriaMedica == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechaHistoria.get(), self.svMotivoHistoria.get(), self.svTratamientoHistoria.get(), self.svDetalleHistoria.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except Exception as e:
            title = "Agregar Historia"
            mensaje = f"Error al Agregar Historia: {str(e)}"
            messagebox.showerror(title, mensaje)

    #DEFINIMOS FUNCIONALIDAD AL BOTON ELIMINAR HISTORIA EN TOPAGREGARHISTORIA
    def eliminarHistorialMedico(self):
        try:
            self.idhistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())["text"]
            eliminarHistoria(self.idhistoriaMedica)

            self.idhistoriaMedica = None
            self.topHistoriaMedica.destroy()
        except Exception as e:
            title = "Eliminar Historia"
            mensaje = f"Error al eliminar: {str(e)}"
            messagebox.showerror(title, mensaje)
    

    #DEFINIMOS FUNCIONALIDAD EL BOTON EDITAR HISTORIA EN TOPAGREGARHISTORIA
    def topeditarHistorialMedico(self):
        try:
            self.idhistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())["text"]
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())["values"][1]
            self.motivoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())["values"][2]
            self.tratamientoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())["values"][3]
            self.detalleHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())["values"][4]

            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title("EDITAR HISTORIA MEDICA")
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.config(bg="#15274b")

            #CREANDO FRAMES
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg="#15274b")
            self.frameEditarHistoria.pack(fill="both", expand="yes", padx=20, pady=10)

            #CREANDO LABELS DE ESTE NUEVO FRAME
            self.lblMotivoEditar = tk.Label(self.frameEditarHistoria, text="Motivo de la Consulta", width=20, font=("Arial",12,"bold"),bg="#CDD8FF")
            self.lblMotivoEditar.grid(row=0, column=0, padx=5, pady=3, sticky="nse")

            self.lblTratamientoEditar = tk.Label(self.frameEditarHistoria, text="Tratamiento", width=20, font=("Arial",12,"bold"),bg="#CDD8FF")
            self.lblTratamientoEditar.grid(row=2, column=0, padx=5, pady=3, sticky="nse")

            self.lblDetalleEditar = tk.Label(self.frameEditarHistoria, text="Detalles", width=20, font=("Arial",12,"bold"),bg="#CDD8FF")
            self.lblDetalleEditar.grid(row=4, column=0, padx=5, pady=3, sticky="nse")


            #CREANDO ENTRYS PARA ESTOS LABELS
            self.svMotivoEditar = tk.StringVar()
            self.entryMotivoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoEditar)
            self.entryMotivoEditar.config(width=48, font=("Arial",15))
            self.entryMotivoEditar.grid(row=1, column=0, padx=5, pady=3, columnspan=2)
    
            self.svTratamientoEditar = tk.StringVar()
            self.entryTratamientoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTratamientoEditar)
            self.entryTratamientoEditar.config(width=48, font=("Arial",15))
            self.entryTratamientoEditar.grid(row=3, column=0, padx=5, pady=3, columnspan=2)

            self.svDetalleEditar = tk.StringVar()
            self.entryDetalleEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svDetalleEditar)
            self.entryDetalleEditar.config(width=48, font=("Arial",15))
            self.entryDetalleEditar.grid(row=5, column=0, padx=5, pady=3, columnspan=2)


            #CREAMOS UN SEGUNDO FRAM PARA FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(bg="#15274b")
            self.frameFechaEditar.pack(fill="both", expand="yes", padx=20, pady=10)
            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text="Fecha y Hora", width=20, font=("Arial",15,"bold"),bg="#CDD8FF")
            self.lblFechaHistoriaEditar.grid(row=1, column=0, padx=5, pady=3)
            #ENTRY PARA EL LABEL FECHA EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=15, font=("Arial",15))
            self.entryFechaHistoriaEditar.grid(row=1, column=1, padx=5, pady=3)

            #INSERTAR LOS VALORES PREVIOS A LOS ENTRYS PARA EDITARLOS
            self.entryMotivoEditar.insert(0, self.motivoHistoriaEditar)
            self.entryTratamientoEditar.insert(0, self.tratamientoHistoriaEditar)
            self.entryDetalleEditar.insert(0, self.detalleHistoriaEditar)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)

            #BOTONES EDITAR HISTORIA
            self.btnEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text="Guardar Cambios", command=self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20, font=("Arial",15,"bold"),fg="#DAD5D6",bg="#005600", cursor="hand2", activebackground="#003A00")
            self.btnEditarHistoriaMedica.grid(row=2, column=0, padx=10, pady=5)

            self.btnSalirHistoriaMedica = tk.Button(self.frameFechaEditar, text="Salir", command=self.topEditarHistoria.destroy)
            self.btnSalirHistoriaMedica.config(width=20, font=("Arial",15,"bold"),fg="#DAD5D6",bg="#770907", cursor="hand2", activebackground="#560605")
            self.btnSalirHistoriaMedica.grid(row=2, column=1, padx=10, pady=5)

            if self.idhistoriaMedicaEditar == None:
                self.idhistoriaMedicaEditar = self.idhistoriaMedica

            self.idhistoriaMedica = None
        except:
            title = "Editar Historia"
            mensaje = "Error al Editar Historia"
            messagebox.showerror(title,mensaje)

    #DAMOS FUNCIONALIDAD AL BOTON GUARDAR CAMBIOS EN HISTORIA EDITAR
    def historiaMedicaEditar(self):
        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoEditar.get(), self.svTratamientoEditar.get(), self.svDetalleEditar.get(), self.idhistoriaMedicaEditar)
            self.idhistoriaMedicaEditar = None
            self.idhistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title= "Guardar Cambios"
            mensaje = "No se pudo guardar los Cambios"
            messagebox.showerror(title,mensaje)
            self.topEditarHistoria.destroy()




    def salirTop(self):
        self.topHistoriaMedica.destroy()

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"] #TRAE EL ID
            self.fechaPaciente = self.tabla.item(self.tabla.selection())["values"][0]
            self.nombrePaciente = self.tabla.item(self.tabla.selection())["values"][1]
            self.apellidoPaciente = self.tabla.item(self.tabla.selection())["values"][2]
            self.ciPaciente = self.tabla.item(self.tabla.selection())["values"][3]
            self.edadPaciente = self.tabla.item(self.tabla.selection())["values"][4]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())["values"][5]
            self.domicilioPaciente = self.tabla.item(self.tabla.selection())["values"][6]
            self.correoPaciente = self.tabla.item(self.tabla.selection())["values"][7]
            self.motivoPaciente = self.tabla.item(self.tabla.selection())["values"][8]

            self.habilitar()


            self.entryFecha.insert(0,self.fechaPaciente)
            self.entryNombre.insert(0,self.nombrePaciente)
            self.entryApellidoPaterno.insert(0,self.apellidoPaciente)
            self.entryCi.insert(0,self.ciPaciente)
            self.entryEdad.insert(0,self.edadPaciente)
            self.entryTelefono.insert(0,self.telefonoPaciente)
            self.entryDomicilio.insert(0,self.domicilioPaciente)
            self.entryCorreo.insert(0,self.correoPaciente)
            self.entryMotivo.insert(0,self.motivoPaciente)


        except:
            title = "Editar Paciente"
            mensaje = "Error al editar paciente"
            messagebox.showerror(title,mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"]
            eliminarPaciente(self.idPersona)
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = "Eliminar Paciente"
            mensaje = "No se pudo eliminar Paciente"
            messagebox.showwarning(title,mensaje)

















