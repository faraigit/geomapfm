"""Main module for the geomapfm package."""
import ipyleaflet
import os
from ipyleaflet import FullScreenControl, LayersControl, DrawControl, MeasureControl, ScaleControl, TileLayer
from ipyleaflet.leaflet import Layer
class Map(ipyleaflet.Map):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)