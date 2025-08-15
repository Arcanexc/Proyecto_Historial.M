from turtle import title
from .conexion import ConexionDB
from tkinter import messagebox

from HistoriaMedica.modelo import conexion


def GuardarDatoPaciente (Persona):
    conexion = ConexionDB()
    sql = f""" INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno, 
            dni, fechaNacimiento, edad, antecedentes, correo, telefono, activo) VALUES 
            ('{Persona.nombre}', '{Persona.apellidoPaterno}', '{Persona.apellidoMaterno}',
            {Persona.dni}, '{Persona.fechaNacimiento}','{Persona.edad}', '{Persona.antecedentes}',
            '{Persona.correo}', '{Persona.telefono}', 1)"""


    try:

        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:

        title = 'Registrar Paciente'
        mensaje = 'Error al registrar Paciente'
        messagebox.showerror(title, mensaje)



class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, dni, fechaNacimiento, edad, antecedentes, correo, telefono):

        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.dni = dni 
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono


    def __str__(self):
        return f'Persona [{self.nombre}, {self.apellidoPaterno}, {self.apellidoMaterno}, {self.dni}, {self.fechaNacimiento}, {self.edad}, {self.antecedentes}, {self.correo}, {self.telefono}]'
