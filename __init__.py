from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qgis.gui import QgisInterface


def classFactory(iface: "QgisInterface"):  # noqa N802
    from import_all.plugin import Plugin

    return Plugin()
