from requests import get
import requests

#This is a Python LIB for fn-api.com  , Developers Caser - command :D
# The LIB Made by : LKST1 #

""" #Supported Langs
->
-> ar 
-> de 
-> en
-> es  
-> es-419  
-> fr  
-> it  
-> ja  
-> ko  
-> pl  
-> pt-BR  
-> ru  
-> tr
"""

class FNapi() :
    def allcosmetics(self,lang="en") :
        cosmetics_url = "https://fn-api.com/api/cosmetics?lang={}".format(lang)
        cosmetics = get(cosmetics_url).json()
        return cosmetics
    ######################
    def cosmeticD(self,cosmeticId,lang="en") :
        cosmetics_urlD = f"https://fn-api.com/api/cosmetics/{cosmeticId}?lang={lang}"
        cosmeticsD = get(cosmetics_urlD).json()
        return cosmeticsD
    ######################
    def Blogposts(self,lang="en") :
        Blogposts_url = "https://fn-api.com/api/blogposts?lang={}".format(lang)
        Blogposts = get(Blogposts_url).json()
        return Blogposts
    
    
    ######################
    def calendar(self) :
        calender_url = "https://fn-api.com/api/calendar"
        calendar = get(calender_url).json()
        return calendar
    
    ######################
    def status(self) :
        Fnstatus_url = "https://fn-api.com/api/status"
        FNStatus = get(Fnstatus_url).json()
        return FNStatus
    
    ######################
    
    def staging(self) :
        Staging_url = "https://fn-api.com/api/servers"
        Staging = get(Staging_url).json()
        return Staging
    
    ######################
    
    def trello(self) :
        trello_url = "https://fn-api.com/api/trello"
        trello = get(trello_url).json()
        return trello
    
    ######################

    
    def cloudStorage(self) :
        CloudStorage_url = "https://fn-api.com/api/cloudstorage"
        CloudStorage = get(CloudStorage_url).json()
        return CloudStorage
    
    ######################
    
    
    def cloudstorefile(self,fileName) :
        CloudStoreFile_url = f"https://fn-api.com/api/cloudstorage/{fileName}"
        CloudStoreFile = get(CloudStoreFile_url).json()
        return CloudStoreFile
    
    ######################
    
    
    def radios(self,lang="en") :
        Radios_url = f"https://fn-api.com/api/radios?lang={lang}"
        Radios = get(Radios_url).json()
        return Radios
    
    ######################
 
    def Emergency(self,lang="en") :
        Emergency_url = f"https://fn-api.com/api/emergencyNotices?lang={lang}"
        Emergency = get(Emergency_url).json()
        return Emergency
    
    ######################

    def backgrounds(self) :
        backgrounds_url = "https://fn-api.com/api/backgrounds"
        backgrounds = get(backgrounds_url).json()
        return backgrounds
    
    ######################

    def news(self,lang="en") :
        news_url = f"https://fn-api.com/api/news?lang={lang}"
        news = get(news_url).json()
        return news
    
    ######################

    def news_type(self,game_mode,lang="en") :
        newtype_url = f"https://fn-api.com/api/news/{game_mode}?lang={lang}"
        newtype = get(newtype_url).json()
        return newtype
    
    ######################

    def playlists(self,lang="en") :
        playlists_url = f"https://fn-api.com/api/playlists?lang={lang}"
        playlists = get(playlists_url).json()
        return playlists
    ######################

    
    def active_playlists(self,lang="en") :
        activeplaylists_url = f"https://fn-api.com/api/playlists/active?lang={lang}"
        activeplaylists = get(activeplaylists_url).json()
        return activeplaylists
    ######################

    
    def playlist_search(self,playlistid) :
        playlist_search_url = f"https://fn-api.com/api/playlists/{playlistid}"
        playlist_search = get(playlist_search_url).json()
        return playlist_search

    ######################
    def shop_sections(self,auth=None,lang="en",hideCosmetics=True) :
        shopsections_url = f"https://fn-api.com/api/shop/br/sections?lang={lang}?hideCosmetics={hideCosmetics}"
        head = {
          'Authorization': f'{auth}'
        }
        shopsections = requests.get(shopsections_url, headers=head).json()
        return shopsections
    ######################

    
    def stores(self,lang="en") :
        stores_url = f"https://fn-api.com/api/stores?lang={lang}"
        stores = get(stores_url).json()
        return stores
    ######################

    
    def store_select(self,storename) :
        stores_select_url = f"https://fn-api.com/api/stores/{storename}"
        stores_select = get(stores_select_url).json()
        return stores_select
    ######################

    
    def stream(self,stream_id,lang="en") :
        stream_id_url = f"https://fn-api.com/api/streams/{stream_id}?lang={lang}"
        stream_by_id = get(stream_id_url).json()
        return stream_by_id
    ######################

    
    def aes(self) :
        aes_url = f"https://fn-api.com/api/aes"
        aes = get(aes_url).json()
        return aes
    ######################

    
    def map(self,lang="en") :
        map_url = f"https://fn-api.com/api/map?lang={lang}"
        map = get(map_url).json()
        return map
    ######################

    
    def rarities(self,lang="en") :
        rarities_url = f"https://fn-api.com/api/rarity?lang={lang}"
        rarities = get(rarities_url).json()
        return rarities
    ######################

    
    def sections_list(self,auth=None,lang="en",hideCosmetics=True) :
        shopsectionsList_url = f"https://fn-api.com/api/shop/br/sections?lang={lang}?hideCosmetics={hideCosmetics}"
        head = {
          'Authorization': f'{auth}'
        }
        sectionsListdata = requests.get(shopsectionsList_url, headers=head).json()
        return sectionsListdata
    ###################### Premium


    ###### PRIMUIM
    def weapons(self,auth,lang="en") :
        weapons_url = f"https://fn-api.com/api/weapons?lang={lang}"
        head = {
          'Authorization': f'{auth}'
        }
        weapons = requests.get(weapons_url, headers=head).json()
        return weapons
    #######################
    def npcs(self,auth,lang="en"):
        
        Npcs_url = f"https://fn-api.com/api/npcs?lang={lang}"
        header = {
          'Authorization': f'{auth}'
        }
        npcs = requests.get(Npcs_url, headers=header).json()
        return npcs
    #######################
    def npcsD(self,auth,npcId,lang="en",):
        
        NpcD_url = f"https://fn-api.com/api/npcs/{npcId}?lang={lang}"
        header = {
          'Authorization': f'{auth}'
        }
        npcsD = requests.get(NpcD_url, headers=header).json()
        return npcsD
    ######################
    def stwshop(self,auth,lang="en") :
        stwshop_url = f"https://fn-api.com/api/shop/stw?lang={lang}"
        header = {
          'Authorization': f'{auth}'
        }
        stD = requests.get(stwshop_url,headers=header).json()
        return stD
    #####################
    def stwdaily(self,auth,lang="en") :
        stwdailyurl = f" https://fn-api.com/api/stw/dailyRewards?lang={lang}"
        header = {
          'Authorization': f'{auth}'
        }
        stDaily = requests.get(stwdailyurl,headers=header).json()
        return stDaily
    #####################
    def stw_user_stats(self,auth,lang="en",name=None,id=None) :
        if name is not None :
            name = name
            stwPlayerstats_url = f"https://fn-api.com/api/stw/stats?lang={lang}?name={name}"
        elif id is not None :
            id = id
            stwPlayerstats_url = f"https://fn-api.com/api/stw/stats?lang={lang}?id={id}"
        else:
            name = "SypherPK"
            stwPlayerstats_url = f"https://fn-api.com/api/stw/stats?lang={lang}?name={name}"
        header = {
          'Authorization': f'{auth}'
        }
        STWplayerstats = requests.get(stwPlayerstats_url,headers=header).json()
        return STWplayerstats
    ############################
    def weaponsD(self,auth,weaponId,lang="en") :
        weaponsD_url = f"https://fn-api.com/api/weapons/{weaponId}lang={lang}"
        header = {
          'Authorization': f'{auth}'
        }
        weaponsD = requests.get(weaponsD_url, headers=header).json()
        return weaponsD
    ################