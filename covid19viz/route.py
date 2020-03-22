from dateutil.parser import parse
from covid19viz.utils import helper as h, errors
import json
import logging

log = logging.getLogger(__name__)


def get_locations_for_all_country():
    """
    Server geojson file
    :return: json
    """
    _data = h.get_all_records_by_country()
    geojson_data = dict(
        type='FeatureCollection',
        features=[]
    )

    for _item in _data:
        try:
            _dt = dict(
                type="Feature",
                geometry=dict(
                    type="Point",
                    coordinates=[float(_item['long']), float(_item['lat'])]
                ),
                properties=dict(
                    country=_item['label'],
                    last_updated=str(parse(_item['last_updated']).date()),
                    confirmed=_item['confirmed'],
                    deaths=_item['deaths'],
                    recovered=_item['recovered']
                )
            )
            geojson_data['features'].append(_dt)
        except Exception as e:
            log.error(e)
            pass

    return json.dumps(geojson_data)


def get_locations_for_all_state():
    """
    Server geojson file
    :return: json
    """

    _data = h.get_all_records_by_country()
    print(_data)


def show_stats_country():
    """
    Server geojson file
    :return: json
    """

    pass


def show_stats_state():
    """
    Server geojson file
    :return: json
    """

    pass


