
aktive_player = "X"

                            # Aktuelles Tic Tac Toe Spielfeld
spielfeld = ["",
             "1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

run = True

def spielfeld_anzeigen():   # Spielfeld wird Angezeigt
    print(str(spielfeld[1:4]) + "\n" + str(spielfeld[4:7]) + "\n" + str(spielfeld[7:]))


def next_move():            # hier wird der Spielzug definiert
    global run
    while True:
        player_move = input("Bitte das gewünschte Feld eingeben: ")
        if player_move == "q":                                          # Prüft ob das spiel abgebrochen werden soll
            print("Spiel wird geschlossen")
            run = False
            return
        elif player_move =="Q":
            print("Spiel wird geschlossen")
            run = False
            return
        try:
            player_move = int(player_move)
            if player_move >= 1 and player_move <= 9:                                       # Prüft es zahl 1-9 ist
                if spielfeld[player_move] == "X" or spielfeld[player_move] == "O":          # Prüft ob das Spielfeld bereits Belegt wurde.
                    print("Spielfeld bereits belegt, bitte wiederhole Suche dir ein anderes Feld aus......")
                else:
                    return player_move
            else:
                print("bitte Zahle 1-9 eingeben...")
        except ValueError:
            print("Die eingebene Zahl ist Falsch, Bitte nur 1-9 eingeben...")

def change_player():            # Wechselt zwischen spieler 1 und 2
    global aktive_player
    if aktive_player == "X":
        aktive_player = "O"
    else:
        aktive_player = "X"

def check_win():
    # Zeilen prüfen
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]

    # spalte prüfen
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[1]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[1]

    # diagonal prüfen
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[1]
    if spielfeld[3] == spielfeld[5] == spielfeld[7]:
        return spielfeld[3]

def check_draw(): # unentschieden Prüfen
    if spielfeld[1] != "1" and spielfeld[2] != "2" and spielfeld[3] != "3" and spielfeld[4] != "4" \
            and spielfeld[5] != "5" and spielfeld[6] != "6" and spielfeld[7] != "7" and spielfeld[8] != "8" \
                    and spielfeld[9] != "9":
        return True


while run:

    spielfeld_anzeigen()
    player_move = next_move()
    spielfeld[player_move] = aktive_player
    winner = check_win()                                                    # wird entweder "X" oder "O" wiedergegeben
    if winner:
        spielfeld_anzeigen()
        print("Spieler " + winner + " hat gewonnen")
        run = False
    if check_draw():
        spielfeld_anzeigen()
        print("Es ist unentschieden...")
        run = False
    change_player()

