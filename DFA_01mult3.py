"""DFA_01mult3.py implementa un autómata deterministico.

Descripción.
                    Muestra como implementar un Automáta Finito Deterministico (DFA), que acepte las
                    palabras {0,1}* qye sean muliplos de 3.
Instalación.
                    >python -m pip install FAdo
                    >python -m pip install graphviz
                    
Referencia.

DFA. 
Disponible en: https://www.dcc.fc.up.pt/~rvr/FAdoDoc/notebooks/FAdoTutorial.html#
Consultado:30sept24
"""
from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *
from graphviz  import *
import time
import sys

def mostrarDataTime():
    """imprime estampa de tiempo"""
    print(time.ctime())


def myDFA():
    """retorna un objeto tipo FAdo.fa.DFA.
         retorna una tupla con elementos estructurales de DFA"""
    m3 = DFA()# define instancia
    m3.setSigma(['0','1'])#define alfabeto de entrada
    m3.addState('s1')#define estados
    m3.addState('s2')
    m3.addState('s3')
    m3.setInitial(0)#define estado incial
    m3.addFinal(0)#define estado final
    m3.addTransition(0, '1', 1)
    m3.addTransition(0, '0', 0)
    m3.addTransition(1, '1', 0)
    m3.addTransition(1, '0', 2)
    m3.addTransition(2, '1', 2)
    m3.addTransition(2, '0', 1)
    return m3

def main()->int:
    print(f"Estructura del DFA: {myDFA()}")
    m3=myDFA()
    #1 1 0
    print(m3.evalWordP("011"))
    print(m3.evalWordP("10010"))
    print(m3.evalWordP("110"))
    print(m3.evalWordP("000"))
    print(m3.evalWordP("110"))
    print(m3.evalWordP("1101"))
    print(m3.evalWordP("1011"))
    #m3.display()
    mostrarDataTime()
    return 0



if __name__ == '__main__':
    try:        
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)
