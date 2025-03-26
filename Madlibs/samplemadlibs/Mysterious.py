def madlib():
    place = input("A Place: ")
    adjective1 = input("An Adjective: ")
    adjective2 = input("Another Adjective: ")
    noun1 = input("A Noun: ")
    verb1 = input("A Verb: ")
    animal = input("An Animal: ")
    noun2 = input("Another Noun: ")
    verb2 = input("Another Verb: ")

    madlib = f"In the {place}, a {adjective1} girl appeared out of nowhere. \
She wore a {adjective2} dress and held a {noun1}. Suddenly, she began to {verb1}, \
causing a {animal} to run past her holding a {noun2}. Everyone nearby started to {verb2}, \
but she just smiled mysteriously and vanished into thin air!"

    print(madlib)
