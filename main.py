from fastapi import FastAPI
from api.v1.routes.entityroutes import Entitiesrouter
from api.v1.routes.tagroutes import Tagsrouter

app = FastAPI()

#app.include_router(tagsrouter)

app.include_router(Entitiesrouter, prefix="/entities", tags=["ENTITIES"])
app.include_router(Tagsrouter, prefix="/tags", tags=["TAGS"])
