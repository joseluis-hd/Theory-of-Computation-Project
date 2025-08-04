# fsm_proceso.py

# Códigos de eventos
EVENTOS = {
    0: "Admitir",
    1: "Activar",
    2: "Ejecutar",
    3: "Suspender",
    4: "Esperar suceso",
    5: "Ocurrencia de suceso",
    6: "Final de tiempo",
    7: "Salir"
}

# Códigos de estados
ESTADOS = {
    0: "Nuevo",
    1: "Listo",
    2: "Listo y Suspendido",
    3: "Ejecución",
    4: "Bloqueado",
    5: "Bloqueado y Suspendido",
    6: "Terminado"
}

# δ: mapa (estado_actual, evento) → siguiente_estado
TRANSICIONES = {
    (0, 0): 1,  # Nuevo --Admitir--> Listo

    (1, 2): 3,  # Listo --Ejecutar--> Ejecución
    (1, 3): 2,  # Listo --Suspender--> Listo y Suspendido

    (2, 1): 1,  # Listo y Suspendido --Activar--> Listo

    (3, 4): 4,  # Ejecución --Esperar suceso--> Bloqueado
    (3, 6): 1,  # Ejecución --Final de tiempo--> Listo
    (3, 7): 6,  # Ejecución --Salir--> Terminado

    (4, 3): 5,  # Bloqueado --Suspender--> Bloqueado y Suspendido
    (4, 5): 1,  # Bloqueado --Ocurrencia de suceso--> Listo

    (5, 1): 4,  # Bloqueado y Suspendido --Activar--> Bloqueado
    (5, 5): 2   # Bloqueado y Suspendido --Ocurrencia de suceso--> Listo y Suspendido
}

# g: mapa (estado_actual, evento) → mensaje de salida
SALIDAS = {
    (0, 0): "Proceso admitido",

    (1, 2): "Ejecutando proceso",
    (1, 3): "Proceso suspendido",

    (2, 1): "Reactivar proceso",

    (3, 4): "Solicitud E/S",
    (3, 6): "Quantum agotado",
    (3, 7): "Proceso terminado",

    (4, 3): "Proceso suspendido",
    (4, 5): "E/S completada",

    (5, 1): "Reactivar proceso",
    (5, 5): "E/S completada"
}


class FSMProceso:
    def __init__(self):
        self.estado = 0

    def on_event(self, ev: int):
        """Procesa un evento ev (código 0–7)."""
        if ev not in EVENTOS:
            raise ValueError(f"Evento desconocido: {ev}")

        key = (self.estado, ev)
        if key not in TRANSICIONES:
            print(f"Transición inválida: {ESTADOS[self.estado]} + {EVENTOS[ev]}")
            return

        # mensaje de salida
        msg = SALIDAS.get(key)
        # siguiente estado
        siguiente = TRANSICIONES[key]

        # imprimir log
        print(f"Evento  : {ev} – {EVENTOS[ev]}")
        if msg:
            print(f"Acción  : {msg}")
        print(f"{ESTADOS[self.estado]} → {ESTADOS[siguiente]}\n")

        # actualizar estado
        self.estado = siguiente

    def estado_actual(self):
        return self.estado, ESTADOS[self.estado]


if __name__ == "__main__":
    fsm = FSMProceso()

    # Ejemplo de secuencia (puedes cambiarla para probar otros flujos)
    secuencia = [0, 2, 6, 2, 4, 5, 2, 7]
    
    for ev in secuencia:
        fsm.on_event(ev)

    # 0, 2, 7
    # 0, 3, 1, 2, 7
    # 0, 2, 4, 5, 2, 7
    # 0, 2, 4, 3, 1, 5, 2, 7
    # 0, 2, 6, 2, 4, 5, 2, 7
