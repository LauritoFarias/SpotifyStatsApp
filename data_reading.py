import pandas

data = pandas.read_json(r'spotify_data\Streaming_History_Audio_2023_10.json')

# Index(['ts', 'username', 'platform', 'ms_played', 'conn_country',
#        'ip_addr_decrypted', 'user_agent_decrypted',
#        'master_metadata_track_name', 'master_metadata_album_artist_name',
#        'master_metadata_album_album_name', 'spotify_track_uri', 'episode_name',
#        'episode_show_name', 'spotify_episode_uri', 'reason_start',
#        'reason_end', 'shuffle', 'skipped', 'offline', 'offline_timestamp',
#        'incognito_mode', 'Count'],
#       dtype='object')



data['Count'] = 1

count = data.groupby(['master_metadata_track_name']).count()['Count']

sorted_by_count = count.sort_values(ascending=False)

print(sorted_by_count)

# print(data.loc[data['ts'] == '2023-05-24T01:13:58Z'])