from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import pyodbc
import json

def index(request):
	return render(request, 'inicio.html')

def getprice(request):
	#if request.is_ajax():
	CodeBar = request.GET.get('q', False)
	cnxn = pyodbc.connect('DSN=pm_local;UID=sa;PWD=Contrasena1')
	cursor = cnxn.cursor()
	cursor.execute("SELECT TOP 1 * FROM productos WHERE codigo_producto = '%s'" %CodeBar)

	Producto = {}

	if cursor.rowcount < 0:
		row = cursor.fetchone()
		Producto['Descripcion'] = row.descrip_producto
		Producto['Precio'] = round(row.precio1, 2)
		Producto['Existencias'] = int(row.cant_total)
		Producto['CodBar'] = row.codigo_producto
	else:
		row = cursor.fetchone()
		Producto['Descripcion'] = "No se encuentra el producto"
		Producto['Precio'] = "0.00"
		Producto['Existencias'] = 0
		Producto['CodBar'] = CodeBar

	return render(request, 'resultado.html', {'Producto' : Producto})