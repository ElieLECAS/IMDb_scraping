# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import mysql.connector


class ImdbPipeline:
    def process_item(self, item, spider):
        return item


class ConvertirDureePipeline:
    def process_item(self, item, spider):
        if "duration" in item:
            item["duration"] = self.convertir_duree_en_minutes(item["duration"])
        return item
    
    def convertir_duree_en_minutes(self, duree):
        if not duree:
            return 0
     
        heures = 0
        minutes = 0
        if 'h' in duree:
            heures_minutes = duree.split("h")
            heures = int(heures_minutes[0].strip())
            if 'm' in heures_minutes[1]:
                minutes = int(heures_minutes[1].split("m")[0].strip())
        elif 'm' in duree:
            minutes = int(duree.split("m")[0].strip())
        duree_en_minutes = heures * 60 + minutes
        return duree_en_minutes

class ActorsPipeline:
    def process_item(self, item, spider):
        item["actors"] = self.keep_first_actors(item["actors"])
        return item
    
    def keep_first_actors(self, actors):
        return actors[:3] 
    
class SeasonsPipeline:
    def process_item(self, item, spider):
        if 'seasons' in item:
            item["seasons"] = self.set_one_season(item["seasons"])
        return item
    
    def set_one_season(self, seasons):
        if not seasons:
            return '1'
        else:
            return seasons
        
class YearPipeline:
    def process_item(self, item, spider):
        item["year"] = item["year"][:4] if item["year"] else None
        return item
    


class ConvertToIntPipeline:
    def process_item(self, item, spider):
        if "score" in item:
            item["score"] = float(item["score"])
        if "year" in item:
            item["year"] = int(item["year"])
        if "duration" in item:
            item["duration"] = int(item["duration"]) 
        if "episodes" in item:
            item["episodes"] = int(item["episodes"])
        if "seasons" in item:
            item["seasons"] = int(item["seasons"])
        if "score" in item:
            item["score"] = float(item["score"])
        return item



# class SaveMyMoviesPipeline:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = '',
#             database = 'movies'
#         )

#         self.cur = self.conn.cursor

#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS movies(
#             id int NOT NULL auto_increment,
#             title text,
#             score DECIMAL,
#             genre text,
#             year INTEGER,
#             public text,
#             duration INTEGER,
#             description text,
#             director text,
#             actors text,
#         )

# """
#         )

# class SaveMySeriesPipeline:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = '',
#             database = 'series'
#         )


