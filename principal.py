import Compuesto
import Paralela
class ProgramaPrincipal:

	lista_compuesto_quimicos = []
	numero_hilos = 16
	hilo = []
	def leer_Archivo(self):
		archivo = open("ZINC_chemicals.tsv", "r")
		archivo.readline()
		for linea in archivo.readlines():
			datos_compuesto = linea.split("\t")
			compuesto_quimico = Compuesto.Compuesto(datos_compuesto[1], datos_compuesto[3])
			self.lista_compuesto_quimicos.append(compuesto_quimico)
		archivo.close()

	def ordenar_listaCompuestos(self):
		self.lista_compuesto_quimicos.sort(key=lambda CompuestoQuimico: CompuestoQuimico.nombre)

	def calcularValorformula(self):
		for compuesto in self.lista_compuesto_quimicos:
			compuesto.modificarArrayformula()
			compuesto.calculoCoeficienteSimilitud()

	def impirmirLista(self):
		for compuesto in self.lista_compuesto_quimicos:
			print(compuesto.get_nombre(),"  ",compuesto.get_arrayformula())

	def calculoCoeficienteJaccarTinomotoParalelo(self):
		for i in range(self.numero_hilos):
			self.hilo.append(Paralela.Paralela(id_hilo=i,listaCompuesto=self.lista_compuesto_quimicos))
		for i in range(self.numero_hilos):
			self.hilo[i].start()
		for i in range(self.numero_hilos):
			self.hilo[i].join()

	def cerrarArchivoSalida(self):
		self.hilo[0].archivo.close()
