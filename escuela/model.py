# -*- coding: utf-8 -*- 

from odoo import models, fields


class ProfesorRecord(models.Model):

    _inherit = ["profesor.profesor"]
    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')


class AsignaturaRecord(models.Model):

    _inherit = ["asignatura.asignatura"]
    nombre = fields.Char(string='Nombre', required=True)
    temas = fields.Integer(string='Temas')
    tipo = fields.Selection([('c', 'Ciencias'), ('l', 'Letras'), ('i', 'Idiomas'), ('o', 'Otro')], string='Tipo')
    profesor = fields.Many2one('profesor.profesor', string='Profesor')