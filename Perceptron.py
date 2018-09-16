import sys

def main():
    operacao = int(input("Escolha a Função Logica: 1 = And | 2 = Or | 3 = Xor "))
    print( )
  

    lines = [line.rstrip('\n') for line in open("Entrada.txt")]
    
    print("Entrada  - Saida ")
    print( )
    for line in lines:
        NumeroBits = len(line)
        VetorAprendizado = GetVetorAprendizado(operacao, NumeroBits)
        VetorPesos = GetVetorPesos(NumeroBits)
        VetorEntrada = []
        N = NumeroBits-1
        for i in range(len(line)):
            VetorEntrada.append(int(line[i]))
        if(NumeroBits == 2):            
            print(" ",line, "  -  ", FuncaoDoisTreinamento(VetorAprendizado, VetorPesos, 0.4, VetorEntrada))
        elif(NumeroBits == 3):
            print(" ",line, "  -  ", FuncaoTresTreinamento(VetorAprendizado, VetorPesos, 0.6, VetorEntrada))
        elif(NumeroBits == 4):
            print(" ",line, "  -  ", FuncaoQuatroTreinamento(VetorAprendizado, VetorPesos, 0.2, VetorEntrada))
        elif(NumeroBits == N):
            print(" ",line, "  -  ", FuncaoNTreinamento(VetorAprendizado, VetorPesos, 0.5, VetorEntrada)) 
        
#Fim do main


def GetVetorPesos(NumeroBits):
    switcher = {
        2: [0, 0, 0],
        3: [0, 0, 0, 0],
        4: [0, 0, 0, 0, 0],
    }  #N: for i in range(NumeroBits):
            #vet[i] = 0
       
    

    return switcher.get(NumeroBits, '')
#end PegarVetorPeso


#Funções Treinamento de 2 ate N Bits


def FuncaoDoisTreinamento(VetorAprendizado, VetorPesos, TaxaAprendizado, VetorEntrada):
    for i in range(200):
        for x in range(0, len(VetorAprendizado)):
            Resultado = (VetorAprendizado[x][0] * VetorPesos[0]) + (VetorAprendizado[x][1] * VetorPesos[1]) + (ValorBias * VetorPesos[2])
            teste = 1 if Resultado >= 0 else 0
            if(teste != VetorAprendizado[x][2]):
                VetorPesos = AlteraPeso2(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado)
    Resultado = (VetorEntrada[0] * VetorPesos[0]) + (VetorEntrada[1] * VetorPesos[1]) + (ValorBias * VetorPesos[2])
    teste = 1 if Resultado >= 0 else 0
    return teste
#Fim treinamento 2 com NumeroBits   

def FuncaoTresTreinamento(VetorAprendizado, VetorPesos, TaxaAprendizado, VetorEntrada):
    for i in range(100):
        for x in range(0, len(VetorAprendizado)):
            Resultado = (VetorAprendizado[x][0] * VetorPesos[0]) + (VetorAprendizado[x][1] * VetorPesos[1]) + (VetorAprendizado[x][2] * VetorPesos[2]) + (ValorBias * VetorPesos[3])
            teste = 1 if Resultado >= 0 else 0
            if(teste != VetorAprendizado[x][3]):
                VetorPesos = AlteraPeso3(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado)
    Resultado = (VetorEntrada[0] * VetorPesos[0]) + (VetorEntrada[1] * VetorPesos[1]) + (VetorEntrada[2] * VetorPesos[2]) + (ValorBias * VetorPesos[3])
    teste = 1 if Resultado >= 0 else 0
    return teste
#Fim treinamento 3 NumeroBits    

def FuncaoQuatroTreinamento(VetorAprendizado, VetorPesos, TaxaAprendizado, VetorEntrada):
    for i in range(10):
        for x in range(0, len(VetorAprendizado)):
            Resultado = (VetorAprendizado[x][0] * VetorPesos[0]) + (VetorAprendizado[x][1] * VetorPesos[1]) + (VetorAprendizado[x][2] * VetorPesos[2]) + (VetorAprendizado[x][3] * VetorPesos[3]) + (ValorBias * VetorPesos[4])
            teste = 1 if Resultado >= 0 else 0
            if(teste != VetorAprendizado[x][4]):
                VetorPesos = AlteraPeso4(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado)
    Resultado = (VetorEntrada[0] * VetorPesos[0]) + (VetorEntrada[1] * VetorPesos[1]) + (VetorEntrada[2] * VetorPesos[2]) + (VetorEntrada[3] * VetorPesos[3]) + (ValorBias * VetorPesos[4])
    teste = 1 if Resultado >= 0 else 0
    return teste
#Fim treinamento 4 NumeroBits        

def FuncaoNTreinamento(VetorAprendizado, VetorPesos, TaxaAprendizado, VetorEntrada):
    for i in range(200):
        for x in range(0, len(VetorAprendizado)):
            Resultado += (VetorAprendizado[x][i] * VetorPesos[i]) + (ValorBias * VetorPesos[i])
            teste = 1 if Resultado >= 0 else 0
            if(teste != VetorAprendizado[x][i]):
                VetorPesos = AlteraPesoN(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado)
    Resultado += (VetorEntrada[x] * VetorPesos[x]) 
    teste = 1 if Resultado >= 0 else 0
    return teste
#Fim treinamento N NumeroBits   


#Funções para alterar peso para chegar no resultado adequado


def AlteraPeso2(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado):
    for y in range(0, len(VetorPesos) -1):
        VetorPesos[y] = VetorPesos[y] + (TaxaAprendizado * (VetorAprendizado[x][2] - teste) * VetorAprendizado[x][y])
    VetorPesos[2] = VetorPesos[2] + (TaxaAprendizado * (VetorAprendizado[x][2] - teste) * ValorBias)

    return VetorPesos
#Fim alteração peso função 2 NumeroBits

def AlteraPeso3(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado):
    for y in range(0, len(VetorPesos) -1):
        VetorPesos[y] = VetorPesos[y] + (TaxaAprendizado * (VetorAprendizado[x][3] - teste) * VetorAprendizado[x][y])
    VetorPesos[3] = VetorPesos[3] + (TaxaAprendizado * (VetorAprendizado[x][3] - teste) * ValorBias)

    return VetorPesos
#Fim alteração peso função 3 NumeroBits

def AlteraPeso4(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado):
    for y in range(0, len(VetorPesos) -1):
        VetorPesos[y] = VetorPesos[y] + (TaxaAprendizado * (VetorAprendizado[x][4] - teste) * VetorAprendizado[x][y])
    VetorPesos[4] = VetorPesos[4] + (TaxaAprendizado * (VetorAprendizado[x][4] - teste) * ValorBias)

    return VetorPesos
#Fim alteração peso função 4 NumeroBits

def AlteraPesoN(x, teste, TaxaAprendizado, VetorPesos, VetorAprendizado):
    for y in range(0, len(VetorPesos) -1):
        VetorPesos[y] = VetorPesos[y] + (TaxaAprendizado * (VetorAprendizado[x][y] - teste) * VetorAprendizado[x][y])
    VetorPesos[x] = VetorPesos[x] + (TaxaAprendizado * (VetorAprendizado[x][y] - teste) * ValorBias)

    return VetorPesos
#Fim alteração peso função N NumeroBits

                  

def GetVetorAprendizado(operacao, NumeroBits):
    if(NumeroBits == 2):
        switcher = {
            1: [[0, 0, 0],
                [0, 1, 0],
                [1, 0, 0],
                [1, 1, 1]],
            2: [[0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 1]],
            3: [[0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]],
        }
    elif(NumeroBits == 3):
        switcher = {
            1: [[0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0], 
                [1, 0, 0, 0], 
                [1, 0, 1, 0],
                [1, 1, 0, 0], 
                [1, 1, 1, 1]],
            2: [[0, 0, 0, 0],
                [0, 0, 1, 1],
                [0, 1, 0, 1],
                [0, 1, 1, 1], 
                [1, 0, 0, 1], 
                [1, 0, 1, 1], 
                [1, 1, 0, 1], 
                [1, 1, 1, 1]],
            3: [[0, 0, 0, 0],
                [0, 0, 1, 1],
                [0, 1, 0, 1],
                [0, 1, 1, 0], 
                [1, 0, 0, 1], 
                [1, 0, 1, 0], 
                [1, 1, 0, 0], 
                [1, 1, 1, 1]],
        }
    elif(NumeroBits == 4):
        switcher = {
            1: [[0, 0, 0, 0, 0], 
                [0, 0, 0, 1, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 1, 1, 0], 
                [0, 1, 0, 0, 0], 
                [0, 1, 0, 1, 0], 
                [0, 1, 1, 0, 0], 
                [0, 1, 1, 1, 0], 
                [1, 0, 0, 0, 0], 
                [1, 0, 0, 1, 0], 
                [1, 0, 1, 0, 0], 
                [1, 0, 1, 1, 0], 
                [1, 1, 0, 0, 0], 
                [1, 1, 0, 1, 0], 
                [1, 1, 1, 0, 0], 
                [1, 1, 1, 1, 1]],
            2: [[0, 0, 0, 0, 0], 
                [0, 0, 0, 1, 1], 
                [0, 0, 1, 0, 1], 
                [0, 0, 1, 1, 1], 
                [0, 1, 0, 0, 1], 
                [0, 1, 0, 1, 1], 
                [0, 1, 1, 0, 1], 
                [0, 1, 1, 1, 1], 
                [1, 0, 0, 0, 1], 
                [1, 0, 0, 1, 1], 
                [1, 0, 1, 0, 1], 
                [1, 0, 1, 1, 1], 
                [1, 1, 0, 0, 1], 
                [1, 1, 0, 1, 1], 
                [1, 1, 1, 0, 1], 
                [1, 1, 1, 1, 1]],
            3: [[0, 0, 0, 0, 0], 
                [0, 0, 0, 1, 1], 
                [0, 0, 1, 0, 1], 
                [0, 0, 1, 1, 0], 
                [0, 1, 0, 0, 1], 
                [0, 1, 0, 1, 0], 
                [0, 1, 1, 0, 0], 
                [0, 1, 1, 1, 1], 
                [1, 0, 0, 0, 1], 
                [1, 0, 0, 1, 0], 
                [1, 0, 1, 0, 0], 
                [1, 0, 1, 1, 1], 
                [1, 1, 0, 0, 0], 
                [1, 1, 0, 1, 1], 
                [1, 1, 1, 0, 1], 
                [1, 1, 1, 1, 0]],
        }

    return switcher.get(operacao, '')

#end GetVetorAprendizado

Resultado = -1
ValorBias = 1  
main()

