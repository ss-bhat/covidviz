import os
from dash.dash import exceptions
from dash.dash import _format_tag
from dash.dash import __version__
from dash.dash import _app_entry
from dash.dash import _re_index_entry_id
from dash.dash import _re_index_config_id
from dash.dash import _re_index_scripts_id
from dash.dash import _re_renderer_scripts_id
import dash


def custom_index(self, *args, **kwargs):  # pylint: disable=unused-argument
    scripts = self._generate_scripts_html()
    css = self._generate_css_dist_html()
    config = self._generate_config_html()
    metas = self._generate_meta_html()
    renderer = self._generate_renderer()
    title = getattr(self, "title", "Dash")

    # Hack to add meta tag
    metas += """
    <meta name="viewport" content="width=device-width, initial-scale=1">
    """

    if self._favicon:
        favicon_mod_time = os.path.getmtime(
            os.path.join(self.config.assets_folder, self._favicon)
        )
        favicon_url = self.get_asset_url(self._favicon) + "?m={}".format(
            favicon_mod_time
        )
    else:
        favicon_url = "{}_favicon.ico?v={}".format(
            self.config.requests_pathname_prefix, __version__
        )

    favicon = _format_tag(
        "link",
        {"rel": "icon", "type": "image/x-icon", "href": favicon_url},
        opened=True,
    )

    index = self.interpolate_index(
        metas=metas,
        title=title,
        css=css,
        config=config,
        scripts=scripts,
        app_entry=_app_entry,
        favicon=favicon,
        renderer=renderer,
    )

    checks = (
        (_re_index_entry_id.search(index), "#react-entry-point"),
        (_re_index_config_id.search(index), "#_dash-configs"),
        (_re_index_scripts_id.search(index), "dash-renderer"),
        (_re_renderer_scripts_id.search(index), "new DashRenderer"),
    )
    missing = [missing for check, missing in checks if not check]

    if missing:
        plural = "s" if len(missing) > 1 else ""
        raise exceptions.InvalidIndexException(
            "Missing element{pl} {ids} in index.".format(
                ids=", ".join(missing), pl=plural
            )
        )

    return index


dash.Dash.index = custom_index
