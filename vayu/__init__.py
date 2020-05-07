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

from .timeInteractiveScatterPlot import timeInteractiveScatterPlot
from .scatterPlot import scatterPlot
from .timePlot import timePlot
from .calendarPlot import calendarPlot
from .linearRelation import linearRelation
from .selectByDate import selectByDate
from .summaryPlot import summaryPlot
from .timeProp import timeProp
from .timeVariation import timeVariation
from .trendLevel import trendLevel
from .windRosePy import windRose
from .interpolPlot import interpolPlot
from .smoothTrend import smoothTrend
from .interactiveChoroplethPlot import interactiveChoroplethPlot
