class Parental:

    #Construtor do Pai ou Mãe, defini atributos e o gene pode ter, no máximo, 2 elementos
    def __init__(self,gene):
        if len(gene)>2: self.gene = ""
        else: self.gene = gene
        self.result = []
        self.porcento = []

    #Relaciona os genes de um parente a outro, guardando no atributo result dos dois | Deixa letras maiúsculas na frente
    def Procriar(self,parente):
        result = list()
        for x in self.gene:
            for y in parente.gene:
                if x.isupper(): result.append(x+y)
                else: result.append(y+x)
        possibilidades = set(result)
        print("Possibilidades: ",*possibilidades)
        self.result,parente.result= result[:],result[:]


    #Coloca no atributo .porcento a porcentagem de aparecimento de tais genes em tal cruzamento | Copia a lista, verifica a quantidade, deleta os repetidos e guarda a quantidade e seu respectivo elemento
    def Porcento(self):
        if self.result:
            templist = self.result[:]
            indice = 0
            posicao = list()
            valor = list()
            while indice<len(templist):
                atual = templist[indice]
                quantidade = templist.count(atual)
                posicao.append(quantidade)
                valor.append(atual)
                if quantidade>1:
                        #passagem | Ajuste dos índices após remoção de elementos
                        passagem = 0
                        deletar = list()
                        for _ in range(len(templist)):
                            if templist[_] == atual: deletar.append(_)
                        for _ in deletar:
                            templist.pop(_-passagem)
                            passagem+=1
                else: indice+=1

        total = sum(posicao)
        porcento = map(lambda x: "{}%".format(x*100/total),posicao)
        self.porcento=list(zip(valor,list(porcento)))

    #Analisa e mostra amigavelmente as porcentagens
    def Analise(self):
        if self.porcento:
            print("\n")
            for i in self.porcento:
                print("{} : {}".format(i[0],i[1]))



# a = Parental("Aa")
# b = Parental("Aa")
# a.Procriar(b)
# a.Porcento()
# a.Analise()
