class Dictionary:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def addWord(self, word):
        self.dictionary.append(word.lower())

    def translate(self, aliena):
        trovata = False
        for w in self.dictionary:
            if aliena.lower() in w.lower():
                trovata = True
                riga_split = w.split(" ")
                if len(riga_split) == 2:
                    return riga_split[1]+"\n"
                elif len(riga_split) > 2:
                    traduzione = ""
                    primo = False
                    for i in range(1, len(riga_split)):
                        if primo is False:
                            traduzione += riga_split[i]
                            primo = True
                        else:
                            traduzione += " "+riga_split[i]
                    return traduzione
        if trovata == False:
            return "Parola non trovata\n"

    def translateWordWildCard(self):
        pass

