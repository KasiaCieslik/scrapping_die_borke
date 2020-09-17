from src.utils.utils import parse_data
from bs4 import BeautifulSoup
import datetime

with open("scraped_raw.txt",'r') as f:
    data = BeautifulSoup(f, "html.parser")
output = {'lastupdate': datetime.datetime(2020, 9, 16, 22, 8, 21),
     'temp': 21.4,
     'wind': 9.5,
     'boen': 17.3,
     'niederschlag': 0.0,
     'feuchte': 74,
     'luftdruck': 1018.1}
def test_parse_data():
    assert (parse_data(data)==output)
    assert (parse_data(data)['temp']==21.4)
    assert (parse_data(data)['luftdruck']==1018.1)
 



