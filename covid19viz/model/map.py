import folium
import dash_core_components as dcc
import dash_html_components as html
from covid19viz.utils import helper as h
from covid19viz.toolkit import covid_data
import json
import logging

log = logging.getLogger(__name__)

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


def get_map1():
    """
    Get leaflet map
    :return: map object
    """
    _static_dir = h.get_static_dir_path()
    m = folium.Map([53.350140, -6.266155], zoom_start=2)
    _geojson_file = "{}/clean_countries.geojson".format(_static_dir)

    with open(_geojson_file, 'r') as f:
        geojson = json.load(f)
        f.close()

    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.GeoJson(
        geojson,
        style_function=lambda x: {
            'fillColor': '#18607e',
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7
        },
        highlight_function=lambda x: {
            'fillOpacity': 1
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['id'],
            aliases=['Country:'],
        )
    ).add_to(m)
    m.save("{}/geojson.html".format(_static_dir))

    element = html.Iframe(
                    id='map-iframe',
                    srcDoc=open("{}/geojson.html".format(_static_dir), 'r').read(),
                    width='100%', height='700'
                )

    return element


def get_map():
    _static_dir = h.get_static_dir_path()
    _geojson_file = "{}/data/clean_countries.geojson".format(_static_dir)
    _token = "pk.eyJ1Ijoic3dhcm9vcGJoYXQxMjMiLCJhIjoiY2s4MmZleHZiMDUyMzNlcWtudWJxNHQ4byJ9.q_M3yDIf3UCUXD8jk8nelw"
    with open(_geojson_file, 'r') as f:
        geojson = json.load(f)
        f.close()

    layer = dict(
        type="fill",
        below='traces',
        color="#18607e",
        opacity=0.7,
        hovermode="closest",
        interactive=True,
        text=[x['properties']['id'] for x in geojson['features']],
        source=geojson,
        sourcetype="geojson"

    )

    element = dcc.Graph(
                id='TxWCD-choropleth',
                figure=dict(
                    data=[dict(
                        type='scattermapbox'
                    )],
                    layout=dict(
                            plot_bgcolor="#18607e",
                            paper_bgcolor="#18607e",
                            clickmode="event+select",
                            mapbox=dict(
                                layers=[layer],
                                accesstoken=_token,
                                center=dict(
                                    lat=53.350140,
                                    lon=-6.266155
                                ),
                                zoom=1,
                                style='light'
                            ),
                            height=600,
                            autosize=True,
                            margin=dict(
                                l=0,
                                r=0,
                                b=0,
                                t=0,
                                pad=4
                            )
                    )
                )
            )

    return element


def get_polygons_geojson():
    """

    :return:
    """
    _countries = covid_data.show_available_countries()
    _countries = [x.lower() for x in _countries]
    _static_dir = h.get_static_dir_path()
    _countries_geojson_file = "{}/data/countries.geojson".format(_static_dir)

    required_geojson = {"type": "FeatureCollection", "features":[]}
    features = required_geojson['features']
    found_countries = []
    _id = 1
    with open(_countries_geojson_file, 'r') as f:
        geojson = json.load(f)['features']
        for item in geojson:
            _ctr = item['properties']['ADMIN'].lower()
            _ctr = country_mapping.get(_ctr, _ctr)
            if _ctr in _countries:
                item['properties']['ADMIN'] = _ctr
                item['properties']['id'] = _ctr
                item['id'] = _id
                _id += 1
                features.append(item)
                found_countries.append(_ctr)
        f.close()
    del geojson
    print("TOTAL AVAILABLE COUNTRIES: {}".format(str(len(_countries))))
    print("TOTAL FOUND: {}".format(str(len(found_countries))))
    print("NOT FOUND: {}".format(str(len(_countries)-len(found_countries))))
    print(set(_countries).difference(set(found_countries)))

    with open("{}/data/clean_countries.geojson".format(_static_dir), 'w') as f:
        json.dump(required_geojson, f)
        f.close()

