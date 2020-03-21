import os
import glob
from covid19viz.utils import errors
from covid19viz.toolkit import covid_data
from functools import lru_cache
import logging

log = logging.getLogger(__name__)


def get_static_dir_path():
    """
    Get the static folder path
    :return:
    """
    _this_dir = os.path.dirname(os.path.realpath(__file__))
    static_dir = "{}/{}".format(os.path.dirname(_this_dir), "static")

    if not os.path.dirname(static_dir):
        raise errors.NotFound("Static directory not found")

    return static_dir


def get_all_css_files():
    """
    Get all the css files from the static folder.
    :return: list
    """
    _css_dir = "{}/css".format(get_static_dir_path())
    css_files = []
    _css_files = glob.glob("{}/*".format(_css_dir))

    for _f in _css_files:
        css_files.append(os.path.basename(_f))

    return css_files


def get_all_images_icons():
    """
    Get all the image files from the static folder.
    :return: list
    """
    _img_dir = "{}/img".format(get_static_dir_path())
    img_files = []
    _img_files = glob.glob("{}/*".format(_img_dir))

    for _f in _img_files:
        img_files.append(os.path.basename(_f))

    return img_files


@lru_cache(maxsize=1)
def get_all_records_by_country():
    """
    Get all records by country
    :return: dict
    """
    data = list(covid_data.get_all_records_by_country().values())
    return data


def sort_data(data, action):
    """
    Extract top 10 data
    :param action: str
    :param data: list
    :return: list
    """
    extract_top = 10
    return sorted(data, key=lambda k: k[action], reverse=True)[:extract_top]


@lru_cache(maxsize=10)
def get_history_by_country(country):
    """
    get history data for the country
    :param country: str
    :return: list
    """
    history = list(covid_data.get_history_by_country(country).values())[0]['history']
    return history


def get_plot_layout(title=None, x_title=None, y_title=None):
    """
    Get the plot layout given title, x axis and y axis
    :param title: str
    :param x_title: str
    :param y_title: str
    :return: dict
    """
    return dict(
        title=title,
        plot_bgcolor="#18607e",
        paper_bgcolor="#18607e",
        xaxis={
            'title': x_title
        },
        yaxis={
            'title': y_title
        },
        font=dict(
            color="#ffff"
        ),
        hovermode='closest'
    )
