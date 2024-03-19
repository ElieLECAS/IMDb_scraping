# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ImdbPipeline:
    def process_item(self, item, spider):
        return item


class ConvertirDureePipeline:
    def process_item(self, item, spider):
        if "duration" in item:
            item["duration"] = self.convertir_duree_en_minutes(item["duration"])
        return item
    
    def convertir_duree_en_minutes(self, duree):
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

