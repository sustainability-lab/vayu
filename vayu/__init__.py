# # -*- coding: utf-8 -*-
# from pkg_resources import get_distribution, DistributionNotFound

# try:
#     # Change here if project is renamed and does not equal the package name
#     dist_name = "vayu"
#     __version__ = get_distribution(dist_name).version
# except DistributionNotFound:
#     __version__ = "unknown"
# finally:
#     del get_distribution, DistributionNotFound

from .timeProp import timeProp
from .timePlot import timePlot
from .windRosePy import windRose
from .trendLevel import trendLevel
from .summaryPlot import summaryPlot
from .scatterPlot import scatterPlot
from .smoothTrend import smoothTrend
from .selectByDate import selectByDate
from .calendarPlot import calendarPlot
from .interpolPlot import interpolPlot
from .timeVariation import timeVariation
from .linearRelation import linearRelation
from .interactiveChoroplethPlot import interactiveChoroplethPlot
from .timeInteractiveScatterPlot import timeInteractiveScatterPlot
