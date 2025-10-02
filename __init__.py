from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qgis.gui import QgisInterface


def classFactory(iface: "QgisInterface"):
    from import_all.plugin import Plugin
    return Plugin(iface)
