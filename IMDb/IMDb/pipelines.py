# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

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
            return None
     
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
        
class CleanAmountPipeline:
    def process_item(self, item, spider):
        if "budget" in item:
            budget = item['budget']
            if budget is not None:
                clean_budget = ''.join(char for char in budget if char.isdigit())
                item['budget'] = int(clean_budget)
        
        return item


    
class ConvertToIntPipeline:
    def process_item(self, item, spider):
        item["year"] = item["year"][:4]
        # item["seasons"] = item["seasons"][:1] if item["seasons"] else None

        item["score"] = float(item["score"])
        item["year"] = int(item["year"])

        if "episodes" in item:
            item["episodes"] = int(item["episodes"])
        if "seasons" in item:
            item["seasons"] = item["seasons"][:1]
            item["seasons"] = int(item["seasons"])
        return item

class ActorsSplitPipeline:
    def process_item(self, item, spider):
        if "actors" in item:
            item["actors"] = ', '.join(item["actors"][:3])
        return item


class SaveAllPipelines:
    def __init__(self):
        self.conn = sqlite3.connect('imdb_bdd.db')
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            score DECIMAL,
            genre TEXT,
            year INTEGER,
            public TEXT,
            duration INTEGER,
            description TEXT,
            creator TEXT,
            actors TEXT,
            country TEXT,
            budget INTEGER
        )
        """)
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS series(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            score DECIMAL,
            genre TEXT,
            year INTEGER,
            public TEXT,
            duration INTEGER,
            episodes INTEGER,
            seasons INTEGER,
            description TEXT,
            creator TEXT,
            actors TEXT,
            country TEXT
        )
        """)
        
        self.conn.commit()

    def process_item(self, item, spider):
        if 'episodes' in item and 'seasons' in item:
            table_name = 'series'
        else:
            table_name = 'movies'

        columns = ', '.join(item.keys())
        placeholders = ', '.join('?' * len(item))
        values = tuple(item.values())

        self.cur.execute(f"""
        INSERT INTO {table_name} ({columns}) 
        VALUES ({placeholders})
        """, values)

        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
    
