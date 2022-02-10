from country import*
class Continent:
    def __init__(self, name,countries):
        self.name = name
        self.countries = countries
    def __str__(self):
       s = f"{self.name} has:\n"
       for country in self.countries:
           s += str(country) + "\n"
       return s
    def total_population(self):
        s = 0
        for country in self.countries:
            s += country.population 
        return s
    
canada = Country('Canada',34482779,9984670)
usa = Country('United States of America',313914040,9826675)
mexico = Country('Mexico',112336538,1943950)
countries = [canada,usa,mexico]
north_america = Continent('North America',countries)
print(north_america)
print(f"{north_america.name} has population of {north_america.total_population()}.")