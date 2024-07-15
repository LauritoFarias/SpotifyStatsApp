import pandas as pd
from datetime import date

def load_stats(data):
    get_most_plays_by_category(data, 'artist')
    #get_most_plays_by_category(data, 'track')
    #get_most_plays_by_category(data, 'album')
    get_most_plays_by_time_period(data, 'day')

def read_file(file_path):
    data = pd.read_json(file_path)
    return data

def get_most_plays_by_category(data_frame, category):
    match category:
        case 'track':
            categorical_index = 'master_metadata_track_name'
        case 'artist':
            categorical_index = 'master_metadata_album_artist_name'
        case 'album':
            categorical_index = 'master_metadata_album_album_name'
        case _:
            categorical_index = None
    data_frame['Count'] = 1
    count = data_frame.groupby([categorical_index]).count()['Count']
    sorted_by_count = count.sort_values(ascending=False)
    print(sorted_by_count)

def get_most_plays_by_time_period(data_frame, time_period):
    match time_period:
        case 'day':
            get_most_plays_by_day(data_frame)

def get_most_plays_by_day(data_frame):
    str_date = data_frame['ts'].split('T')[0]
    date_numbers = str_date.split('-')
    data_frame['day'] = date(*date_numbers)
    play_count_by_day = data_frame['day'].value_counts().sort_index()
    print(play_count_by_day)