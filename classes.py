from platform import python_version, system

print(python_version())
print(system())

class Movie:
    def __init__(self, title, year, imdb, have_seen):
        self.title = title
        self.year = year
        self.imdb = imdb
        self.have_seen = have_seen

    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb)
        print("I have seen it: ", self.have_seen)


film1 = Movie("Life of Brian", 1979, 8.1, True)

film1.nice_print()