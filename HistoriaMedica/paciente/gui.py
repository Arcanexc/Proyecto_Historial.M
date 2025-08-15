import tkinter as tk
from tkinter import messagebox
from tkinter import Button, ttk, scrolledtext, Toplevel
from HistoriaMedica.modelo.conexion import ConexionDB
from HistoriaMedica.modelo.pacienteDao import Persona, GuardarDatoPaciente, ListarCondicion, ListarPacientes


class Frame(tk.Frame):  # clase para el frame de la ventana principal
    def __init__(self, root):   # constructor de la clase

        super().__init__(root, width=1280, height=720)  # super() es para llamar al constructor de la clase padre
        self.root = root                 # self es para referirse a la instancia de la clase
        self.idPersona = None  # Inicializa el atributo idPersona
        self.pack()
        self.config(bg="#C0C0C0")

        self.campo_paciente()
        self.DeshabilitarCampos()



    '''creamos campo de los pacientes'''


    def campo_paciente(self):   

        # LABEL

        self.lblNombre = tk.Label(self, text="Nombre: ")
        self.lblNombre.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblNombre.grid(row=0, column=0, padx=10, pady=10)

        self.lblAppaterno = tk.Label(self, text="Apellido Paterno: ")
        self.lblAppaterno.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblAppaterno.grid(row=1, column=0, padx=10, pady=10)

        self.lblApmaterno = tk.Label(self, text="Apellido Materno: ")
        self.lblApmaterno.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblApmaterno.grid(row=2, column=0, padx=10, pady=10)

        self.lblDni = tk.Label(self, text="DNI: ")
        self.lblDni.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblDni.grid(row=3, column=0, padx=10, pady=10)

        self.lblFecNacimiento = tk.Label(self, text="Fecha de Nacimiento: ")
        self.lblFecNacimiento.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblFecNacimiento.grid(row=4, column=0, padx=10, pady=10)


        self.lblEdad = tk.Label(self, text="Edad: ")
        self.lblEdad.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblEdad.grid(row=5, column=0, padx=10, pady=10)

        self.lblAntecedentes = tk.Label(self, text="Antecedentes: ")
        self.lblAntecedentes.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblAntecedentes.grid(row=6, column=0, padx=10, pady=10)

        self.lblCorreo = tk.Label(self, text="Correo: ")
        self.lblCorreo.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblCorreo.grid(row=7, column=0, padx=10, pady=10)

        self.lblTelefono = tk.Label(self, text="Telefono: ")
        self.lblTelefono.config(font=("Arial", 15, 'bold'), bg="#C0C0C0" )
        self.lblTelefono.grid(row=8, column=0, padx=10, pady=10)



        #ENTRYS

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('Arial',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=10, columnspan= 2)

        self.svAppaterno = tk.StringVar()
        self.entryAppaterno = tk.Entry(self, textvariable=self.svAppaterno)
        self.entryAppaterno.config(width=50, font=('Arial',15))
        self.entryAppaterno.grid(column=1, row=1, padx=10, pady=10, columnspan= 2)

        self.svApmaterno = tk.StringVar()
        self.entryApmaterno = tk.Entry(self, textvariable=self.svApmaterno)
        self.entryApmaterno.config(width=50, font=('Arial',15))
        self.entryApmaterno.grid(column=1, row=2, padx=10, pady=10, columnspan= 2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=('Arial',15))
        self.entryDni.grid(column=1, row=3, padx=10, pady=10, columnspan= 2)


        self.svFecNacimiento = tk.StringVar()
        self.entryFecNacimiento = tk.Entry(self, textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width=50, font=('Arial',15))
        self.entryFecNacimiento.grid(column=1, row=4, padx=10, pady=10, columnspan= 2)


        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('Arial',15))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=10, columnspan= 2)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50, font=('Arial',15))
        self.entryAntecedentes.grid(column=1, row=6, padx=10, pady=10, columnspan= 2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('Arial',15))
        self.entryCorreo.grid(column=1, row=7, padx=10, pady=10, columnspan= 2)

        
        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('Arial',15))
        self.entryTelefono.grid(column=1, row=8, padx=10, pady=10, columnspan= 2)



        #BUTTONS


        self.btnNuevo = tk.Button(self, text="Nuevo", command=self.HabilitarCampos)
        self.btnNuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',
                         bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=10)

        self.btnGuardar = tk.Button(self, text="Guardar", command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',
                         bg='#000000', cursor='hand2', activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=10)

        self.btnCancelar = tk.Button(self, text="Cancelar", command=self.DeshabilitarCampos)
        self.btnCancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',
                         bg='#B00000', cursor='hand2', activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=10)


    def guardarPaciente(self):

        persona = Persona(
            self.svNombre.get(),
            self.svAppaterno.get(),
            self.svApmaterno.get(),
            self.svDni.get(),
            self.svFecNacimiento.get(),
            self.svEdad.get(),
            self.svAntecedentes.get(),
            self.svCorreo.get(),
            self.svTelefono.get()
        )
        GuardarDatoPaciente(persona)
        self.DeshabilitarCampos()  # Deshabilita los campos después de guardar

#        if self.idPersona == None:
#            GuardarDatoPaciente(persona)

    def HabilitarCampos(self):

        self.svNombre.set('')
        self.svAppaterno.set('')
        self.svApmaterno.set('')
        self.svDni.set('')
        self.svFecNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.entryNombre.config(state='normal')
        self.entryAppaterno.config(state='normal')
        self.entryApmaterno.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFecNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')


    def  DeshabilitarCampos(self):

        self.svNombre.set('')
        self.svAppaterno.set('')
        self.svApmaterno.set('')
        self.svDni.set('')
        self.svFecNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.entryNombre.config(state='disabled')
        self.entryAppaterno.config(state='disabled')
        self.entryApmaterno.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFecNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')


        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')

    def TablaPacientes(self, where=''):
        if len(where) > 0:
            self.ListaPersonas = ListarCondicion(where)

        else:
            self.ListaPersonas = ListarPacientes()

        self.tabla = ttk.Treeview(self, columns=('idPersona', 'nombre', 'apellidoPaterno', 'apellidoMaterno', 'dni', 'fechaNacimiento', 'edad', 'antecedentes', 'correo', 'telefono'), show='headings')
        self.tabla.column('idPersona', width=50, anchor='center')
        self.tabla.column('nombre', width=150, anchor='center')
        self.tabla.column('apellidoPaterno', width=150, anchor='center')
        self.tabla.column('apellidoMaterno', width=150, anchor='center')
        self.tabla.column('dni', width=100, anchor='center')
        self.tabla.column('fechaNacimiento', width=150, anchor='center')
        self.tabla.column('edad', width=50, anchor='center')
        self.tabla.column('antecedentes', width=200, anchor='center')
        self.tabla.column('correo', width=200, anchor='center')
        self.tabla.column('telefono', width=100, anchor='center')

        self.tabla.heading('idPersona', text='ID')
        self.tabla.heading('nombre', text='Nombre')
        self.tabla.heading('apellidoPaterno', text='Apellido Paterno')
        self.tabla.heading('apellidoMaterno', text='Apellido Materno')
        self.tabla.heading('dni', text='DNI')
        self.tabla.heading('fechaNacimiento', text='Fecha Nacimiento')
        self.tabla.heading('edad', text='Edad')
        self.tabla.heading('antecedentes', text='Antecedentes')
        self.tabla.heading('correo', text='Correo')
        self.tabla.heading('telefono', text='Telefono')

        self.tabla.grid(row=10, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

