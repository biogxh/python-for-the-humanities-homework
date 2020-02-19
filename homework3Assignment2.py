A = "Sociobiology is a field of biology that aims to examine and explain social behavior in terms of evolution. It draws from disciplines including psychology, ethology, anthropology, evolution, zoology, archaeology, and population genetics. Within the study of human societies, sociobiology is closely allied to Darwinian anthropology, human behavioral ecology and evolutionary psychology."

Alist = A.split(" ")
FilteredResults = []
L=len(Alist)
Prefix=input("Pleas enter a prefix and the program will finds all the words that start with that prefix")
def find(Word,Prefix,FilteredResults):
    count = 0
    LList = list(Word)
    PPlist = list(Prefix)
    for i in range(len(PPlist)):
        if len(PPlist)> len(LList):
            break
        else:
            if PPlist[i] == LList[i]:
                count += 1
    if count == len(PPlist):
           FilteredResults.append(str(Word))



for i in Alist:    
    find(i,Prefix,FilteredResults)
    
print(len(FilteredResults)) 
print(FilteredResults)