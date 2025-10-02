from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qgis.gui import QgisInterface


def classFactory(iface: "QgisInterface"):  # noqa N802
    from reloadproject.plugin import Plugin

    return Plugin()
