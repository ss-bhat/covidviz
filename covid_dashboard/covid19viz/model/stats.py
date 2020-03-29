from collections import OrderedDict
from dateutil.parser import parse
from covid19viz.utils import helper as h
from covid19viz.toolkit import config
from covid19viz.model import covid_data
import logging

log = logging.getLogger(__name__)


def get_statistics():
    """
    Current covid-19 stats.
    :return: dict
    """
    log.info("Gathering total statistics")
    stats = covid_data.get_stats()
    return stats


def top_n_countries_confirmed_cases(value=10):
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
    log.info("Preparing data for top {} countries".format(value))
    _data = h.get_all_records_by_country()

    # Sort data on top confirmed cases
    sorted_data = h.sort_data(_data, "confirmed", value=value)

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
    log.info("Preparing bubble chart")
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
    log.info("Preparing historical data for action: {}".format(action))
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
        text = []
        for dt in _history:
            x.append(str(parse(dt).date()))
            y.append(_history[dt][action])
            text.append(
                "Country: {}<br>".format(ctry) +
                "State: {}<br>".format(action) + "Last Updated: {}".format(str(parse(dt).date()))
            )

        figure['data'].append(
            dict(
                x=x,
                y=y,
                text=text,
                name=ctry,
                opacity=2,
                mode="lines+markers",
                fill='tozeroy'
                )
            )

    # Layout
    figure['layout'] = h.get_plot_layout(
        title='Historical Data for - {}'.format(action.title()),
        x_title="Date",
        y_title="Count"
    )
    log.info("Rendering fig data")
    return figure


def get_stats_by_country(country=config.get('dash.default_country')):
    """
    Get historical statistics for the given country data
    :param country: str (default ireland)
    :return: dict
    """
    log.info("Getting statistics for the country: {}".format(country))
    _actions = OrderedDict([
        ("confirmed", config.get('dash.ui.confirmed_color')),
        ("recovered", config.get('dash.ui.recovered_color')),
        ("deaths", config.get('dash.ui.deaths_color'))
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
    log.info("Rendering fig data for a given country")
    return figure


def get_current_stats_for_country(country=config.get('dash.default_country')):
    """
    Gets current statistics for the country
    :param country: str
    :return: dict
    """
    log.info("Getting current stats for the country: {}".format(country))
    _actions = OrderedDict([
        ("confirmed", config.get('dash.ui.confirmed_color')),
        ("recovered", config.get('dash.ui.recovered_color')),
        ("deaths", config.get('dash.ui.deaths_color'))
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
            opacity=0.8,
            type="bar",
            marker=dict(
                color=list(_actions.values())
            )
        )
    )

    figure['layout'] = h.get_plot_layout(
        title='Data as of {}: {}'.format(h.get_last_updated_date(as_string=True), _data['label'].title()),
        x_title='Cases',
        y_title='Count'
    )
    log.info("getting plot data")
    return figure


def get_all_countries_options():
    """
    Get all the
    :return:
    """
    _countries = covid_data.show_available_countries()
    options = []
    for _ctr in _countries:
        options.append(
            {
                "label": _ctr, 'value': _ctr.lower()
            }
        )

    log.info("Gathering all options for the country..")
    return options
