import threading
import time
import sys
class Paralela(threading.Thread):
	comparadas = []
	numHilos = 16
	archivo = open("RESULTADOS.tsv","w")
	def __init__(self, id_hilo, listaCompuesto):
		threading.Thread.__init__(self , target = Paralela.run)
		self.id_hilo = id_hilo
		self.listaCompuesto = listaCompuesto

	def run(self):
		self.CoeficienteTanimoto()

	def CoeficienteTanimoto(self):
		for i in range (self.id_hilo, len(self.listaCompuesto), self.numHilos):
			for j in range (i+1 , len(self.listaCompuesto)):
				compuesto1 = self.listaCompuesto[i]
				compuesto2 = self.listaCompuesto[j]
				self.archivo.write(compuesto1.get_nombre()+ "\t"+compuesto2.get_nombre() +"\t" + str(self.__ccalculoTab(compuesto1,compuesto2))+"\n")

	def __calculoNc(self,compuesto1,compuesto2):
		valor_comunCoeficienteSimilitud = 0
		for key in compuesto2.get_arrayformula():
			if key in compuesto1.get_arrayformula():
				if (compuesto1.get_arrayformula()[key] <= compuesto2.get_arrayformula()[key]):
					valor_comunCoeficienteSimilitud += compuesto1.get_arrayformula()[key]
				else:
					valor_comunCoeficienteSimilitud += compuesto2.get_arrayformula()[key]
		return valor_comunCoeficienteSimilitud

	def __ccalculoTab(self,compuesto1,compuesto2):
		Nc = self.__calculoNc(compuesto1,compuesto2)
		return round((Nc/float(compuesto1.get_coeficientesimilitud() + compuesto2.get_coeficientesimilitud() - Nc)),2)
