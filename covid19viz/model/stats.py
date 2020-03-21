from covid19viz.toolkit import covid_data
from collections import OrderedDict
from dateutil.parser import parse
from covid19viz.utils import helper as h
from functools import lru_cache
import logging

log = logging.getLogger(__name__)


def get_statistics():
    """
    Current covid id stats.
    :return: dict
    """
    stats = covid_data.get_stats()

    return stats


def top_10_countries_confirmed_cases():

    actions = OrderedDict([
        ("confirmed", "rgb(255, 204, 0, 1)"),
        ("recovered", "rgb(127, 255, 0, 1)"),
        ("deaths", "rgb(220, 53, 69, 1)"),
        ("label", "")
    ])
    extract_top = 10
    _data = h.get_all_records_by_country()
    sorted_data = sorted(_data, key=lambda k: k['confirmed'], reverse=True)[:extract_top]

    figure = dict()
    stats = dict()
    for x in sorted_data:
        for _a in actions:
            if _a in stats:
                stats[_a].append(x.get(_a))
            else:
                stats[_a] = [x.get(_a)]

    figure['data'] = []

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

    figure['layout'] = h.get_plot_layout(
        title='Top 10 Countries Effected',
        x_title="Country",
        y_title="Count"
    )

    return figure


def top_10_countries_confirmed_cases_by_time():
    """

    :return:
    """
    data = h.get_all_records_by_country()
    sorted_data = h.sort_data(data, "confirmed")
    countries = [x.get('label') for x in sorted_data]

    figure = dict()
    figure['data'] = []

    for ctry in countries:
        _history = h.get_history_by_country(ctry)
        x = []
        y = []
        for dt in _history:
            x.append(str(parse(dt).date()))
            y.append(_history[dt]['confirmed'])

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

    figure['layout'] = h.get_plot_layout(
        title='Top 10 Countries History',
        x_title="Date",
        y_title="Count"
    )

    return figure


@lru_cache(maxsize=3)
def top_10_percentage_change(action):

    _actions = OrderedDict([
        ("confirmed", "rgb(255, 204, 0, 0.8)"),
        ("recovered", "rgb(127, 255, 0, 0.8)"),
        ("deaths", "rgb(220, 53, 69, 0.8)"),
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
