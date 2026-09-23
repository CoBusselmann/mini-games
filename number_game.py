import random

def gissa_nummer():
    print("-------Hej och välkommen-------\n---Gissa nummer mellan 1-100")

    secret_number = random.randint(1, 100) #tar in ett random nummer mellan 1-100
    antal_gissningar = 0 #detta värde är startvärde som skapar en count för hur många gissningar man har gjort.


    while True:
        try:
            gissning = int(input(">>> "))
        except ValueError:
            print("Det där är inte ett gilltigt tal, skriv igen.")
            continue

        if gissning < 0 or gissning >100:
            print("Du har skrivit ett ogiltigt nummer, försök igen.")
            continue

        antal_gissningar += 1 #Lägger till en gissning vid varje körning av loopen.

        if gissning < secret_number:
            print("Du gissade för lågt")

        if gissning > secret_number:
            print("Du gissade för högt")
            
        if gissning == secret_number:
            print(f"Grattis du gissade rätt! numret var {secret_number}, du gissade {antal_gissningar} gånger.")
            break   

def hangman():

    print("---Välkommen till hängagubbe!---")

    answer = "motorbåt"
    rätt_bokstäver = []
    fel_bokstäver = []
    antal_gissningar = 0

    while True:

        bokstav = input("Bokstav: ")


        if bokstav in answer:

            print("Rätt!")
            rätt_bokstäver.append(bokstav)
            print(f"Du har rätt på dessa: {rätt_bokstäver}\nFel på dessa: {fel_bokstäver}")

        if bokstav not in answer: 

            print("Du har fel")
            antal_gissningar += 1
            fel_bokstäver.append(bokstav)
            print(f"Du har rätt på dessa: {rätt_bokstäver}\nFel på dessa: {fel_bokstäver}")

            if antal_gissningar == 20: 
                print("Du har tyvärr förlorat.")
                break
            else: 
                continue

        if all(bokstav in rätt_bokstäver for bokstav in answer):
            print(f"Grattis du vann, ordet var: {answer}")
            break

def meny(): 
    while True:
        print("\n----------MENY----------")
        print("1. Hängagubbe")
        print("2. Gissa nummer")
        print("3. EXIT")
        val = input("Välj spel: ")
        if val == "1":
            hangman()
        elif val == "2":
            gissa_nummer()
        elif val == "3":
            print("!!-Hejdå-!!")
            break
        else: 
            print("Du måste skriva ett alternativ i menyn.")
            continue
if __name__ == "__main__":
    meny()
