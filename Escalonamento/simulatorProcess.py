import random
import operator

class Processo(object):
    def __init__(self, nome, burst, tcheg, prioridade, q):
        self.nome = nome
        self.burst = burst
        self.tcheg = tcheg
        self.prioridade = prioridade
        self.q = q

def setNome(nome):
    self.nome = nome

def setBurst(burst):
    self.burst = burst

def setTcheg(tcheg):
    self.tcheg = tcheg

def setPrioridade(prioridade):
    self.prioridade = prioridade

def setQ(q):
    self.q = q


class ListRR(object):
    def __init__(self,proc, ta):
        self.proc = proc
        self.ta = ta
    




def calcQ(quantum, burst):
    for i in burst:
        while i != quantum:
            if i != burst:
               sobraQ =  i - quantum
               i -= sobraQ
        break



def verificaBurst(listBurst, burst):
    pass    
    



def leArq(file):
    listaArquivo = []
    arq = open(file)
    line = arq.readline()
    while line:
        proc = line.split("&")[0]
        proc = proc.split(";")
        nome = proc[0].split("@")[1]
        burst = int(proc[1])
        tcheg = int(proc[2])
        pri = int(proc[3])
        quantum = int(proc[4])
        #print(nome, burst, tche, pri, quant)
        proc = Processo(nome, burst, tcheg, pri, quantum)
        listaArquivo.append(proc)
        line = arq.readline()

    return listaArquivo



def calcWait(t, b):
    if t < b:
        return b - t
    else:
        return t - b


def imprimiInfo(lista):
    turnAr = 0
    mediaWait = 0
    mediaTurnAr = 0
    p=0

    for i in lista:
        p+=1
        turnAr += (i.burst - i.tcheg)
                
        print(i.nome,"\t", i.burst,"\t",i.tcheg,"\t\t\t",turnAr,"\t\t",calcWait(turnAr,i.burst))
                
        mediaWait+= calcWait(turnAr, i.burst)
        mediaTurnAr+= turnAr

    print('\n')
                              
    print('\nAVG Waiting Time: ',float(mediaWait/len(lista)))
    print('AVG TurnAround Time: ', float(mediaTurnAr/len(lista)))             
    print('****************************\n')

    
    

def calcFCFS():
    infoProcessFCFS = []

    while True:
        entrada = input('Digite o tipo de entrada: manual (M/m) arquivo (A/a): ')
      

        if entrada == 'm' or entrada == 'M':
            qProcess_FCFS = int(input('Insira a quantidade de processos: '))

            for i in range(qProcess_FCFS):
                print('P '+str(i+1))
                b = int(input('Burst: '))
                c = int(input('Tempo de chegada: '))
                pr = 0
                q = 0
                proc = Processo(i, b, c, pr, q)
                infoProcessFCFS.append(proc)

            print('\n')

            infoProcessFCFS.sort(key = operator.attrgetter("tcheg"), reverse = False)

            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(infoProcessFCFS)
            break

        elif entrada == 'a' or entrada == 'A':
            arquivoFCFS = []
            arquivoFCFS = leArq('fcfs.txt')
            print('\n')

            arquivoFCFS.sort(key = operator.attrgetter("tcheg"), reverse = False)

            mediaWait = 0
            mediaTurnAr = 0

            turnAr = 0

            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(arquivoFCFS)
            break

        else:
            print('Entrada inválida!')
                   
                

            
def calcSJF():
    infoProcessSJF = []
    listaBurst = []

    while True:
        entrada = input('Digite o tipo de entrada: manual (M/m) arquivo (A/a): ')

        if entrada == 'm' or entrada == 'M':
            qProcessSJF = int(input('Insira a quantidade de processos: '))
            
            for i in range(qProcessSJF):
                print('P '+str(i+1))
                b = int(input('Burst: '))
                c = int(input('Tempo de chegada: '))
                p = 0
                q = 0
                proc = Processo(i, b, c, p, q)
                infoProcessSJF.append(proc)
                listaBurst.append(b)

                infoProcessSJF.sort(key = operator.attrgetter("burst"), reverse = False)
                infoProcessSJF.sort(key = operator.attrgetter("tcheg"), reverse = False)

            print('\n')

           

            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(infoProcessSJF)
            break

        elif entrada == 'A' or entrada == 'a':
            arquivoSJF = []
            arquivoSJF = leArq('sjf.txt')
            print('\n')

            arquivoSJF.sort(key = operator.attrgetter("burst"), reverse = False)
            arquivoSJF.sort(key = operator.attrgetter("tcheg"), reverse = False)

            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(arquivoSJF)
            break

        else:
            print('Entrada inválida!')
            



'''def calcSRTF():    print('****************************\n')

    infoProcessSRTF = []
    listaBurst = []
    listaCheg = []
    
    qProcessSRTF = int(input('Insira a quantidade de processos: '))

    for i in range(qProcessSRTF):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        q = 0
        p = 0
        proc = Processo(i, b, c, q, p)
        infoProcessSRTF.append(proc)
        


    infoProcessSRTF.sort(key = operator.attrgetter("tcheg"), reverse = False)

    for k in infoProcessSRTF:
        listaBurst.append(k.burst)
        listaCheg.append(k.tcheg)
  
    print('\n')
    
    print('Informações dos processos:\n')
    print('Process\t','Burst\t','Tempo de chegada')

    for k in infoProcessSRTF:        
        print(int(k.nome+1),'\t', k.burst,'\t',k.tcheg)

    print('\n')

    time = 0

    for x in infoProcessSRTF:
        while(x.burst > 0):
            for i in range(len(listaBurst)):
                burstF = listaBurst[i]
                x.burst-=1
                for k in range(burstF):
                    time+=1
                    listaBurst[i] -=1
                    print(listaBurst[i])

                    if time in listaCheg and listaBurst[i] > listaBurst[i+1]:
                        print('tempo do próximo burst: ',time)
                        print('vez do burst ',listaBurst[i+1])                                            
                        break'''
                
            
        
    
def calcRoundR():
    infoProcessRR = []
    listaBurst = []
    copyBurst = []
    copyTA = []
    qProcessRR = int(input('Insira a quantidade de processos: '))
    quantum = int(input('Insira o quantum de tempo: '))
    for i in range(qProcessRR):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = 0
        priori = 0
        proc = Processo(i, b, c, quantum, priori)
        infoProcessRR.append(proc)
        listaBurst.append(b)
        copyBurst.append(b)
    print('\n')
    

    percorre = []
    valor = quantum
    vez = 0
    valorEsp = quantum
    percorre.append(valor)
    finais = []
    final = []
    listaMod = []
    listaEspera = []

    for x in listaBurst:
        listaMod.append(0)
        
        listaEspera.append(0)

        
    while sum(listaBurst) >= 0:
        
        for i in range(len(listaBurst)):
            vez+=1
            
            if listaBurst[i] > quantum and listaBurst[i] > 0:
                #valor = listaBurst[i]
                listaBurst[i] -= quantum
                valorEsp += listaBurst[i]
                valor += quantum

                listaMod[i] += valor
                listaEspera[i] += (valor-listaMod[i])
                
                #valor-=listaBurst[i]
                percorre.append(valor)
                
                       
            
            elif listaBurst[i] < quantum and listaBurst[i] > 0:
                valor += listaBurst[i]
                listaMod[i] += listaBurst[i]
                valorEsp += listaBurst[i]
                listaBurst[i]-=listaBurst[i]
                #valor-=listaBurst[i]
                listaEspera[i] += (valorEsp-listaMod[i])
                percorre.append(valor)

            if listaBurst[i] == 0:
                if vez not in final and valor not in final:
                    final.append(vez)
                    final.append(valor)
                    rr = ListRR(vez, valor)
                    finais.append(rr)
                    
            #print(listaBurst[i])

            
            if vez >= len(listaBurst):
                vez = 0
            
            
    
        if sum(listaBurst) == 0:
            break
        
        print('\n')

    finais.sort(key = operator.attrgetter("proc"), reverse = False)
    for x in finais:
        copyTA.append(x.ta)
    
    print('\nInformações dos processos:\n')
    print('Process\t','Burst\t','TurnAround\t','Wait Time')

    p = 0
    tavg = 0
    for x in range(qProcessRR):
        p+=1
        print(p,"\t", copyBurst[x],"\t ",copyTA[x],"\t\t",listaEspera[x])
        tavg+= copyTA[x]

    print('AVG TurnAround: ',float(tavg)/qProcessRR)
    print('****************************\n')

    #print(percorre)

    
while(True):
    opcao = input('1 - FCFS\n2 - SJF\n3 - SRTF\n4 - Round Robin\n5 - Multinível\n6 - Sair\n')
    
    if opcao == '1':
        calcFCFS()        

    

    elif opcao == '2':
        calcSJF() 
    
    elif opcao == '3':
        print('não funciona')
        


        
    elif opcao == '4':
        calcRoundR()

    elif opcao == '5':
        print('não funciona')

    
    elif opcao == '6':
        break


    else:
        print('Insira uma opção válida do menu')
