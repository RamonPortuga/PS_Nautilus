"""
Implemente um modelo que descreva os AUVs da UFRJ Nautilus

Requerimentos 

Deve conter os atributos: número de thursters, lista com sensores,
ano de construção, nome do veículo, e no mínimo, mais 1 atributo de
livre escolha 
Deve conter métodos para:
Exibir todos os AUVs em tabela
Exibir os robôs individulmente
Rankear os robôs do mais novo para o mais antigo
Deve conter outro método de livre escolha
"""

class AUV():
    def __init__(self, numThursters, listaDeSensores, anoDeConstrucao, nomeVeiculo, velMaxima):
        self.numThursters = numThursters
        self.listaDeSensores = listaDeSensores
        self.anoDeConstrucao = anoDeConstrucao
        self.nomeVeiculo = nomeVeiculo
        self.velMaxima = velMaxima

    def __gt__(self, AUV2):
        return (self.anoDeConstrucao > AUV2.anoDeConstrucao)

    def getAnoDeConstrucao(auv):
        return auv.anoDeConstrucao

def exibeEmTabela(listaDeAUV):
    print(" Nome \tNúmero de Thrsters\t\t\t\tLista de Sensores\t\t\t\t   Ano de Construção \t   Velocidade Máxima")
    for i in range(0, len(listaDeAUV)):
        print("\n", listaDeAUV[i].nomeVeiculo, "\t\t", listaDeAUV[i].numThursters, "\t\t   ",
              listaDeAUV[i].listaDeSensores, "\t\t", listaDeAUV[i].anoDeConstrucao, "\t\t\t",
              listaDeAUV[i].velMaxima, "km/h");

def exibeIndividualmente(listaDeAUV):
    for i in range(0, len(listaDeAUV)):
        print("Nome:\t\t\t", listaDeAUV[i].nomeVeiculo)
        print("Número de Thrusters:\t", listaDeAUV[i].numThursters)
        listaTemp = ""
        for j in range (0, len(listaDeAUV[i].listaDeSensores)):
            listaTemp += listaDeAUV[i].listaDeSensores[j].replace("'", "")
            if(j != len(listaDeAUV[i].listaDeSensores) - 1):
                listaTemp += ", "
        print("Lista de Sensores:\t", listaTemp)
        print("Ano de Construção:\t", listaDeAUV[i].anoDeConstrucao)
        print("Velocidade Máxima:\t", listaDeAUV[i].velMaxima, "km/h")
        print("\n")

def rankearPorIdade (listaDeAUV):
    listaTemp = listaDeAUV
    listaTemp.sort(key = lambda x: x.anoDeConstrucao, reverse = True)
    exibeIndividualmente(listaTemp)

def rankearPorVelocidade (listaDeAUV):
    listaTemp = listaDeAUV
    listaTemp.sort(key = lambda x: x.velMaxima, reverse = True)
    exibeIndividualmente(listaTemp)

auv1 = AUV (2, ["Infravermelho", "Ultrassom", "Profundidade", "Giroscópio"], 2018, "AUV1", 10)
auv2 = AUV (4, ["Infravermelho", "Ultrassom", "Profundidade", "Acelerômetro"], 2019, "AUV2", 8)
auv3 = AUV (5, ["Ultrassom", "Profundidade", "Giroscópio", "Acelerômetro"], 2021, "AUV3", 9)
auv4 = AUV (3, ["Infravermelho", "Profundidade", "Giroscópio", "Acelerômetro"], 2022, "AUV4", 12)
listaDeAUV = [auv1, auv2, auv3, auv4]

print("Exibindo todos os AUV's em tabela:\n")
exibeEmTabela(listaDeAUV)
print("\n\nExibindo os robôs individualmente:")
exibeIndividualmente(listaDeAUV)
print("\n\nRankeamento do mais novo ao mais velho:")
rankearPorIdade(listaDeAUV)
print("\n\nRankeamento do mais rápido ao mais lento:")
rankearPorVelocidade(listaDeAUV)
