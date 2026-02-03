
nenndurchmesser_schrauben = [3,4,5,6,8,10]

spannungsquerschnitt = 0.8 * (3.14*nenndurchmesser_schrauben[0]**2)/4

zugfestigkeiten = [400, 800, 1000]
vorspannkraft = 0.2 * nenndurchmesser_schrauben * spannungsquerschnitt * zugfestigkeiten[0]

anziehdrehmoment = 0.2 * nenndurchmesser_schrauben * vorspannkraft


for durchmesser in nenndurchmesser_schrauben:
    print(f"M{durchmesser}     |", end="")

    #for zugfestigkeit in zugfestigkeiten: