import time
class _NotBiology(Exception):
    def __init__(self,message=""):
        self.message = message
        self.expression = [print(message),time.sleep(2)]

class Parental:

    #Construtor do Pai ou Mãe, define atributos e o gene pode ter, no máximo, 2 elementos
    def __init__(self,genes,config={}):
        if type(genes) not in [str,list]:
            raise _NotBiology("The type must be string or array(of strings)")
        self.gene = genes
        self.result = []
        self.porcento = []
        self.config=config

    def dominancia(self,parente,dx,y):

        dy = 0
        if y in parente.config:
            dy = parente.config[y]
        return max([dx,dy])

    #Relaciona os genes de um parente a outro, guardando no atributo result dos dois | Deixa letras maiúsculas na frente
    def Procriar(self,parente):
        result = list()
        for x in self.gene:
            dominanciax = 0
            if x in self.config:
                dominanciax = self.config[x]

            for y in parente.gene:
                dominanciaNivel = self.dominancia(parente,dominanciax,y)
                if type(x)==str:
                    if x.isupper():
                        result.append((x+y,dominanciaNivel))
                        continue
                result.append(("{}{}".format(y,x),dominanciaNivel))
        possibilidades = set(result)
        print("Possibilidades: ",*[x[0] for x in possibilidades])
        self.result,parente.result= result[:],result[:]


    #Coloca no atributo porcento a porcentagem de aparecimento de tais genes em tal cruzamento | Copia a lista, verifica a quantidade, deleta os repetidos e guarda a quantidade e seu respectivo elemento
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
                valor = i[0][0]
                grauDeDominancia = i[0][1]
                porcentagem = i[1]
                print(valor,end="")
                print(" :",porcentagem,end="")
                print(" - ","Grau de dominância: {}".format(grauDeDominancia))



# a = Parental(["A","a"],{"A":1,"a":0})
# b = Parental("Aa",{"A":1,"a":0})
# a.Procriar(b)
# a.Porcento()
# a.Analise()
