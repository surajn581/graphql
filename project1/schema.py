import graphene

class weather(graphene.ObjectType): 
    sunrise=graphene.String()
    sunset=graphene.String()
    timezone=graphene.String()