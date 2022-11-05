from Functions import *;
from Utils import *;

examen = Examen("data.txt")
NumeroDePreguntas = 5
while True:
    print("1. Start Quiz")
    print("2. Exit")
    inp = getIntput()
    if(inp == 1 ):
        examen.darExamen(NumeroDePreguntas)
    if(inp == 2):
        break
