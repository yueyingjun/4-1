def stars(tou,tui):
    for ji in range (1,tou):
        for tu in range (1,tou):
         if ji+tu==tou and 2*ji+4*tu==tui:
            print(ji,tu)
stars(35,94)