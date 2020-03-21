import flask
from covid19viz.utils import helper as h, errors


def serve_stylesheet(stylesheet):
    """
    Server the custom stylesheet route for the dashboard. This is hack.
    :param stylesheet: str
    :return: file object
    """
    _css_directory = "{}/css".format(h.get_static_dir_path())
    _css_files = h.get_all_css_files()

    if stylesheet not in _css_files:
        raise errors.NotFound(
            'Stylesheet "{}" is not found'.format(
                stylesheet
            )
        )

    return flask.send_from_directory(_css_directory, stylesheet)


def server_image(img):
    """
    Serve images and icons to the app
    :param icon_image:
    :return:
    """
    _img_directory = "{}/img".format(h.get_static_dir_path())
    _img_files = h.get_all_images_icons()

    if img not in _img_files:
        raise errors.NotFound(
            'Image/Icon "{}" is not found'.format(
                img
            )
        )

    return flask.send_from_directory(_img_directory, img)
