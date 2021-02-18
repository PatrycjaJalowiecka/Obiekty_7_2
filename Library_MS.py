class Movies:
    movie_tracker = []    

    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.no_play = 100
        self.ms = ms
        self.movie_tracker.append(self) 

    def __str__(self):
        return f' {self.title} {self.year}' 

    def __repr__(self):
        return f" title = {self.title} year = {self.year}" 
  
    def play(self, step=1):
        self.no_play += step

        ##jeżeli obejrzany, ile razy. Albo słownik z elementami, times - tuple - ile razy obejrzany. Nie dodawaj drugi raz
           ## w play. bo tam oglądam. 
           #  
movie1 = Movies(title = "The Producers", year = "1968", genre = "comedy", ms = "m")
movie2 = Movies(title = "The Bourne Identity", year = "2002", genre = "thriller", ms = "m")
movie3 = Movies(title = "The Duck Soup", year = "1933", genre = "comedy", ms = "m")
movie4 = Movies(title = "M.A.S.H", year = "1970", genre = "comedy", ms = "m")
movie5 = Movies(title = "Harry Potter and the Order of the Phoenix", year = "2007", genre = "Fantasy", ms = "m")
movie6 = Movies(title = "Life of Brian", year = "1979", genre = "comedy", ms = "m")
movie7 = Movies(title = "The Terminator", year = "1984", genre = "Sci-Fi", ms = "m")
movie8 = Movies(title = "Stargate ", year = "1994", genre = "Sci-Fi", ms = "m")
movie9 = Movies(title = "Flatliners", year = "1990", genre = "Sci-fi", ms = "m")
movie10 = Movies(title = "Die Hard", year = "1988", genre = "thriller", ms = "m")
movie11 = Movies(title = "Robin Hood Men in Tights", year = "1993", genre = "comedy", ms = "m")
movie12 = Movies(title = "Blade", year = "1998", genre = "horror", ms = "m")
movie13 = Movies(title = "Ghostbusters", year = "1984", genre = "comedy", ms = "m")
movies_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, movie13]

##for movie in Movies.movie_tracker:
##    print(movie.title, movie.year)

class TV_series(Movies):
    series_tracker = []

    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)
        self.series_tracker.append(self)
        ##Variables
        self.episode_no = 0
        self.season_no = 0
        self.episodes_per_season = 10
        self.seasons_count = 5
        self.no_play = 100
        self.ms = ms

    def __str__(self):
        return f' {self.title} S{self.season_no}E{self.episode_no}' 

    def __repr__(self):
        return f" title = title = {self.title} S, season_no = {self.season_no} E, episode_no = {self.episode_no}"

    def play(self, step=1):
        self.no_play += step
        self.season_no < 6
        if self.episode_no == 10: ## zmienna
            self.season_no += step
            self.episode_no == 1
        else: 
            self.episode_no += step
        "Ostatni odcinek lub zerować"

    @property
    def episode(self):
        return self._episode_no

    @episode.setter
    def episode(self, number):
        if number <= 250:
            self._episode_no = number
        else:
            raise ValueError(f"Please check epiode_no. {number}")
    
    def series(self, step = 1):
        self.season_no += step

series1 = TV_series(title = "House M.D.", year = "2004 - 2007", genre = "drama", ms = "s")
series2 = TV_series(title = "Doctor Who", year = "1963 - 2020 ", genre = "Sci-Fi", ms = "s"  )
series3 = TV_series(title = "The Big Bang Theory ", year = "2007 - 2019 ", genre = "comedy", ms = "s" )
series4 = TV_series(title = "M.A.S.H.", year = "1972 - 1983", genre = "comedy", ms = "s" )
series5 = TV_series(title = "Stargate SG-1", year = "1997 - 2007 ", genre = "sci-Fi", ms = "s" )
series6 = TV_series(title = "Buffy the Vampire Slayer", year = "1997 - 2003", genre = "fantasy", ms = "s" )
series7 = TV_series(title = "Scrubs", year = "2001 - 2010", genre = "comedy", ms = "s" )
series8 = TV_series(title = "Fawlty Towers", year = "1979", genre = "comedy", ms = "s" )
series9 = TV_series(title = "McGyver", year = "1985 - 1992", genre = "thriller", ms = "s" )
series10 = TV_series(title = "Miami Vice", year = "1984 - 1990", genre = "criminal", ms = "s" )
series11 = TV_series(title = "Red Dwarf", year = "1988 - 1999", genre = "comedy", ms = "s" )
series12 = TV_series(title = "Nash Bridges", year = "1996 - 2001", genre = "criminal", ms = "s" )
series13 = TV_series(title = "Castle", year = "2009 - 2016", genre = "criminal", ms = "s" )
series_list = [series1, series2, series3, series4, series5, series6, series7, series8, series9, series10, series11, series12, series13]


class Library(Movies, TV_series):
    Library_list = [series_list] + [movies_list]
    
    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)
        self.series_tracker.append(self)
        ##Variables
        self.episode_no = 0
        self.season_no = 0
        self.no_play = 100
        self.ms = ms

## watch movie metoda, tworzy obiekt movie i wrzuca do listy. self.series_list, self.series. 
##i dodawać do tej listy bezpośrednio. linia 99 library.add_series (series1)
 ##Library.watch_series(series1) i doda do series list i że odcinek obejrzany 
##Library.watch_series(series2)
 
    def get_movies():
        nl = '\n'
        by_title = sorted(Library_list, key = self.title ) ## sortować movie_list
        if self.ms = "m":
            for item in Library_list:
                print(by_title, nl) 
    

    def get_series():
        nl = '\n'
        by_title = sorted(Library_list, key = self.title) ## sortować * series_list
        if self.ms = "s":
            for item in Library_list:
                print(by_title, nl) 

    def search(title): ## do całej listy, 
        title_search = input("Podaj tytuł: ")
        if title_search == self.title:
            print(self.title, self.year, self.genre)
        else:
            print("Nie ma takiego filmu")
            exit(1)        
            

    def generate_views():
        random_view = random.choice(Library_list)
        random_number = randrange(1, 100)
        print(random_number, random.view)

    def generate_views_10():
        for _ in range(10):
            generate_views()

    def top_titles(content_type, number):
        by_no_play = sorted(Library_list, key = self.no_of_play)
        content_type = input("Wybierz czy chcesz zobaczyć listę filmów czy serii m/s: ")
        content_type = self.ms
        number = int(input("Podaj proszę liczbę Top Tytułów, które chcesz zobaczyć: ")
        nl = '\n'
        if content_type == "m":
            if ms == "m": 
                for movie in Library_list in range (0, number): 
                    print (movie, nl)
        elif content_type == "s":
             if ms == "s": 
                for serie in Library_list in range (0, number): 
                    print (serie, nl)
        elif content_type == ""
                for item in Library_list in range (0, number): 
                    print (item, nl) 
        else:
            print("Niewłaściwy parametr")
            exit(1) 