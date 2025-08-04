import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidget
from gui import Ui_MainWindow
from source import FSMProceso, SALIDAS, ESTADOS, EVENTOS, TRANSICIONES

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # FSM
        self.fsm = FSMProceso()

        # Crear QListWidget dinámicamente en el listView
        self.log_display = QListWidget()
        self.ui.listView.setViewport(self.log_display)

        # Eventos de botones
        self.ui.pushButton.setText("Ingresar Entrada")
        self.ui.pushButton.clicked.connect(self.ingresar_evento)

        self.ui.pushButton_2.setText("Reiniciar")
        self.ui.pushButton_2.clicked.connect(self.reiniciar_fsm)

        self.actualizar_estado_visual()
        self.mostrar_opciones_disponibles()

    def ingresar_evento(self):
        self.log_display.clear()
        entrada = self.ui.textEdit.toPlainText().strip()
        if not entrada.isdigit():
            QMessageBox.warning(self, "Entrada inválida", "Ingrese un número entero del 0 al 7.")
            return

        evento = int(entrada)
        estado_actual = self.fsm.estado

        if (estado_actual, evento) not in TRANSICIONES:
            QMessageBox.warning(self, "Transición inválida",
                                f"No se puede aplicar el evento '{EVENTOS.get(evento, '?')}' en el estado actual '{ESTADOS[estado_actual]}'.")
            return

        siguiente = TRANSICIONES[(estado_actual, evento)]
        accion = SALIDAS.get((estado_actual, evento), "")
        transicion_texto = f"{ESTADOS[estado_actual]} -> {ESTADOS[siguiente]}"
        evento_texto = f"Evento  : {evento} - {EVENTOS[evento]}"
        accion_texto = f"Acción  : {accion}" if accion else "Acción  : (sin acción)"

        # Ejecutar transición
        self.fsm.on_event(evento)

        # Mostrar detalles en log
        self.log_display.addItem(evento_texto)
        self.log_display.addItem(accion_texto)
        self.log_display.addItem(transicion_texto)
        self.log_display.addItem("-" * 40)

        # Actualizar visualización
        self.actualizar_estado_visual()
        self.ui.textEdit.clear()

        # Mostrar estado actual y opciones disponibles
        self.mostrar_opciones_disponibles()

    def reiniciar_fsm(self):
        self.fsm = FSMProceso()
        self.log_display.clear()
        self.actualizar_estado_visual()
        self.mostrar_opciones_disponibles()

    def actualizar_estado_visual(self):
        """Muestra el estado actual en los labels de la interfaz."""
        estado = self.fsm.estado

        # Limpiar todos los labels
        self.ui.label.setText("")
        self.ui.label_3.setText("")
        self.ui.label_5.setText("")
        self.ui.label_6.setText("")

        # Mostrar el estado actual con íconos
        if estado == 0:  # Nuevo
            self.ui.label_5.setText("Nuevo 🆕")
        elif estado == 1:  # Listo
            self.ui.label_3.setText("Listo ✅")
        elif estado == 2:  # Listo y Suspendido
            self.ui.label.setText("Listo y Suspendido ✅😴")
        elif estado == 3:  # Ejecución
            self.ui.label_3.setText("Ejecución 🏃")
        elif estado == 4:  # Bloqueado
            self.ui.label_3.setText("Bloqueado 🔒")
        elif estado == 5:  # Bloqueado y Suspendido
            self.ui.label.setText("Bloqueado y Suspendido 🔒😴")
        elif estado == 6:  # Terminado
            self.ui.label_6.setText("Terminado 💀")

    def mostrar_opciones_disponibles(self):
        """Muestra en el log las transiciones posibles desde el estado actual."""
        estado = self.fsm.estado
        self.log_display.addItem(f"Estado actual: {ESTADOS[estado]}")
        posibles = [f"{k[1]}: {EVENTOS[k[1]]}" for k in TRANSICIONES if k[0] == estado]
        if posibles:
            self.log_display.addItem("Opciones disponibles:")
            for p in posibles:
                self.log_display.addItem(f"  - {p}")
        self.log_display.addItem("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())