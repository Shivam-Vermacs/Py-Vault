def madlib():
    place = input("A Place: ")
    adjective1 = input("An Adjective: ")
    verb1 = input("A Verb Ending in -ing: ")
    noun1 = input("A Noun: ")
    adjective2 = input("Another Adjective: ")
    verb2 = input("Another Verb: ")
    sound = input("A Sound: ")

    madlib = f"It was a {adjective1} night at the {place}. The wind was {verb1} through the trees, \
and I clutched my {noun1} tightly. Suddenly, a {adjective2} shadow appeared, and I heard a {sound}. \
I tried to {verb2}, but my legs wouldnt move. Whatever it was, it was getting closer!"

    print(madlib)
