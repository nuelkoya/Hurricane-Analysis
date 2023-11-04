# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 
'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 
'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 
'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 
'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 
'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 
'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 
1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 
175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], [
    'Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
    ['The Bahamas', 'Northeastern United States'], 
    ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
    ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], 
    ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
    ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
    ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], 
    ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], 
    ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], 
    ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], 
    ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
    ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
    ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
    ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
    ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
    ['Bahamas', 'United States Gulf Coast'], 
    ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], 
    ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
    ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
    ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
    ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 
'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 
'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,
124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def convert_damages(damages):
  damages_updated = []
  for damage in damages:
    if damage[-1] == 'M':
      damages_updated.append(float(damage.replace('M','')) * 1000000)
    elif damage[-1] == 'B':
      damages_updated.append(float(damage.replace('B','')) * 1000000000)
      
    else:
      damages_updated.append(damage)
  return damages_updated

#print(convert_damages(damages))
damages = convert_damages(damages)



# 2 
# Create a Table

# Create and view the hurricanes dictionary

def data_construction(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  data = zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
  new_data = {}

  for item in data:
    new_data[item[0]] = {'Name': item[0], 'Month': item[1], 'Year': item[2], 'Max Sustained Wind': item[3], 'Areas Affected': item[4], 'Damage': item[5], 'Deaths': item[6]}
  return new_data


hurricane_data = data_construction(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricane_data["Cuba I"]['Year'])


# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
hurricane_data_year = {}

def arranging_hurricane_data_by_year(hurricane_data):
  for item in hurricane_data:
    if not hurricane_data[item]['Year'] in hurricane_data_year.keys():
      #print("Special!!! " + str(hurricane_data[item]['Year']))
      hurricane_data_year[hurricane_data[item]['Year']] = [hurricane_data[item]]
    else:
      #print(hurricane_data[item]['Year'])
      hurricane_data_year[hurricane_data[item]['Year']].append(hurricane_data[item])
  return hurricane_data_year


hurricane_data_year = arranging_hurricane_data_by_year(hurricane_data)
#print(hurricane_data_year[1933])
#print("\n")




# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

def areas_count(hurricane_data_year):
  count_of_area = {}
  for each_data in hurricane_data_year.values():
    for item_data in each_data:
      for each_area in item_data['Areas Affected']:
        #print(item_data['Areas Affected'])
        #print(each_area)
        if not each_area in count_of_area:
          count_of_area[each_area] = 1
        else:
          count_of_area[each_area] += 1
  return count_of_area

area_count = areas_count(hurricane_data_year)




# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in

def most_area_with_hurricane(area_count):
  max_area = 'Central America'
  max_area_count = 0
  for each_area in area_count.items():
    if each_area[1] > max_area_count:
      max_area_count = each_area[1]
      max_area = each_area[0]
    return max_area, max_area_count


max_area_count = {}
max_area_count.update({str(most_area_with_hurricane(area_count)[0]): most_area_with_hurricane(area_count)[1]})
#print(max_area_count)

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def most_death(hurricane_data_year):
  count = 0
  max_death_area = 'Cuba I'
  max_death_count = 0
  for each_data in hurricane_data_year.values():
    for inner_data in each_data:
      if inner_data['Deaths'] > max_death_count:
        max_death_count = inner_data['Deaths']
        max_death_area = inner_data['Name']

  return max_death_area, max_death_count


max_death={}
max_death.update({most_death(hurricane_data_year)[0]: most_death(hurricane_data_year)[1]})

#print(max_death)



# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key
def hurricane_rating(hurricane_data_year):
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  mortality = {0: [], 1:[], 2:[], 3 : [], 4 : []}
  #mortality ={}
  for each_data in hurricane_data_year.values():
    for inner_data in each_data:
      #print(inner_data)
      #print(inner_data["Deaths"])
      if inner_data["Deaths"] > 0 and inner_data["Deaths"] <= 100:
        mortality[0].append(inner_data)
      elif inner_data["Deaths"] > 100 and inner_data["Deaths"] < 500:
        mortality[1].append(inner_data) 
      elif inner_data["Deaths"] > 500 and inner_data["Deaths"] <= 1000:
        mortality[2].append(inner_data)
      elif inner_data["Deaths"] > 1000 and inner_data["Deaths"] <= 10000:
        mortality[3].append(inner_data)
      elif inner_data["Deaths"] > 10000:
        mortality[4].append(inner_data)
           
  return mortality


mortality_rating = hurricane_rating(hurricane_data_year)
#print(mortality_rating)

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost

def greatest_damage(hurricane_data_year):
  greatest_damage_name = 'Cuba I'
  greatest_damage_count = 0
  for each_data in hurricane_data_year.values():
    for inner_data in each_data:
      if type(inner_data['Damage']) == float:
        if inner_data['Damage'] > greatest_damage_count:
          greatest_damage_name = inner_data['Name']
          greatest_damage_count = inner_data['Damage']
  return greatest_damage_name,greatest_damage_count


greatest_damage_dict = {}
greatest_damage_dict.update({greatest_damage(hurricane_data_year)[0]: greatest_damage(hurricane_data_year)[1]})
#print(greatest_damage_dict)



# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def damage_ratings(hurricane_data_year):
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

  damage = {0: [], 1:[], 2:[], 3 : [], 4 : [], 5: []}

  for each_data in hurricane_data_year.values():
    for inner_data in each_data:
      #print(inner_data)
      #print(inner_data["Deaths"])
      if type(inner_data["Damage"]) == float:
        if inner_data["Damage"] > 0 and inner_data["Damage"] <= 100000000:
          damage[0].append(inner_data)
        elif inner_data["Damage"] > 100000000 and inner_data["Damage"] < 1000000000:
          damage[1].append(inner_data) 
        elif inner_data["Damage"] > 1000000000 and inner_data["Damage"] <= 10000000000:
          damage[2].append(inner_data)
        elif inner_data["Damage"] > 10000000000 and inner_data["Damage"] <= 50000000000:
          damage[3].append(inner_data)
        elif inner_data["Damage"] > 50000000000:
          damage[4].append(inner_data)
      else:
        damage[5].append(inner_data)
  return damage

print(damage_ratings(hurricane_data_year))