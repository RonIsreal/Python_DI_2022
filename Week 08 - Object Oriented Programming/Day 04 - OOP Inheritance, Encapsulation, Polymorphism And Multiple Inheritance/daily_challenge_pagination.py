class Pagination:

    def __init__(self, items, pageSize=10):
        self.items = list(items)
        self.visibleItems = []
        self.pagesize = pageSize
        self.currentpage = 0

    def getVisitbleItems(self):
        self.visibleItems = [self.items[i * self.pagesize:(i + 1) * self.pagesize] for i in range((len(self.items) + self.pagesize - 1) // self.pagesize )]
        return self.visibleItems[0]

    def nextPage(self):
        self.currentpage += 1
        return self.visibleItems[self.currentpage]

    def previousPage(self):
        self.currentpage -= 1
        return self.visibleItems[self.currentpage]

    def firstPage(self):
        return self.visibleItems[0]

    def lastPage(self):
        return self.visibleItems[-1]

    def goToPage(self):
        self.currentpage = int(input(f"Please choose a page between 0 and {len(self.visibleItems)}: "))
        return self.visibleItems[self.currentpage - 1]



alphabetList = "abcdefghijklmnopqrstuvwxyz"


p = Pagination(alphabetList,4)
print(p.getVisitbleItems())
print(p.nextPage())
print(p.previousPage())
print(p.lastPage())
print(p.visibleItems)
print(p.goToPage())
