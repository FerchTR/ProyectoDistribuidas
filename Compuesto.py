import re
class Compuesto:
	nombre = ""
	arrayFormula = {}
	formula = ""
	coeficienteSimilitud = 0

	def __init__(self,nombre,array_formula):
		self.nombre = nombre
		self.formula = array_formula
		self.coeficienteSimilitud = 0
		

	def modificarArrayformula(self):
		arrayFormula = {}
		cadenaPatron = re.compile(r'[a-zA-Z]')
		segmFormula = cadenaPatron.findall(self.formula)
		for partes in segmFormula:
			if (partes in arrayFormula):
				arrayFormula[partes] = arrayFormula[partes] + 1
			else:
				arrayFormula[partes] = 1
		self.arrayFormula = arrayFormula

	def calculoCoeficienteSimilitud(self):
		valor = 0
		for key in self.arrayFormula:
			valor += self.arrayFormula[key]
		self.coeficienteSimilitud = valor

	def get_nombre(self):
		return self.nombre

	def get_arrayformula(self):
		return self.arrayFormula

	def get_coeficientesimilitud(self):
		return self.coeficienteSimilitud