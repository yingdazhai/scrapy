# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class FifaItemPipeline:
    def __init__(self, file_name):
        # Storing output filename
        self.file_name = file_name
        # Creating a file handle and setting it to None
        self.file_handle = None
        
        
    # `settings.py` could be accessed by `from_crawler`.    
    @classmethod
    def from_crawler(cls, crawler):
        # getting the value of FILE_NAME field from settings.py
        output_filename = crawler.settings.get('FILE_NAME')
        # cls() calls FifaItemPipeline's constructor
        # Returning a FifaItemPipeline object
        return cls(output_filename)
    
    def open_spider(self, spider):
        print('CSV Exporter opened:')
    
        file = open(self.file_name, 'wb')
        self.file_handle = file
    
        self.exporter = CsvItemExporter(file)
        
        # CsvItemExporter respects both the list and the order of the list when writing files
        self.exporter.fields_to_export = ['name',
                                          'country',
                                          'position',
                                          'age',
                                          'overall_rating',
                                          'potential','club',
                                          'value',
                                          'wage',
                                          'total_stats'
                                          ,'hits'
                                         ]
        
        # Initiating export
        self.exporter.start_exporting()
        
    def close_spider(self, spider):
        print('CSV Exporter closed.')
        
        # Ending the export to file from CsvItemExporter object
        self.exporter.finish_exporting()
        # Closing the opened output file
        self.file_handle.close()

    def process_item(self, item, spider):
        # passing the item to CsvItemExporter object for expoting to file
        self.exporter.export_item(item)
        return item
