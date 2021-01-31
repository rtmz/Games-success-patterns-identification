from igdb.wrapper import IGDBWrapper
#import urllib.parse
import time
import json
import csv


wrapper = IGDBWrapper(<INSERT API key here>)

categories = ['Three', 'Seven', 'Twelve', 'Sixteen', 'Eighteen', 'RP', 'EC', 'E', 'E10+', 'T','M', 'AO'  ]
platforms_dict = {'Wii':5, 'NES':18, 'GB':33, 'DS':20, 'X360':12, 'PS3':9, 'PS2':8, 'SNES':19, 'GBA':24,
       'PS4':48, '3DS':37, 'N64':4, 'PS':7, 'XB':11, 'PC':6, '2600':59, 'PSP':38, 'XOne':49,
       'WiiU':41, 'GC':21, 'GEN':29, 'DC':23, 'PSV':46, 'SAT':32, 'SCD':78, 'WS':57, 'NG':136, 'TG16':150,
       '3DO':50, 'GG':35}

# Convert unix time in seconds into year
def get_year(secs):
    return time.localtime(secs).tm_year

# Do API request to get ESRB age rating 
def get_rating(ids):
    for idd in ids:
        byte_array = wrapper.api_request(
                    'age_ratings',
                    'fields *; offset 0;where id = '+str(idd)+';'
                    )
        json_data = json.loads(byte_array)

        for cat in json_data:
            # Give up if it's not ESRB type
            if cat['category']!=1:
                break
            return categories[cat['rating']-1]

# Do API request to get release date for the platform        
def get_release_date(rels, platform):
   
    for idd in rels:
        
        byte_array = wrapper.api_request(
                    'release_dates',
                    'fields *; offset 0;where id = '+str(idd)+';'
                    )
        json_data = json.loads(byte_array)    

        for rel in json_data:
            if rel['platform'] == platform:
                if 'y' in rel.keys():
                    return rel['y']
                else:
                    return 2020
#  return infinity=2020 if no information found
    return 2020    


# Do API call to find game info based on game name and platform name
def get_game_info(game_name, platform_name):

    platform_name = str(platform_name)
    # first trying to use the main name as a condition
    byte_array = wrapper.api_request(
                'games',
               'fields id, name, first_release_date, release_dates,age_ratings, platforms; offset 0; where  name="'+game_name+'";'
                )


    json_data = json.loads(byte_array)
    # if no success, try alternative names
    if  len(json_data) ==0:
        byte_array = wrapper.api_request(
                    'alternative_names',
                    'fields *; offset 0; limit 1;where name="'+game_name+'";' 
                    )

        json_data = json.loads(byte_array)
    # if still no success, try to make search and take the first most relevant
        if  len(json_data) ==0:
            byte_array = wrapper.api_request(
                        'games',
                        'search "'+game_name+'"; fields id, name, first_release_date, release_dates,age_ratings, platforms; offset 0; limit 1;' 
                        )
            json_data = json.loads(byte_array)
     # if no query succeded give up and return NaN
            if  len(json_data) == 0:
                return ('NaN','NaN')   
     #if alternative name search was successful do API call to get game by ID
        else:
            game_id =  json_data[0]['game']
            byte_array = wrapper.api_request(
                        'games',
                        'fields id, name, first_release_date, release_dates,age_ratings, platforms; offset 0; where  id='+str(game_id)+';' 
                        )
            json_data = json.loads(byte_array)

  

    for game in json_data:
        rating = 'NaN'
        release_year = 'NaN'
        first_release = 'NaN'

        if 'age_ratings' in game.keys():
            age_ids =  game['age_ratings']            
            rating = get_rating(age_ids)
        if 'release_dates' in game.keys():
            release_year = get_release_date(game['release_dates'], platforms_dict[platform_name])
        # if no year was found let's try another game from the array
            if  release_year==2020:
                continue
        else:
            continue
       
        if  'first_release_date' in game.keys():
            first_release = str(get_year(game['first_release_date']))
        print(game['name']+'\t'+ first_release, rating, release_year)
        # for the first game from the array return the rating and year if found
        return (rating, release_year)

    return ('NaN','NaN')


# open csv with games lack year or rating
with open('noyear.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)


# look at each row and get game info for the game name and the platform
for row in data:
    if row[1] == 'name':
        row.append('rating')
        row.append('release_year')
        continue 
    try:
        rating, release_year = get_game_info(row[1], row[2]) 
        row.append(rating)
        row.append(release_year)
    except Exception as e:
        print("Error occured:", e)   
        continue
# after info was captured write it into file
with open("games_igdb_year.csv", "w", newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
