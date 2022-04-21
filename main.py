#!/bin/python3

from time import sleep
from requests import get
from datetime import datetime
from json import loads
from os import makedirs

def id_pair_json_link() -> str:
    return "https://www.dmi.dk/NinJo2DmiDk/ninjo2dmidk?cmd=slj"

def station_data_json_link(id: str) -> str:
    return f"https://www.dmi.dk/NinJo2DmiDk/ninjo2dmidk?cmd=obj&wmo={id}"

def fetch_id_pair_data() -> list:
    response = get(id_pair_json_link())
    # TODO check response for non-ok
    data = loads(response.text)
    # TODO sanitize/parse
    return data

def find_station_id(id_pair_data: list, name: str) -> str:
    for i in id_pair_data:
        if i['name'].lower() == name.lower():
            return i['id']
    assert False, 'should not reach'

def fetch_station_data_json(station_id: str) -> str:
    response = get(station_data_json_link(station_id))
    if not response.ok:
        return ''
    # TODO check response for non-ok
    return response.text

def make_filename_friendly(value: str) -> str:
    return value.replace('/', '_').replace('. ', '_').replace(' ', '_')

def make_dated_filename(prefix: str) -> str:
    d = datetime.now()
    filename = f'{prefix}-{d.year}-{d.month}-{d.day}-{d.hour}-{d.minute}-{d.second}.json'
    return filename

def main():
    makedirs('data', exist_ok=True)
    while True:
        id_pair_data = fetch_id_pair_data()
        station_name = "Flyvestation Karup".lower()
        station_id = find_station_id(id_pair_data, station_name)
        station_data_json = fetch_station_data_json(station_id);
        filename = make_dated_filename(make_filename_friendly(station_name))
        with open(f"./data/{filename}", 'w') as file:
            file.write(station_data_json)
        sleep(60 * 60 * 24)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    