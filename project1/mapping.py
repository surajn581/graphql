
import graphene
from schema import weather
from data import read_data

class query(graphene.ObjectType):
    sun_time=graphene.Field(weather,lat=graphene.NonNull(graphene.Float), long = graphene.NonNull(graphene.Float))
    def resolve_sun_time(self,info,lat,long):
        return read_data(lat, long)