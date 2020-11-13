from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from almacen_particulas import Almacen_Particulas
from particula import Particula
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.almacen_de_particulas = Almacen_Particulas()
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
        self.ui.Orden_Distancia_pushButton.clicked.connect(self.ordenDistancia)
        self.ui.Orden_Velocidad_pushButton.clicked.connect(self.ordenVelocidad)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
    
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

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.almacen_de_particulas))