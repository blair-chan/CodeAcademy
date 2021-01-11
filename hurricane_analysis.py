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

# write your update damages function here:

damages_updated = []
for damage in damages:
    if damage[-1] == 'M':
        cost = float(damage[0:len(damage)-1])*1000000
        damages_updated.append(cost)
    elif damage[-1] == 'B':
        cost = float(damage[0:len(damage)-1])*1000000000
        damages_updated.append(cost)
    else:
        damages_updated.append(damage)
#print(len(damages_updated))
#print(len(damages_updated))


# write your construct hurricane dictionary function here:

#test = dict(zip(names,months))
#print(test)

def make_dict_by_name(names_list, months_list, years_list, max_sustained_winds_list, areas_affected_list, damages_list, deaths_list):
    counter = 0
    new_dict = {}
    while counter < len(names_list):
        new_dict[names_list[counter]] = {'Name': names_list[counter], 'Month': months_list[counter], 'Year': years_list[counter], 
                             'Max Sustained Wind': max_sustained_winds_list[counter], 'Areas Affected': areas_affected_list[counter], 
                             'Damage': damages_list[counter], 'Deaths': deaths_list[counter]}
        counter +=1
    return new_dict

dict_by_name = make_dict_by_name(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)
#print(dict_by_name)

# write your construct hurricane by year dictionary function here:
    
def make_dict_by_year(mydict):
    new_dict = {}
    for key, value in mydict.items():
        new_dict[value.get('Year')] = value
    return new_dict

dict_by_year = make_dict_by_year(dict_by_name)
#print(dict_by_year)



# write your count affected areas function here:

# Make areas affected into a dictionary
# create a list with all of the affected areas listed out

def affected_area_count(area_list):
    master_area_list = []
    new_dict = {}
    for areas in area_list:
        for area in areas: 
            master_area_list.append(area)
    for region in master_area_list:
        new_dict[region] = master_area_list.count(region)
            
            
    return new_dict

affected_area_count_dict = affected_area_count(areas_affected)


# write your find most affected area function here:

def most_hurricanes(mydict):
    max_number = 0
    max_area = ""
    for key, value in mydict.items():
        if value > max_number:
            max_number = value
            max_area = key
    return max_area, max_number

#print(most_hurricanes(affected_area_count_dict))



# write your greatest number of deaths function here:


def find_greatest_deaths(mydict):
    max_number = 0
    max_hurricane = ''
    for key, value in mydict.items():
        if mydict.get(key).get('Deaths') > max_number:
            max_number = mydict.get(key).get('Deaths')
            max_hurricane = key
    return max_hurricane, max_number

#print(find_greatest_deaths(dict_by_name))


# write your catgeorize by mortality function here:
# run through each hurricane in dict_by_name. 1) determine the hurricane rating. 2) Assign the rating to a new dictionary key. 3) Add to the new dictionary
#value list through append the full hurricane dictionary information.
    
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality_rating(mydict):
    new_dict = {}
    for i in range(6):
        temp_dict = {}
        temp_list = []
        for key in mydict.keys():
            deaths = mydict.get(key).get('Deaths') 
            if ((i == 5) and (deaths > mortality_scale.get(i-1))):
                temp_dict = mydict.get(key)
                temp_list.append(temp_dict)
                #print(temp_list)
                #new_dict[i] = temp_list.append(temp_dict)
            elif (i == 0 and deaths <= mortality_scale.get(i)):
                temp_dict = mydict.get(key)
                temp_list.append(temp_dict)
                #print(temp_list)
                #new_dict[i] = temp_list.append(temp_dict)
            elif (i > 0 and i< 5) and (deaths <= mortality_scale.get(i) and deaths > mortality_scale.get(i-1)):
                temp_dict = mydict.get(key)
                temp_list.append(temp_dict)
                #print(temp_list)
                #new_dict[i] = temp_list.append(temp_dict)
        new_dict[i] = temp_list
        #print(new_dict)
    return new_dict
    

dict_by_mortality_rating = mortality_rating(dict_by_name)
#print(dict_by_mortality_rating)
    


# write your greatest damage function here:

def find_greatest_cost(mydict):
    max_cost = 0
    max_hurricane = ''
    for key, value in mydict.items():
        try:
            if mydict.get(key).get('Damage') > int(max_cost):
                max_cost = mydict.get(key).get('Damage')
                max_hurricane = key
        except:
            continue
    return max_hurricane, max_cost

print(find_greatest_cost(dict_by_name))



# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_rating(mydict):
    new_dict = {}
    for i in range(6):
        temp_dict = {}
        temp_list = []
        for key in mydict.keys():
            cost = mydict.get(key).get('Damage')
            try:
                if ((i == 5) and (cost > damage_scale.get(i-1))):
                    temp_dict = mydict.get(key)
                    temp_list.append(temp_dict)
                    #print(temp_list)
                    #new_dict[i] = temp_list.append(temp_dict)
                elif (i == 0 and cost <= damage_scale.get(i)):
                    temp_dict = mydict.get(key)
                    temp_list.append(temp_dict)
                    #print(temp_list)
                    #new_dict[i] = temp_list.append(temp_dict)
                elif (i > 0 and i< 5) and (cost <= damage_scale.get(i) and cost > damage_scale.get(i-1)):
                    temp_dict = mydict.get(key)
                    temp_list.append(temp_dict)
                    #print(temp_list)
                    #new_dict[i] = temp_list.append(temp_dict)
            except:
                continue
        new_dict[i] = temp_list
        #print(new_dict)
    return new_dict

dict_by_cost = damage_rating(dict_by_name)
print(dict_by_cost)