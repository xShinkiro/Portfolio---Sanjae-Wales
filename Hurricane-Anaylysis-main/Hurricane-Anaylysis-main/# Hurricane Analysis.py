# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
# 1
# Update Recorded Damages
conversion = {"M": 1000000,
             "B": 1000000000}
#print(conversion.get("B")) 
#print(conversion.get("M")) 

def updating_damages(list1):
    updated_damages = []
    for i in list1: 
        if i == 'Damages not recorded':
            updated_damages.append(i)
        elif "B" in i:
            new_number = float(i.strip("B")) * conversion.get("B")
            updated_damages.append(new_number)
          
        elif "M" in i:
            new_number = float(i.strip("M")) * conversion.get("M")
            updated_damages.append(new_number)

    return updated_damages 

zipped_list = zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
updated_damages = updating_damages(damages)
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
    hurricanes_name = dict()
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        hurricanes_name[names[i]] = {"Name": names[i],
                              "Month": months[i],
                              "Year": years[i],
                              "Max Sustained Wind": max_sustained_winds[i],
                              "Areas Affected": areas_affected[i],
                              "Damage": updated_damages[i],
                              "Deaths": deaths[i]}
    return hurricanes_name

hurricanes= create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)

def create_hurri_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
#Create dictionary of hurricanes with hurricane year as the key and a dictionary of hurricane data as the value.
    hurricanes_year = dict()
    num_hurricanes = len(years)
    for i in range(num_hurricanes):
        hurricanes_year[years[i]] = {"Name": names[i],
                              "Month": months[i],
                              "Year": years[i],
                              "Max Sustained Wind": max_sustained_winds[i],
                              "Areas Affected": areas_affected[i],
                              "Damage": updated_damages[i],
                              "Deaths": deaths[i]}
    return hurricanes_year

hurricanes_year = create_hurri_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes_year)


#for name, month, year, max_sustained_wind, area_affected, damage, death in zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths):               
#updating_damages(damages)

#print(updated_damages)
# test function by updating damages

#Counting damaged areas

def areas_count(hurricanes):
    affected_areas_count = dict()
    for cane in hurricanes:
        for area in hurricanes[cane]['Areas Affected']:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count

affected_areas_count = areas_count(hurricanes)
print(affected_areas_count)

# 5
# Calculating Maximum Hurricane Count
def most_affected_area(affected_areas_count):
    """Find most affected area and the number of hurricanes it was involved in."""
    max_area = 'Central America'
    max_area_count = 0
    for area in affected_areas_count:
        if affected_areas_count[area] > max_area_count:
            max_area = area
            max_area_count = affected_areas_count[area]
    return max_area, max_area_count

# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = most_affected_area(affected_areas_count)
print(max_area, max_area_count)

def highest_mortality(hurricanes):
    """Find the highest mortality hurricane and the number of deaths it caused."""
    max_mortality_cane = 'Cuba I'
    max_mortality = 0
    for cane in hurricanes:
        if hurricanes[cane]['Deaths'] > max_mortality:
            max_mortality_cane = cane
            max_mortality = hurricanes[cane]['Deaths']
    return max_mortality_cane, max_mortality

# find highest mortality hurricane and the number of deaths
max_mortality_cane, max_mortality = highest_mortality(hurricanes)
print(max_mortality_cane, max_mortality)

# Rating Hurricanes by Mortality
def categorize_by_mortality(hurricanes):
    """Categorize hurricanes by mortality and return a dictionary."""
    mortality_scale = {0: 0,
                      1: 100,
                      2: 500,
                      3: 1000,
                      4: 10000}
    hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for cane in hurricanes:
        num_deaths = hurricanes[cane]['Deaths']
        if num_deaths == mortality_scale[0]:
            hurricanes_by_mortality[0].append(hurricanes[cane])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(hurricanes[cane])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(hurricanes[cane])
        elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(hurricanes[cane])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(hurricanes[cane])
        elif num_deaths > mortality_scale[4]:
            hurricanes_by_mortality[5].append(hurricanes[cane])
    return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = categorize_by_mortality(hurricanes)
print(hurricanes_by_mortality)
    
def highest1_damage(hurricanes):
    max_damage_cane = 'Cuba I'
    max_damage = 0

    for cane in hurricanes:
        if hurricanes[cane]['Damage'] == "Damages not recorded":
            continue
        elif hurricanes[cane]['Damage'] > max_damage:
            max_damage_cane = cane 
            max_damage = hurricanes[cane]['Damage']
        
    return max_damage_cane, max_damage
highest_damage = highest1_damage(hurricanes)
print(highest_damage)

def scale_of_damage(hurricanes):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    scale_of_damages =  {0: [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : []}
    for cane in hurricanes:
        total_damages = hurricanes[cane]['Damage']
        if hurricanes[cane]['Damage'] == "Damages not recorded":
            continue
        elif hurricanes[cane]['Damage']:
            if total_damages == damage_scale[0]:
                scale_of_damages[0].append(hurricanes[cane])
            elif total_damages > damage_scale[0] and total_damages <= damage_scale[1]:
                scale_of_damages[1].append(hurricanes[cane])
            elif  total_damages <= damage_scale[2]:
                scale_of_damages[2].append(hurricanes[cane])
            elif  total_damages <= damage_scale[3]:
                scale_of_damages[3].append(hurricanes[cane])
            elif  total_damages <= damage_scale[4]:
                scale_of_damages[4].append(hurricanes[cane])
            elif  total_damages > damage_scale[4]:
                scale_of_damages[5].append(hurricanes[cane])
    return scale_of_damages

scale_of_damages = scale_of_damage(hurricanes)
print(scale_of_damages)


      







































