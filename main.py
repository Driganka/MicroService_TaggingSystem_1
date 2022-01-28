from fastapi import FastAPI
from api.v1.microservices.microservices import Microservicesrouter
from api.v1.entities.entities import Entitiesrouter

app = FastAPI()

#app.include_router(tagsrouter)

app.include_router(Entitiesrouter, prefix="/entities", tags=["ENTITIES"])

app.include_router(Microservicesrouter, prefix="/microservices", tags=["REGISTER APPLICATIONS / MICROSERVICE"])
