import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    opzione = input("Seleziona un'opzione: ")

    # Add input control here!

    if int(opzione) == 1:
        txtIn = input("Ok, quale parola devo aggiungere? ")
        t.handleAdd(txtIn)
        print("Aggiunta!\n")
    if int(opzione) == 2:
        txtIn = input("Ok, quale parola devo cercare? ")
        """input_valido = True
        for char in txtIn:
            if not (65 < ord(char) < 90 or 97 < ord(char) < 122):
                input_valido = False
                print("Inserimento non valido, per parole con caratteri speciali selezionare l'opzione 3.\n")
                break
        if input_valido is True:
            print(t.handleTranslate(txtIn))"""
        if txtIn.isalpha():
            print(t.handleTranslate(txtIn))
        else:
            print("Inserimento non valido, per parole con caratteri speciali selezionare l'opzione 3.\n")

    if int(opzione) == 3:
        txtIn = input("Ok, quale parola devo cercare? ")
        pos_da_sostituire = 0
        conta_speciali = 0
        wild_card = ""
        for char in txtIn:
            if not (('a' <= char <= 'z' or 'A' <= char <= 'Z') or char == '?'):
                conta_speciali += 1
                pos_da_sostituire = txtIn.index(char)
        if conta_speciali == 0:
            print(t.handleTranslate(txtIn))
        elif conta_speciali == 1:
            wild_card = txtIn[:pos_da_sostituire]+"?"+txtIn[pos_da_sostituire+1:]
            #print(t.handleWildCard(wild_card))
        else:
            print("Inserimento non valido, è ammesso un solo carattere speciale per parola,"
                  " seleziona nuovamente l'opzione 3 con inserimento corretto.\n")

        print(wild_card)

    if int(opzione) == 4:
        break
