#!/usr/bin/env python3

from rdapi import RD

'''
System

'''

# print(RD().system.disable_token())

# print(RD().system.time().content)

# print(RD().system.iso_time().content)

'''
User

'''

# print(RD().user.get().json())

'''
Unrestrict

'''

# print(RD().unrestrict.check(link="https://www.youtube.com/watch?v=aqz-KE-bpKQ").json())

# print(RD().unrestrict.link(link="https://real-debrid.com/d/example").json())

# print(RD().unrestrict.folder(link="https://clicknupload.vip/example").json())

# import os
# filepath = os.getcwd() + '/Testpackage.dlc'
# print(filepath)
# print(RD().unrestrict.container_file(filepath).json())

# print(RD().unrestrict.container_link(link="example").json())

'''
Traffic

'''

# print(RD().traffic.get().json())

# import datetime
# start = datetime.datetime(2023, 6, 25)
# end = datetime.datetime(2023, 9, 10)
# print(RD().traffic.details(start, end).json())

'''
Streaming

'''

# print(RD().streaming.transcode('example_id').json())

# print(RD().streaming.media_info('example_id').json())

'''
Downloads

'''

# print(RD().downloads.get(limit=10, page=2).json())

# print(RD().downloads.delete('example_id'))

'''
Torrents

'''

# print(RD().torrents.get(limit=10, page=1).json())

# print(RD().torrents.info('example_id').json())

# print(RD().torrents.instant_availability('FE7E3784A298169D8DE3804B8FDE5EC318105194').json())

# print(RD().torrents.active_count().json())

# print(RD().torrents.available_hosts().json())

# import os
# filepath = os.getcwd() + '/bbb.torrent'
# print(filepath)
# print(RD().torrents.add_file(filepath=filepath).json())

# print(RD().torrents.add_magnet('FE7E3784A298169D8DE3804B8FDE5EC318105194').json())

# print(RD().torrents.select_files('example_id', 'all'))

# print(RD().torrents.delete('example_id'))

'''
Hosts

'''

# print(RD().hosts.get().json())

# print(RD().hosts.status().json())

# print(RD().hosts.regex().json())

# print(RD().hosts.regex_folder().json())

# print(RD().hosts.domains().json())

'''
Settings

'''

# print(RD().settings.get().json())

# print(RD().settings.update('streaming_language_preference', 'eng'))

# print(RD().settings.convert_points())

# print(RD().settings.change_password())

# import os
# filepath = os.getcwd() + '/avatar.png'
# print(filepath)

# print(RD().settings.avatar_file(filepath))

# print(RD().settings.avatar_delete())
