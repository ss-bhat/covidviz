from covid19viz.utils import helper as h
from dateutil.parser import parse
from covid import CovId19Data
from covid19viz.model import harvest
import json
import logging

log = logging.getLogger(__name__)

_harvest_regional_mapping = {
    "ireland": harvest.get_regional_data_ireland
}

country_mapping = {
    "south korea": 'korea, south',
    "north korea": 'korea, north',
    'united republic of tanzania': 'tanzania',
    'the bahamas': 'bahamas, the',
    'cape verde': 'cabo verde',
    'united states of america': 'us',
    'republic of serbia': 'serbia',
    'taiwan': 'taiwan*',
    'gambia': 'gambia, the'


}



def get_polygons_geojson():
    """

    :return:
    """
    covid_data = CovId19Data(force=False)
    _countries = covid_data.show_available_countries()
    _countries = [x.lower() for x in _countries]
    _static_dir = h.get_static_dir_path()
    _countries_geojson_file = "{}/data/countries.geojson".format(_static_dir)

    required_polygon_geojson = {"type": "FeatureCollection", "features":[]}
    features = required_polygon_geojson['features']
    found_countries = []
    _id = 1
    with open(_countries_geojson_file, 'r') as f:
        geojson = json.load(f)['features']
        for item in geojson:
            _ctr = item['properties']['ADMIN'].lower()
            _ctr = country_mapping.get(_ctr, _ctr)

            if _ctr in _countries:
                _data = covid_data.filter_by_country(_ctr)
                item['properties']['ADMIN'] = _ctr
                item['properties']['id'] = _ctr
                item['id'] = _id

                item['properties']['html'] = """
                    <strong>Country:</strong> {label}<br>
                    <strong>Confirmed:</strong> {confirmed}<br>
                    <strong>Recovered:</strong> {recovered}<br>
                    <strong>Deaths:</strong> {deaths}<br>
                    <strong>Last Updated:</strong> {last_updated}
                """.format(
                    label=_data.get('label', 'NA'),
                    confirmed=_data.get('confirmed', 'NA'),
                    recovered=_data.get('recovered', 'NA'),
                    deaths=_data.get('deaths', 'NA'),
                    last_updated=str(parse(_data['last_updated']).date()),
                )

                _id += 1
                features.append(item)
                found_countries.append(_ctr)
        f.close()
    del geojson
    print("TOTAL AVAILABLE COUNTRIES: {}".format(str(len(_countries))))
    print("TOTAL FOUND: {}".format(str(len(found_countries))))
    print("NOT FOUND: {}".format(str(len(_countries)-len(found_countries))))
    #print(set(_countries).difference(set(found_countries)))

    print("Gathering data for regions/province")

    _provinces = covid_data.show_available_regions()
    required_marker_geojson = {"type": "FeatureCollection", "features": []}
    m_features = required_marker_geojson['features']

    for province in _provinces:
        province_data = covid_data.filter_by_province(province)
        feature = h.prepare_feature(province_data)
        m_features.append(feature)

    for _harvest in _harvest_regional_mapping:
        _provinces = _harvest_regional_mapping[_harvest]()
        for province_data in _provinces:
            feature = h.prepare_feature(province_data)
            m_features.append(feature)

    with open("{}/data/polygon.geojson".format(_static_dir), 'w') as f:
        json.dump({
            "polygon_layer": required_polygon_geojson,
            "marker_layer": required_marker_geojson
        }, f)
        f.close()
