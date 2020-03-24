from covid19viz.toolkit import covid_data
from collections import OrderedDict
from dateutil.parser import parse
from covid19viz.utils import helper as h
from covid19viz.toolkit import config
from functools import lru_cache
import logging

log = logging.getLogger(__name__)


def get_statistics():
    """
    Current covid-19 stats.
    :return: dict
    """
    stats = covid_data.get_stats()

    return stats


def top_n_countries_confirmed_cases():
    """
    Get top n countries confirmed cases. Current data of confirmed, recovered and deaths
    :return: dict
    """

    # Set color code
    actions = OrderedDict([
        ("confirmed", config.get('dash.ui.confirmed_color')),
        ("recovered", config.get('dash.ui.recovered_color')),
        ("deaths", config.get('dash.ui.deaths_color')),
        ("label", "")
    ])

    _data = h.get_all_records_by_country()

    # Sort data on top confirmed cases
    sorted_data = h.sort_data(_data, "confirmed")

    figure = dict()
    stats = dict()

    # Prepare the sorted data
    for x in sorted_data:
        for _a in actions:
            if _a in stats:
                stats[_a].append(x.get(_a))
            else:
                stats[_a] = [x.get(_a)]

    figure['data'] = []

    # Create bubble chart and calculate bubble size
    for action in list(actions.keys())[:-1]:
        sizeref = 10. * max(stats[action]) / (100 ** 2)
        figure['data'].append(
            dict(
                x=stats.get('label'),
                y=stats.get(action),
                text=stats.get('label'),
                name=action.upper(),
                opacity=1,
                mode="markers",
                marker=dict(
                    color=actions.get(action),
                    sizemode="area",
                    sizeref=sizeref,
                    size=[x for x in stats.get(action)]
                )
            )
        )

    # Layout
    figure['layout'] = h.get_plot_layout(
        title='Top Countries Effected',
        x_title="Country",
        y_title="Count"
    )

    return figure


def top_n_countries_cases_by_time(action):
    """
    Get top n countries historical data till now
    :return: dict
    """

    data = h.get_all_records_by_country()
    sorted_data = h.sort_data(data, action)
    countries = [x.get('label') for x in sorted_data]

    figure = dict()
    figure['data'] = []

    # Get historical data for each country and prepare
    for ctry in countries:
        _history = h.get_history_by_country(ctry)
        x = []
        y = []
        for dt in _history:
            x.append(str(parse(dt).date()))
            y.append(_history[dt][action])

        figure['data'].append(
            dict(
                x=x,
                y=y,
                text=ctry,
                name=ctry,
                opacity=2,
                mode="lines+markers"
                )
            )

    # Layout
    figure['layout'] = h.get_plot_layout(
        title='Historical Data for - {}'.format(action.title()),
        x_title="Date",
        y_title="Count"
    )

    return figure


@lru_cache(maxsize=3)
def top_n_percentage_change(action):
    """
    Top n countries percentage change data.
    TODO: Currently this is not implemented takes time to load
    :param action: str
    :return: dict
    """
    # TODO: Take this from config
    _actions = OrderedDict([
        ("confirmed", config.get('dash.ui.confirmed_color')),
        ("recovered", config.get('dash.ui.recovered_color')),
        ("deaths", config.get('dash.ui.deaths_color')),
    ])

    _countries = covid_data.show_available_countries()
    change_dict = []
    figure = dict()
    figure['data'] = []

    for ctry in _countries:
        _history = h.get_history_by_country(ctry)
        _last_reading = list(_history.keys())[-1]
        change = _history[_last_reading]["change_{}".format(action)]
        if change != "na":
            change_dict.append(
                {
                    "label": ctry,
                    "key": _last_reading,
                    "value": float(change)
                }
            )

    sorted_data = h.sort_data(change_dict, "value")

    x = []
    y = []
    text = []
    for item in sorted_data:
        x.append(item['label'])
        y.append(item['value'])
        text.append("Country: {}<br>".format(item['label']) +
                    "State: {}<br>".format(action)+"time: {}".format(item['key']))

    figure['data'].append(
        dict(
            x=x,
            y=y,
            text=text,
            name="ads",
            opacity=0.6,
            type="bar",
            marker=dict(
                color=_actions.get(action)
            )
        )
    )

    figure['layout'] = h.get_plot_layout(
        title='Top 10 Change(Rate) - {}'.format(action),
        x_title='Country',
        y_title='Change'
    )

    return figure


def get_stats_by_country(country="ireland"):
    """
    Get historical statistics for the given country data
    :param country: str (default ireland)
    :return: dict
    """
    # TODO: Take this from config
    _actions = OrderedDict([
        ("confirmed", "rgb(255, 204, 0, 0.8)"),
        ("recovered", "rgb(127, 255, 0, 0.8)"),
        ("deaths", "rgb(220, 53, 69, 0.8)"),
    ])
    data = list(covid_data.get_history_by_country(country).values())[0]
    country_label = data['label']
    title = "Historical Data for - {}".format(country_label)
    figure = dict()
    figure['data'] = []

    for action in _actions:
        x = []
        y = []
        text = []
        for dt in data['history']:
            x.append(str(parse(dt).date()))
            y.append(data['history'][dt][action])
            text.append(
                "Country: {}<br>".format(country_label) +
                "State: {}<br>".format(action) + "Last Updated: {}".format(str(parse(dt).date()))
            )

        figure['data'].append(
            dict(
                x=x,
                y=y,
                text=text,
                name=action,
                opacity=0.8,
                mode="lines+markers",
                marker=dict(
                    color=_actions.get(action)
                )
            )
        )

    figure['layout'] = h.get_plot_layout(
        title=title,
        x_title="Date",
        y_title="Count"
    )
    return figure


def get_current_stats_for_country(country="ireland"):
    """
    Gets current statistics for the country
    :param country: str
    :return: dict
    """
    _actions = OrderedDict([
        ("confirmed", "rgb(255, 204, 0, 0.8)"),
        ("recovered", "rgb(127, 255, 0, 0.8)"),
        ("deaths", "rgb(220, 53, 69, 0.8)"),
    ])

    _data = list(covid_data.get_history_by_country(country).values())[0]
    _history = _data['history']
    _key = list(_history.keys())[-1]
    current_data = _history[_key]
    figure = dict()
    figure['data'] = []

    x = []
    y = []
    text = []

    for action in _actions:
        x.append(action.title())
        y.append(current_data.get(action))
        text.append(
            "Country: {}<br>".format(_data['label']) +
            "State: {}<br>".format(action) + "Last Updated: {}".format(str(parse(_key).date()))
        )

    figure['data'].append(
        dict(
            x=x,
            y=y,
            text=text,
            name="ads",
            opacity=0.6,
            type="bar",
            marker=dict(
                color=list(_actions.values())
            )
        )
    )

    figure['layout'] = h.get_plot_layout(
        title='Current Data for the Country: {}'.format(_data['label'].title()),
        x_title='Cases',
        y_title='Count'
    )

    return figure
