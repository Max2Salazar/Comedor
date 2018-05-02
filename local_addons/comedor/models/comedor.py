# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class comedor(osv.osv):
	_name='maximo.comedor'
	_rec_name='nombre'
	
	_colums={
		'nombre':fields.char('Nombre',size=80,required-True,help='Aqui se coloca el Nombre del cliente'),
		'apellido':fields.char('Apellido',size=80,required-True,help='Aqui se coloca el Apellido del cliente'),
		'cedula':fields.integer('Cedula',size=8,required-True,help='Aqui se coloca la Cedula del cliente'),
		'fecha_nacimiento':fields.date('Fecha_nacimiento',help='Aqui se coloca la fecha de nacimiento del cliente'),
		'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
	}
