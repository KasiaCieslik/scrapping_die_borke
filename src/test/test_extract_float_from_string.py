from src.utils.utils import extract_float_from_string


data = ['Letzte Aktualisierung: 16.09.2020 21:20:21', 'Sonnenuntergang: 19:18', 'Temperatur: 22.6 °C', 'Wind / Böen: 8.7 / 11.3 kn => NW', 'Niederschlag: 0.0 mm', 'Feuchte: 66 %', 'Luftdruck: 1017.3 hPa', 'Vorhersage: Meist heiter und wärmer.'] 

def test_extract_float_from_string():
    assert (extract_float_from_string(data[2])==22.6)
    assert (extract_float_from_string(data[3])==[8.7, 11.3])
    assert (extract_float_from_string(data[4])==0.0)
    assert (extract_float_from_string(data[6])==1017.3)
    assert (type(extract_float_from_string(data[6]))==float)
    assert (type(extract_float_from_string(data[3]))==list)



