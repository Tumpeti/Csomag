def bekeres():
    etel_neve = input("Kérem adja meg az étel nevét: ")
    rendelo_neve = input("Kérem adja meg a rendelő nevét: ")
    ertekeles = int(input("Kérem adja meg értékelését: "))
    while ertekeles > 5 or ertekeles < 0:
        if ertekeles < 0:
            ertekeles = int(input("Az értékelés nem lehet negatív! "))
        elif ertekeles > 5:
            ertekeles = int(input("5 pont feletti értékelés nem elfogadható! "))

    print("I/A, B:")
    print(f"\tÉtel neve: {etel_neve}\n\tÉtel renelőének neve: {rendelo_neve}\n\tÉrtékelés (1-5): {ertekeles}" )
    print(f"I/C:\n\tKöszönjük az értékelést!")
