# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(damages):
    updated_damages = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        else:
            # Extrahiere den Präfix und den Wert
            value = float(damage[:-1])
            suffix = damage[-1]

            # Konvertiere in USD
            updated_damages.append(value * conversion[suffix])
    return updated_damages

# test function by updating damages
updated_damages = update_damages(damages)
print(updated_damages)

# 2
# Create a Table
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': updated_damages[i],
            'Deaths': deaths[i]
        }
    return hurricanes

# Create and view the hurricanes dictionary
# Test der Funktion
hurricanes_dict = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes_dict)

# 3
# Organizing by Year
def organize_by_year(hurricanes_dict):
    hurricanes_by_year = {}
    for hurricane in hurricanes_dict.values():
        year = hurricane['Year']
        # Wenn das Jahr noch nicht als Schlüssel im Dictionary existiert, erstelle eine leere Liste
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = []
        # Füge den aktuellen Hurrikan der Liste des entsprechenden Jahres hinzu
        hurricanes_by_year[year].append(hurricane)
    return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organize_by_year(hurricanes_dict)
print(hurricanes_by_year)

# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes_dict):
    area_count = {}
    for hurricane in hurricanes_dict.values():
        for area in hurricane['Areas Affected']:
            if area not in area_count:
                area_count[area] = 0
            area_count[area] += 1
    return area_count


# create dictionary of areas to store the number of hurricanes involved in

affected_areas_count = count_affected_areas(hurricanes_dict)
print(affected_areas_count)

# 5
# Calculating Maximum Hurricane Count
def most_affected_area(affected_areas_count):
    most_affected = None
    max_count = 0
    for area, count in affected_areas_count.items():
        if count > max_count:
            most_affected = area
            max_count = count
    return most_affected, max_count


# find most frequently affected area and the number of hurricanes involved in
most_affected, count = most_affected_area(affected_areas_count)
print(f"Das am meisten betroffene Gebiet ist: {most_affected}, betroffen {count} mal.")

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes_dict):
    deadliest = None
    max_deaths = 0
    for hurricane in hurricanes_dict.values():
        if hurricane['Deaths'] > max_deaths:
            deadliest = hurricane['Name']
            max_deaths = hurricane['Deaths']
    return deadliest, max_deaths

# find highest mortality hurricane and the number of deaths
deadliest, deaths = deadliest_hurricane(hurricanes_dict)
print(f"Der Hurrikan mit den meisten Todesfällen ist: {deadliest}, mit {deaths} Todesfällen.")

# 7
# Rating Hurricanes by Mortality
def rate_hurricanes_by_mortality(hurricanes_dict):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    rated_hurricanes = {i: [] for i in range(6)}  # Initialisiere ein Dictionary für Ratings von 0 bis 5

    for hurricane in hurricanes_dict.values():
        deaths = hurricane['Deaths']
        rating = 5  # Standardmäßig ist das höchste Rating, wenn keine andere Bedingung zutrifft
        for scale, upper_bound in mortality_scale.items():
            if deaths <= upper_bound:
                rating = scale
                break
        rated_hurricanes[rating].append(hurricane)

    return rated_hurricanes


# categorize hurricanes in new dictionary with mortality severity as key
rated_hurricanes = rate_hurricanes_by_mortality(hurricanes_dict)
print(rated_hurricanes)

# 8 Calculating Hurricane Maximum Damage
def most_costly_hurricane(hurricanes_dict):
    most_costly = None
    max_damage = 0
    for hurricane in hurricanes_dict.values():
        damage = hurricane['Damage']
        # "Damages not recorded" ignorieren
        if isinstance(damage, (int, float)) and damage > max_damage:
            most_costly = hurricane['Name']
            max_damage = damage
    return most_costly, max_damage


# find highest damage inducing hurricane and its total cost
most_costly, damage = most_costly_hurricane(hurricanes_dict)
print(f"Der Hurrikan mit dem größten Schaden ist: {most_costly}, mit einem Schaden von ${damage:.2f}.")


# 9
def rate_hurricanes_by_damage(hurricanes_dict):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    rated_hurricanes = {i: [] for i in range(6)}  # Initialisiere ein Dictionary für Ratings von 0 bis 5

    for hurricane in hurricanes_dict.values():
        damage = hurricane['Damage']
        if not isinstance(damage, (int, float)):
            continue  # "Damages not recorded" ignorieren

        rating = 5  # Standardmäßig ist das höchste Rating, wenn keine andere Bedingung zutrifft
        for scale, upper_bound in damage_scale.items():
            if damage <= upper_bound:
                rating = scale
                break
        rated_hurricanes[rating].append(hurricane)

    return rated_hurricanes

rated_hurricanes_by_damage = rate_hurricanes_by_damage(hurricanes_dict)
print(rated_hurricanes_by_damage)