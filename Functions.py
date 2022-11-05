import random
import os


class Examen:
    def __init__(self, data):
        self.Preguntas = []
        self.Respuestas = []
        self.RespuestasAgrupadas = []
        self.getQuestions(data)
        self.doneQs = self.getDoneQs()

    def getQuestions(self, dataText):
        with open(dataText, 'r', encoding="utf8") as file:
            i = 0
            for line in file:
                if(i % 5 == 0):
                    self.Preguntas.append(line)
                else:
                    self.Respuestas.append(line)
                i += 1
        self.agruparRespuestas()

        return

    def agruparRespuestas(self):
        Aux = []
        for i in range(len(self.Respuestas)):
            Aux.append(self.Respuestas[i])
            if(i % 4 == 3):
                self.RespuestasAgrupadas.append(Aux)
                Aux = []
        return

    def getQ(self, index):
        Q = self.Preguntas[index]
        A = self.RespuestasAgrupadas[index]
        return [Q, A]

    def getRandomQA(self):
        RandomIndex = random.randint(0, len(self.Preguntas)-1)
        while(RandomIndex in self.doneQs):
            RandomIndex = random.randint(0, len(self.Preguntas)-1)

        self.doneQs.append(RandomIndex)
        RandomQA = self.getQ(RandomIndex)
        return(RandomIndex, RandomQA)

    def PreguntaExamen(self):
        [Qindex, [Q, A]] = self.getRandomQA()
        print("Pregunta "+str(Qindex)+":")
        print(Q)
        correct = self.RandomRespuestas(A)
        answerUser = self.getIntput()
        if(answerUser == correct):
            print("****CORRECTO****")
            save = input("Ingrese 's' para permitir a esta pregunta repetirse: ")
            if(save == 's' or save == 'S'):
                self.doneQs.remove(Qindex)
                print("Pregunta "+str(Qindex) + " guardada")
            return True
        else:
            print("!!!!Incorrecto!!!!!")
            print("Respuesta: ")
            print(A[0])
            save = input("Ingrese 's' para permitir a esta pregunta repetirse: ")
            if(save == 's' or save == 'S'):
                self.doneQs.remove(Qindex)
                print("Pregunta "+str(Qindex) + " guardada")
            return False

    def RandomRespuestas(self, Respuestas):
        idxs = []
        rdm = random.randint(0, 3)
        while(len(idxs) < 4):
            if(rdm not in idxs):
                idxs.append(rdm)
                if(rdm == 0):
                    correct = len(idxs)-1
                rdm = random.randint(0, 3)
            else:
                rdm = random.randint(0, 3)
        cont = 0
        for i in idxs:
            print(str(cont)+". "+Respuestas[i])
            cont += 1
        return correct

    def darExamen(self, nPreguntas):

        calificacion = 0
        contador = 0

        while contador < nPreguntas:
            print("-"*100)
            print("("+str(contador+1)+"/"+str(nPreguntas)+")")
            if(self.PreguntaExamen()):
                calificacion += 1
            contador += 1
            input("Presione ENTER para continuar...")
            os.system('cls')
        print("Calificación:" + str(calificacion)+"/" + str(nPreguntas))
        self.guardarQsDone()
        print("-"*100)
        print("-"*100)

    def getIntput(self):
        while True:
            num = input("Ingrese una opción: ")
            try:
                val = int(num)
                if(val > 3):
                    print("Número no válido [0,1,2,3]")
                else:
                    return val
            except ValueError:
                print("Ingrese solamente números [0,1,2,3]")

    def reiniciarQs(self):
        self.doneQs = []

    def guardarQsDone(self):
        file = open("doneQs.txt", "w")
        file.write(str(self.doneQs))
        file.close()

    def getDoneQs(self):
        
        file = open('doneQs.txt', 'r', encoding="utf8")
        strline = file.readline()
        if(len(strline)>2):
            strline = strline[1:-1];
            arrayLine = strline.split(',')
            for i in range(len(arrayLine)):
                arrayLine[i]= int(arrayLine[i])
            print("Preguntas que no se van a repetir:")
            print(arrayLine)
            print("-"*100)
            return arrayLine
        else:
            return []
