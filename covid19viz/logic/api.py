from covid19viz.utils import errors
from covid19viz.toolkit import covid_data
from covid19viz.toolkit import config
import logging

log = logging.getLogger(__name__)


def get_stats(context, data_dict):
    """
    Get current stats of covid-19 outbreak
    :return: dict
    """
    return covid_data.get_stats()


def get_all_records_by_country(context, data_dict):
    """
    Get all the records for all the countries available
    :return: dict
    """
    return covid_data.get_all_records_by_country()


def get_all_records_by_provinces(context, data_dict):
    """
    Get all the records for all the available province
    :return: dict
    """
    return covid_data.get_history_by_province()


def filter_by_country(context, data_dict):
    """
    Get records for the country
    :return: dict
    """
    if "country" not in data_dict:
        raise errors.APIParameterError("Missing country parameter")

    return covid_data.filter_by_country(data_dict.get('country'))


def filter_by_province(context, data_dict):
    """
    Get records for the province
    :return: dict
    """
    if "province" not in data_dict:
        raise errors.APIParameterError("Missing country parameter")

    return covid_data.filter_by_country(data_dict.get('province'))


def show_available_countries(context, data_dict):
    """
    Show all the available countries
    :return: dict
    """
    return covid_data.show_available_countries()


def show_available_regions(context, data_dict):
    """
    Show all the available province
    :return: dict
    """
    return covid_data.show_available_regions()


def get_history_by_country(context, data_dict):
    """
    Get all history records for the country
    :return: dict
    """
    if "country" not in data_dict:
        raise errors.APIParameterError("Missing country parameter")

    return covid_data.get_history_by_country(data_dict.get('country'))


def get_history_by_province(context, data_dict):
    """
    Get all history records for the province
    :return: dict
    """
    if "province" not in data_dict:
        raise errors.APIParameterError("Missing country parameter")

    return covid_data.get_history_by_province(data_dict.get('province'))


def get_dash_ui_config(context, data_dict):
    """
    Get dash UI config from the predefined config
    :return:
    """
    ui_config = dict()
    for key in config:
        if "dash.ui" in key:
            ui_config[key] = config.get(key)
    return ui_config

