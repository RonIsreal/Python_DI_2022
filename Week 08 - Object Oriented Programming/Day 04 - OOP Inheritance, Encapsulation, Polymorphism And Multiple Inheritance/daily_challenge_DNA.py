import random

random.seed()
genes = [random.randint(0,1) for i in range(10)]

class Genes:
    def __init__(self, genes):
        self.genes = genes

    def SeeGenes(self):
        return self.genes

    def FlipGenes(self):
        pass

class DNA(Genes):

    def __init__(self, cromosomes):
        self.cromosomes = list(genes)

myGenes = Genes(genes)
print(myGenes.SeeGenes())