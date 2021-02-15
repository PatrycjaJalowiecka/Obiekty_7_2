class Movies:
    Library_list = []

    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.Library_list.append(self)
        self.no_play = 100

    def __str__(self):
        return f' {self.title} {self.year}' 

    def __repr__(self):
        return f" title = {self.title} year = {self.year}" 

    def play(self, step=1):
        self.no_play += step

movie1 = Movies(title = "The Producers", year = "1968", genre = "comedy")
movie2 = Movies(title = "The Bourne Identity", year = "2002", genre = "thriller")

class TV_series(Movies):
    Library_list = []

    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)
        self.Library_list.append(self)

        ##Variables
        self.episode_no = 0
        self.season_no = 0
        self.no_play = 100

    def __str__(self):
        return f' {self.title} S{self.season_no}E{self.episode_no}' 

    def __repr__(self):
        return f" title = title = {self.title} S, season_no = {self.season_no} E, episode_no = {self.episode_no}"

    def play(self, step=1):
        self.no_play += step

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

series1 = TV_series(title = "House M.D.", year = "2004 - 2007", genre = "drama, comedy")
series2 = TV_series(title = "Doctor Who", year = "1963 - 2020 ", genre = "science fiction" )

print(movie1)
print(series2)
##print(Library_list)