from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dizionario = []


    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("TRANSLATOR ALIEN-ITALIAN\n")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        f = open(dict, "r")
        riga = f.readline()
        while riga != "":
            riga_modif = ""
            for char in riga:
                if char != '\n':
                    riga_modif += char
            self.dizionario.append(riga_modif)
            riga = f.readline()
        f.close()

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parola_split = entry.lower().split(" ")
        esistente = False
        for w in self.dizionario:
            if parola_split[0] in w:
                esistente = True
                nuove_trad = ""
                for i in range(1, len(parola_split)):
                    nuove_trad += (" "+parola_split[i])
                self.dizionario[self.dizionario.index(w)] += nuove_trad   #w += nuove_trad
        if esistente is False:
            self.dizionario.append(entry.lower())
        f = open("dictionary.txt", "w")
        for p in self.dizionario:
            f.write(p + "\n")
        f.close()

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        dizz = Dictionary(self.dizionario)
        return dizz.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass


#test handleAdd
"""
diz = Translator()
diz.loadDictionary("dictionary.txt")
entry = "ajeje desco scrivania"
parola_split = entry.lower().split(" ")
esistente = False
for w in diz.dizionario:
    if parola_split[0] in w:
        esistente = True
        nuove_trad = ""
        for i in range(1, len(parola_split)):
            nuove_trad += (" "+parola_split[i])
        diz.dizionario[diz.dizionario.index(w)] += nuove_trad
if esistente is False:
    diz.dizionario.append(entry.lower())
f = open("dictionary.txt", "w")
for p in diz.dizionario:
    f.write(p + "\n")
f.close()
"""