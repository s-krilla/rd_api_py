#!/usr/bin/env python3

import os
import json
import logging
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class RD:
    rd_apitoken = os.getenv('RD_APITOKEN')
    base_url = 'https://api.real-debrid.com/rest/1.0'
    header = {'Authorization': "Bearer " + str(rd_apitoken)}   
    error_codes = json.load(open(os.path.join(Path(__file__).parent.absolute(), 'error_codes.json')))

    def __init__(self):
        self.check_token(self.rd_apitoken)
        self.system = self.System()
        self.user = self.User()
        self.unrestrict = self.Unrestrict()
        self.traffic = self.Traffic()
        self.streaming = self.Streaming()
        self.downloads = self.Downloads()
        self.torrents = self.Torrents()
        self.hosts = self.Hosts()
        self.settings = self.Settings()

    def get(self, path, **options):
        request = requests.get(self.base_url + path, headers=self.header, params=options)
        return self.handler(request, self.error_codes)

    def post(self, path, **payload):
        request = requests.post(self.base_url + path, headers=self.header, data=payload)
        return self.handler(request, self.error_codes)
    
    def put(self, path, filepath, **payload):
        file = open(filepath, 'rb')
        request = requests.put(self.base_url + path, headers=self.header, data=file, params=payload)
        file.close()
        return self.handler(request, self.error_codes)

    def delete(self, path):
        request = requests.delete(self.base_url + path, headers=self.header)
        return self.handler(request, self.error_codes)
    
    def handler(self, request, error_codes):
        try:
            request.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            logging.error(errh)
        except requests.exceptions.ConnectionError as errc:
            logging.error(errc)
        except requests.exceptions.Timeout as errt:
            logging.error(errt)
        except requests.exceptions.RequestException as err:
            logging.error(err)
        try:
            if 'error_code' in request.json():
                code = request.json()['error_code']
                logging.warning(code + ': ' + error_codes[code])
        except:
            pass
        return request
    
    def check_token(self, token):
        if token is None or token == 'your_token_here':
            logging.warning('Add token to .env')

    class System:
        def __init__(self):
            pass

        def disable_token(self):
            return RD().get('/disable_access_token')

        def time(self):
            return RD().get('/time')

        def iso_time(self):
            return RD().get('/time/iso')

    class User:
        def __init__(self):
            pass 

        def get(self):
            return RD().get('/user')

    class Unrestrict:
        def __init__(self):
            pass  

        def check(self, link, password=None):
            return RD().post('/unrestrict/check', link=link, password=password)

        def link(self, link, password=None, remote=None):
            return RD().post('/unrestrict/link', link=link, password=password, remote=remote)
        
        def folder(self, link):
            return RD().post('/unrestrict/folder', link=link)
        
        def container_file(self, filepath):
            return RD().put('/unrestrict/containerFile', filepath=filepath)

        def container_link(self, link):
            return RD().post('/unrestrict/containerLink', link=link)
        
    class Traffic:
        def __init__(self):
            pass  

        def get(self):
            return RD().get('/traffic')

        def details(self, start=None, end=None):
            return RD().get('/traffic/details', start=start, end=end)        
        
    class Streaming:
        def __init__(self):
            pass

        def transcode(self, id):
            return RD().get('/streaming/transcode/' + str(id))

        def media_info(self, id):
            return RD().get('/streaming/mediaInfos/' + str(id))
        
    class Downloads:
        def __init__(self):
            pass

        def get(self, offset=None, page=None, limit=None ):
            return RD().get('/downloads', offset=offset, page=page, limit=limit)
        
        def delete(self, id):
            return RD().delete('/downloads/delete/'+ str(id))

    class Torrents:
        def __init__(self):
            pass

        def get(self, offset=None, page=None, limit=None, filter=None ):
            return RD().get('/torrents', offset=offset, page=page, limit=limit, filter=filter)
        
        def info(self, id):
            return RD().get('/torrents/info/' + str(id))

        def instant_availability(self, hash):
            return RD().get('/torrents/instantAvailability/' + str(hash))

        def active_count(self):
            return RD().get('/torrents/activeCount')
        
        def available_hosts(self):
            return RD().get('/torrents/availableHosts')

        def add_file(self, filepath, host=None):
            return RD().put('/torrents/addTorrent', filepath=filepath, host=host)
        
        def add_magnet(self, magnet, host=None):
            magnet_link = 'magnet:?xt=urn:btih:' + str(magnet)
            return RD().post('/torrents/addMagnet', magnet=magnet_link, host=host)
        
        def select_files(self, id, files):
            return RD().post('/torrents/selectFiles/' + str(id), files=str(files))
        
        def delete(self, id):
            return RD().delete('/torrents/delete/' + str(id))

    class Hosts:
        def __init__(self):
            pass

        def get(self):
            return RD().get('/hosts')        
        
        def status(self):
            return RD().get('/hosts/status')   

        def regex(self):
            return RD().get('/hosts/regex')  

        def regex_folder(self):
            return RD().get('/hosts/regexFolder')  

        def domains(self):
            return RD().get('/hosts/domains')  

    class Settings:
        def __init__(self):
            pass

        def get(self):
            return RD().get('/settings')
        
        def update(self, setting_name, setting_value):
            return RD().post('/settings/update', setting_name=setting_name, setting_value=setting_value)
        
        def convert_points(self):
            return RD().post('/settings/convertPoints')            

        def change_password(self):
            return RD().post('/settings/changePassword')      

        def avatar_file(self, filepath):
            return RD().put('/settings/avatarFile', filepath=filepath)
        
        def avatar_delete(self):
            return RD().delete('/settings/avatarDelete')
