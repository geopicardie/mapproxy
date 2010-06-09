# This file is part of the MapProxy project.
# Copyright (C) 2010 Omniscale <http://omniscale.de>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from mapproxy.core.source import Source, InfoSource
from mapproxy.core.cache import MapExtend, TileSourceError
from mapproxy.core.srs import SRS
from mapproxy.core.client import HTTPClientError
from mapproxy.core.utils import reraise_exception

class WMSSource(Source):
    supports_meta_tiles = True
    def __init__(self, client):
        Source.__init__(self)
        self.client = client
        #TODO extend
        self.extend = MapExtend((-180, -90, 180, 90), SRS(4326))
    
    def get_map(self, query):
        try:
            return self.client.get_map(query)
        except HTTPClientError, e:
            reraise_exception(TileSourceError(e.args[0]), sys.exc_info())
        

class WMSInfoSource(InfoSource):
    def __init__(self, client):
        self.client = client
    def get_info(self, query):
        return self.client.get_info(query).read()
