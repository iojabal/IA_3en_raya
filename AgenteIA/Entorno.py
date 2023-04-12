class Entorno:

    def __init__(self):
        self.agentes = []

    def get_percepciones(self, agente):
        raise Exception("Ahhh,falta implementar")

    def ejecutar(self, agente):
        raise Exception("Ahhh,falta implementar")

    def evolucionar(self):
        for agente in self.agentes:
            if agente.vive:
                self.get_percepciones(agente)
                self.ejecutar(agente)

    def run(self):
        while True:
            if self.finalizar():
                break
            self.evolucionar()

    def finalizar(self):
        return any(not agente.vive for agente in self.agentes)

    def insertar(self, agente):
        self.agentes.append(agente)

