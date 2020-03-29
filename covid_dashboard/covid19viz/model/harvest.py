import requests
import logging

log = logging.getLogger(__name__)


def get_regional_data_ireland():
    """
    Specific to Ireland data
    :return: dict
    """
    _url = 'https://services1.arcgis.com/eNO7HHeQ3rUcBllm/arcgis/rest/services/' \
           'CovidCountyStatisticsHPSCIreland/FeatureServer/0/query?f=json&where=(CovidCases%20%3E%200)&' \
           'returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&' \
           'resultOffset=0&resultRecordCount=250'
    response = requests.get(_url)
    if response.status_code == 200:
        data = response.json()['features']
        res = []
        log.info("Gathering regional data for ireland")
        for _item in data:
            feature = dict()
            feature['label'] = _item['attributes']['CountyName']
            feature['confirmed'] = _item['attributes']['CovidCases']
            feature['deaths'] = "NA"
            feature['recovered'] = "NA"
            feature['lat'] = _item['attributes']['Lat']
            feature['long'] = _item['attributes']['Long']
            feature['last_updated'] = "NA (latest)"
            res.append(feature)
        return res
    else:
        return
