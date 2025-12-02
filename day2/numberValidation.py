import math

def numberValidation(x) :

    numberIsValid = True
    n = 0
    m = 0

    for splitLenght in range(1, len(str(x))):     # für jeden split, zB 1, dann 2, dann 3, dann 4 ... - 6x
        # print("------ Next Loop ------ splitLenght:", splitLenght)
        x = str(x)

        numberOfSplits = math.ceil(len(x)/splitLenght) # z.B. 5 mal der split
        # print("numberOfSplits: ", numberOfSplits)

        numbers = []

        for y in range(0, numberOfSplits) :       # über die Länge von x gehen wir den split durch alle parts  - auch 6x/split
        # wenn hier alle werte gleich sind, dann ist das ganze ding FALSE
            m = m + splitLenght
            abschnitt = x[n:m]
            # print("n: ", n)
            # print("m: ", m)
            # print("Abschnitt " + str(y) + ", Nummer ", abschnitt)
            # print("")

            numbers.append(abschnitt)

            n = n + splitLenght

        # print("numbers LIST: ", numbers)
        # schauen ob alle element in der liste identisch sind
        if len(set(numbers)) == 1 :         # set eliminiert doppelte Elemente in der Liste, len überprüft ob in der Liste nurnoch ein Element übrig ist => d.h. alle sind equal
            numberIsValid = False
            # print(numberIsValid)
        n = 0
        m = 0

    # print(numberIsValid)
    return numberIsValid