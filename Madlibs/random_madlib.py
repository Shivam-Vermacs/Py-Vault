from samplemadlibs import Thriller, Mysterious, Monster, Haunted
import random

if __name__ == "__main__":
    m = random.choice([Thriller, Mysterious, Monster, Haunted])
    m.madlib()
