import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from mapping import query
from starlette.applications import Starlette

app = Starlette()
schema = graphene.Schema(query=query)
app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))
print(schema)