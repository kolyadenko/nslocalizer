from .PBXItem import *

class PBXAggregateTarget(PBX_Base_Target):
    def __init__(self, identifier, dictionary):
        super(self.__class__, self).__init__(identifier, dictionary)