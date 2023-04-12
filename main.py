from AgenteTresEnRaya import AgenteTresEnRaya
from Tablero import Tablero
from HumanoTresEnRaya import HumanoTresEnRaya

if __name__ == "__main__":
    juan = HumanoTresEnRaya()
    luis = AgenteTresEnRaya()
    luis.tecnica = "propio"

   # juan = AgenteTresEnRaya()

    tablero = Tablero()

#    tablero.insertar(juan)
    tablero.insertar(luis)
    tablero.insertar(juan)
    tablero.run()
