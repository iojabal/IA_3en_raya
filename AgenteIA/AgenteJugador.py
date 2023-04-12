#################################################################
# Nombre      : Entorno                                         #
# Version     : 0.05.03.2017                                    #
# Autor       : Victor Estevez                                  #
# Descripcion : Clase Agentes con Adversarios                   #
##################################################################


from AgenteIA.Agente import Agente
from collections import namedtuple
import time


ElEstado = namedtuple('ElEstado', 'jugador, get_utilidad, tablero, movidas')


class AgenteJugador(Agente):

    def __init__(self):
        Agente.__init__(self)
        self.estado = None
        self.juego = None
        self.utilidad = None
        self.tecnica = None

    def funcionEvaluacion(self, e):
        raise  Exception("No Implementado ")

    def jugadas(self, estado):
        raise Exception("Error: No se implemento")

    def get_utilidad(self, estado, jugador):
        raise Exception("Error: No se implemento")

    def testTerminal(self, estado):
        return not self.jugadas(estado)

    def getResultado(self, estado, m):
        raise Exception("Error: No se implemento")

    def minimax(self, estado):

        def valorMax(e):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = -100
            for a in self.jugadas(e):
                v = max(v, valorMin(self.getResultado(e, a)))
            return v

        def valorMin(e):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = 100
            for a in self.jugadas(e):
                v = min(v, valorMax(self.getResultado(e, a)))
            return v

        return max(self.jugadas(estado), key=lambda a: valorMin(self.getResultado(estado, a)))

    def propio(self, estado):
        jugador = estado.jugador

        def max_value(e, alpha, betita, h):
            vm = -100
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            if h == 0:
                return self.funcionEvaluacion(e)
            for j in self.jugadas(e):
                vm = max(vm, min_value(self.getResultado(e, j), alpha, betita, h-1))
                if vm >= beta:
                    return vm
                alpha = max(alpha, vm)
            return vm

        def min_value(e, alpha, betita, h):
            vm = 100
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            if h == 0:
                return self.funcionEvaluacion(e)
            for j in self.jugadas(e):
                vm = min(vm, max_value(self.getResultado(e, j), alpha, betita, h-1))
                if vm <= alpha:
                    return vm
                betita = min(betita, vm)
            return vm

        mejor_score = -100
        beta = 100
        mejor_accion = None
        for a in self.jugadas(estado):
            v = min_value(self.getResultado(estado, a), mejor_score, beta, 2)
            if v > mejor_score:
                mejor_score = v
                mejor_accion = a
        return mejor_accion

    def podaAlphaBeta(self, estado):
        jugador = estado.jugador

        def max_value(e, alpha, betita):
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            vm = -100
            for j in self.jugadas(e):
                vm = max(vm, min_value(self.getResultado(e, j), alpha, betita))
                if vm >= beta:
                    return vm
                alpha = max(alpha, vm)
            return vm

        def min_value(e, alpha, betita):
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            vm = 100
            for j in self.jugadas(e):
                vm = min(vm, max_value(self.getResultado(e, j), alpha, betita))
                if vm <= alpha:
                    return vm
                betita = min(betita, vm)
            return vm

        mejor_score = -100 # max
        beta = 100 # min
        mejor_accion = None # No hay mejor accion
        for a in self.jugadas(estado):
            v = min_value(self.getResultado(estado, a), mejor_score, beta)
            if v > mejor_score:
                mejor_score = v
                mejor_accion = a
        return mejor_accion

    def mide_tiempo(funcion):
        def funcion_medida(*args, **kwards):
            inicio = time.time()
            c = funcion(*args, **kwards)
            print("Tiempo de ejecucion: ", time.time() - inicio)
            return c

        return funcion_medida

    @mide_tiempo
    def programa(self):

        if self.tecnica == "minimax":
            self.acciones = self.minimax(self.estado)
        elif self.tecnica == "podaalfabeta":
            self.acciones = self.podaAlphaBeta(self.estado)
        elif self .tecnica == 'propio':
            self.acciones = self.propio(self.estado)
