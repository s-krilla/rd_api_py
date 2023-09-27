#!/usr/bin/env python3

from rdapi import RD

'''
System

'''

RD().system.disable_token()

RD().system.time().content

RD().system.iso_time().content

'''
User

'''

RD().user.get().json()

'''
Unrestrict

'''

RD().unrestrict.check(link="https://www.youtube.com/watch?v=aqz-KE-bpKQ").json()

RD().unrestrict.link(link="https://real-debrid.com/d/example").json()

RD().unrestrict.folder(link="https://clicknupload.vip/example").json()

import os
filepath = os.getcwd() + '/Testpackage.dlc'
RD().unrestrict.container_file(filepath).json()

RD().unrestrict.container_link(link="example").json()

'''
Traffic

'''

RD().traffic.get().json()

import datetime
start = datetime.datetime(2023, 6, 25)
end = datetime.datetime(2023, 9, 10)
RD().traffic.details(start, end).json()

'''
Streaming

'''

RD().streaming.transcode('example_id').json()

RD().streaming.media_info('example_id').json()

'''
Downloads

'''

RD().downloads.get(limit=10, page=2).json()

RD().downloads.delete('example_id')

'''
Torrents

'''

RD().torrents.get(limit=10, page=1).json()

RD().torrents.info('example_id').json()

RD().torrents.instant_availability('FE7E3784A298169D8DE3804B8FDE5EC318105194').json()

RD().torrents.active_count().json()

RD().torrents.available_hosts().json()

import os
filepath = os.getcwd() + '/bbb.torrent'

RD().torrents.add_file(filepath=filepath).json()

RD().torrents.add_magnet('FE7E3784A298169D8DE3804B8FDE5EC318105194').json()

RD().torrents.select_files('example_id', 'all')

RD().torrents.delete('example_id')

'''
Hosts

'''

RD().hosts.get().json()

RD().hosts.status().json()

RD().hosts.regex().json()

RD().hosts.regex_folder().json()

RD().hosts.domains().json()

'''
Settings

'''

RD().settings.get().json()

RD().settings.update('streaming_language_preference', 'eng')

RD().settings.convert_points()

RD().settings.change_password()

import os
filepath = os.getcwd() + '/avatar.png'

RD().settings.avatar_file(filepath)

RD().settings.avatar_delete()
