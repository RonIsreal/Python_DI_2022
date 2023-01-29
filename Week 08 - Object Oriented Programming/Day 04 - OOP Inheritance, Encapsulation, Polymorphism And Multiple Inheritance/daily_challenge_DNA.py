import random

class Gene:

    def __init__(self):
        self.gene = random.randint(0,1)

    def mutate(self):
        if self.gene == 0:
            self.gene = 1
        else:
            self.gene = 0

    def __repr__(self):
        return f"{self.gene}"

class Chromosome:

    def __init__(self):
        self.chromosomes = []
        while len(self.chromosomes) < 10:
            self.chromosomes.append(Gene())

    def __repr__(self):
        return f"{self.chromosomes}"

class DNA:

    def __init__(self):
        self.dna = [Chromosome() for i in range(10)]

    def __repr__(self):
        return f"DNA({self.dna})"

class Organism:

    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment
        self.counter = 0

    def chancetomutate(self):
        randomnumber = random.randint(0,100)
        for genes in dna:

            if randomnumber in range(0,environment):
                Gene.mutate(self)

            else:
                pass



mydna = DNA()
print(DNA())
testgene = Gene()
print(testgene)
testgene.mutate()
print(testgene)
myOrganism = Organism(mydna, 25)
print(myOrganism.dna)

