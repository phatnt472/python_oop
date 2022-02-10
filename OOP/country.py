class Country:
  def __init__(self, country_name, population, area):
    self.country_name = country_name
    self.area = area
    self.population = population
  def is_lagrer(self,other):
    return self.area > other.area
  def density(self):
    return self.population/self.area
  def __str__(self):
    return f'{self.country_name} has a population of {self.population} and is {self.area} square km.'
  
  def __repr__(self):
    return f'Country({self.country_name},{self.population},{self.area})'

  

# if __name__ == '__main__':
#   canada = Country('Canada',34482779,9984670)
#   usa = Country('United States of America',313914040,9826675)
#   print("Name:",canada.country_name)
#   print("Population:",canada.population)
#   print("Area:",canada.area)
#   print(usa.country_name)
#   print("Population:",usa.population)
#   print("Area:",usa.area)
#   if canada.is_lagrer(usa):
#     print(f'{canada.country_name} is lagrer than {usa.country_name}')
#   else:
#     print(f'{canada.country_name} is not lagrer than {usa.country_name}')
#   print(canada.density())
#   print(usa)
#   print([canada])
