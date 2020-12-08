from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from almacen_particulas import Almacen_Particulas
from particula import Particula
from random import randint
from collections import deque
from pprint import pformat
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.almacen_de_particulas = Almacen_Particulas()
        self.grafos = dict()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_titulo) 
        self.ui.pushButton_Dibujar.clicked.connect(self.dibujar)
        self.ui.pushButton_Limpiar.clicked.connect(self.limpiar)
        self.ui.Orden_ID_pushButton.clicked.connect(self.ordenId)
        self.ui.pushButton_Mostrar_Busqueda_Profundidad.clicked.connect(self.RealizarBusquedaProfundidad)
        self.ui.pushButton_Mostrar_Busqueda_Amplitud.clicked.connect(self.RealizarBusquedaAmplitud)
        self.ui.Orden_Distancia_pushButton.clicked.connect(self.ordenDistancia)
        self.ui.Orden_Velocidad_pushButton.clicked.connect(self.ordenVelocidad)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
    
    @Slot()
    def RealizarBusquedaProfundidad(self):
        origenX = self.ui.spinBox_B_OrigenX.value()
        origenY = self.ui.spinBox_2_B_OrigenY.value()
        key = (origenX, origenY)
        print(key)
        #value = (destinoX, destinoY, particula.distancia)
        if key in self.grafos:
            Grafo = dict()
            Grafo = self.grafos
            visitados = []
            pila = []
            recorrido = []
            visitados.append(key)
            pila.append(key)
            #print("Apilé el valor de origen: ", key)
            #self.grafos[key].append(value)
            current_number = -1
            while len(pila) > 0:
                print("Currently visited: ", visitados)
                vertice = pila[current_number]
                print("Obtuve el valor de vertice: ", vertice)
                reverse_vertice = (vertice[1], vertice[0])
                print("Reverse vertice = ", reverse_vertice)
                if(vertice in self.grafos):
                    print("Existe vertice.")
                    adyacentes = Grafo[vertice]
                    recorrido.append(vertice)
                    pila.pop()
                elif(reverse_vertice in self.grafos):
                    print("Existe vertice reverso.") 
                    adyacentes = Grafo[reverse_vertice]
                    recorrido.append(reverse_vertice) 
                    pila.pop()      
                else:
                    id = vertice[0] * 5
                    particula = Particula(id, vertice[0], vertice[1], vertice[0], vertice[1], 50, 150, 50, 250)
                    self.almacen_de_particulas.agregar_final(particula)
                    value = (vertice[0], vertice[1], particula.distancia)
                    print("Grafos antes de la comparación: ")
                    print(Grafo)
                    if vertice in Grafo:
                        print("Entré aquí 1.")
                        self.grafos[vertice].append(value)
                        Grafo[vertice].append(vertice)
                        adyacentes = Grafo[vertice]
                        recorrido.append(vertice)
                        pila.pop() 
                    else:
                        print("Entré aquí 2.")
                        self.grafos[vertice] = [value]
                        Grafo[vertice] = [value]
                        adyacentes = Grafo[vertice]
                        recorrido.append(vertice)
                        pila.pop() 
                
                print("La lista actualizada de grafos es: ")
                print(Grafo)
                #adyacentes = Grafo[vertice]
                tuplaCompleta = tuple()
                for ady in adyacentes:
                    print("Lista de adyacentes: ")
                    print(adyacentes)
                    print("Entré al ciclo for de ady in adyacentes.")
                    tuplaCompleta = (ady[0], ady[1])
                    print("Recuperé la tupla de: ", tuplaCompleta)
                    if(tuplaCompleta not in visitados):
                        visitados.append(tuplaCompleta)
                        pila.append(tuplaCompleta) 
            print("Recorrido de profundidad: ")
            print (recorrido)
            self.ui.salida_B_Profundidad.clear()
            self.ui.salida_B_Profundidad.insertPlainText("Recorrido de profundidad: ")
            self.ui.salida_B_Profundidad.insertPlainText(str(recorrido))
        else:
            print("No existe el vértice de origen.")
            #self.grafos[key] = [value]

    @Slot()
    def RealizarBusquedaAmplitud(self):
        origenX = self.ui.spinBox_B_OrigenX.value()
        origenY = self.ui.spinBox_2_B_OrigenY.value()
        key = (origenX, origenY)
        print(key)
        
        if key in self.grafos:
            Grafo2 = dict()
            Grafo2 = self.grafos
            visitados2 = []
            cola = deque()
            recorrido2 = []
            print("Grafo 2: ")
            print(Grafo2)

            visitados2.append(key)
            cola.append(key)
            print("Apilé el valor de origen en cola: ", key)

            while len(cola) > 0:
                print("Visitados: ", visitados2)
                vertice2 = cola[0]
                reverse_vertice = (vertice2[1], vertice2[0])
                print("Reverse vertice = ", reverse_vertice)
                if(vertice2 in self.grafos):
                    print("Existe vertice.")
                    adyacentes2 = Grafo2[vertice2]
                    cola.popleft()
                    recorrido2.append(vertice2)
                elif(reverse_vertice in self.grafos):
                    print("Existe vertice reverso.") 
                    adyacentes2 = Grafo2[reverse_vertice]
                    cola.popleft()        
                    recorrido2.append(vertice2)
                else:
                    id = vertice2[0] * 5
                    particula = Particula(id, vertice2[0], vertice2[1], vertice2[0], vertice2[1], 50, 150, 50, 250)
                    self.almacen_de_particulas.agregar_final(particula)
                    value = (vertice2[0], vertice2[1], particula.distancia)
                    print("Grafos antes de la comparación: ")
                    print(Grafo2)
                    if vertice2 in Grafo2:
                        print("Entré aquí 11.")
                        self.grafos[vertice2].append(value)
                        Grafo2[vertice2].append(vertice2)
                        adyacentes2 = Grafo2[vertice2]
                        recorrido2.append(vertice2)
                        cola.popleft() 
                    else:
                        print("Entré aquí 22.")
                        self.grafos[vertice2] = [value]
                        Grafo2[vertice2] = [value]
                        adyacentes2 = Grafo2[vertice2]
                        recorrido2.append(vertice2)
                        cola.popleft() 
                
                print("La lista actualizada de grafos es: ")
                print(Grafo2)
                
                for ady2 in adyacentes2:
                    print("Lista de adyacentes: ")
                    print(adyacentes2)
                    print("Entré al ciclo for de ady in adyacentes.")
                    tuplaCompleta = (ady2[0], ady2[1])
                    print("Recuperé la tupla de: ", tuplaCompleta)
                    if(tuplaCompleta not in visitados2):
                        visitados2.append(tuplaCompleta)
                        cola.append(tuplaCompleta) 
            print("Recorrido de amplitud: ")
            print(recorrido2)
            self.ui.salida_B_Amplitud.clear()
            self.ui.salida_B_Amplitud.insertPlainText("Recorrido de amplitud: ")
            self.ui.salida_B_Amplitud.insertPlainText(str(recorrido2))
        else:
            print("No existe el vértice de origen.")

    @Slot()
    def ordenId(self):
        self.almacen_de_particulas.ordenarId()

    @Slot()
    def ordenDistancia(self):
        self.almacen_de_particulas.ordenarDistancia()

    @Slot()
    def ordenVelocidad(self):
        self.almacen_de_particulas.ordenarVelocidad()

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        for particula in self.almacen_de_particulas:
            orX = particula.origenX
            orY = particula.origenY
            dtX = particula.destinoX
            dtY = particula.destinoY
            vel = particula.velocidad
            r = particula.red
            g = particula.green
            b = particula.blue
            distance = particula.distancia
            color = QColor(r, g, b)
            pen.setColor(color)
            self.scene.addEllipse(orX, orY, 3, 3, pen)
            self.scene.addEllipse(dtX, dtY, 3, 3, pen)
            self.scene.addLine(orX+3, orY+3, dtX, dtY, pen)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def buscar_titulo(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.almacen_de_particulas:
            print(particula.id)
            if id == str(particula.id):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origenX_widget = QTableWidgetItem(str(particula.origenX))
                origenY_widget = QTableWidgetItem(str(particula.origenY))
                destinoX_widget = QTableWidgetItem(str(particula.destinoX))
                destinoY_widget = QTableWidgetItem(str(particula.destinoY))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenX_widget)
                self.ui.tabla.setItem(0, 2, origenY_widget)
                self.ui.tabla.setItem(0, 3, destinoX_widget)
                self.ui.tabla.setItem(0, 4, destinoY_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f'La partícula con la id "{id}" no fue encontrada'
                )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen en X", "Origen en Y", "Destino en X", "Destino en Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.almacen_de_particulas))

        row = 0
        for particula in self.almacen_de_particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origenX_widget)
            self.ui.tabla.setItem(row, 2, origenY_widget)
            self.ui.tabla.setItem(row, 3, destinoX_widget)
            self.ui.tabla.setItem(row, 4, destinoY_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1


    @Slot()
    def action_abrir_archivo(self):
        with open('grafo.json', 'r') as file:
            self.grafos = json.load(file)
        
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.almacen_de_particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        with open('grafo.json', 'w') as file:
            json.dump(str(self.grafos), file, indent=5)   
        
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print (ubicacion)
        if self.almacen_de_particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.ox_spinBox.value()
        origenY = self.ui.oy_spinBox.value()
        destinoX = self.ui.dx_spinBox.value()
        destinoY = self.ui.dy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox_2.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.almacen_de_particulas.agregar_final(particula)

        key = (origenX, origenY)
        key2 = (destinoX, destinoY)
        print("Key 1: ", key)
        print("Key 2: ", key2)
        value = (destinoX, destinoY, particula.distancia)
        value2 = (origenX, origenY, particula.distancia)
        if key in self.grafos:
            self.grafos[key].append(value)
        else:
            self.grafos[key] = [value]
        if key2 in self.grafos:
            self.grafos[key2].append(value2)
        else:
            self.grafos[key2] = [value2]



    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.ox_spinBox.value()
        origenY = self.ui.oy_spinBox.value()
        destinoX = self.ui.dx_spinBox.value()
        destinoY = self.ui.dy_spinBox.value()
        velocidad = self.ui.id_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.almacen_de_particulas.agregar_inicio(particula)

        key = (origenX, origenY)
        print(key)
        value = (destinoX, destinoY, particula.distancia)
        if key in self.grafos:
            self.grafos[key].append(value)
        else:
            self.grafos[key] = [value]


    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        #self.ui.salida.insertPlainText(str(self.almacen_de_particulas))
        str = pformat(self.grafos, width=40, indent=1)
        self.ui.salida.insertPlainText(str)
        print('Imprimiendo keys...')
        for key in self.grafos.keys():
            print(key)