import dash_core_components as dcc
from covid19viz.model import stats
import logging

log = logging.getLogger(__name__)


def update_top_10_country_history(action):
    """
    Call back for radio buttons. Which updates the top n countries
    history confirmed or recovered or death
    :param action:
    :return: dash graph object
    """
    logging.info("Callback function executing for top n country history")

    return dcc.Graph(
        id="history-cases-country",
        figure=stats.top_n_countries_cases_by_time(action),
        className="graph"
    )
