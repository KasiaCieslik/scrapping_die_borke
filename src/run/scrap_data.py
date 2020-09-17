import sys
import time
import logging
import argparse
from src.utils.utils import (extract_float_from_string,
                             download_weather_data,
                             parse_data,create_db,
                             insert_to_db_table,get_data)
ap = argparse.ArgumentParser()
ap.add_argument("-a","--db",required =True, help= "first operand")
ap.add_argument("-b","--scrap_cycle",required =True, help= "second operand")
args = vars(ap.parse_args())

create_db(args['db'])
url = 'https://www.surf-und-segelschule-mueggelsee.de/?Wetterdaten'

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.info('Start logging')
while True:
    try:
        get_data(url,'../../data/scrap_die_borke.db')
        logging.info('Scraping continues')
        time.sleep(int(args['scrap_cycle']))
    except Exception as e:
        logging.exception("File not accessible")
    




