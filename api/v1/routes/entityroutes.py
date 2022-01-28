from fastapi import APIRouter
from api.v1.config.db import connection
from api.v1.schemas.entityschemas import entitySchemas, entitiesSchema
from api.v1.models.entitymodel import Entities

Entitiesrouter = APIRouter()

@Entitiesrouter.get('/find-Entity/{id}')
async def find_Entity_by_id(id):
    return entitySchemas(connection.local.Entities.find_one({"id": id}))

@Entitiesrouter.get('/get-Entities')
async def find_all_Entities():
    return entitiesSchema(connection.local.Entities.find())
    
@Entitiesrouter.post('/create-Entity')
async def create_Entities(Entities: Entities):
    connection.local.Entities.insert_one(dict(Entities))
    return entitiesSchema(connection.local.Entities.find())

@Entitiesrouter.put('/update-Entity/{id}')
async def update_Entities(id, Entities: Entities):
    connection.local.Entities.find_one_and_update( {"id": id}, { "$set": dict(Entities)})
    return entitySchemas(connection.local.Entities.find_one( {"id": id}))
    
@Entitiesrouter.delete('/delete-Entity/{id}')
async def delete_Entities(id, Entities: Entities):
    return entitySchemas(connection.local.Entities.find_one_and_delete({"id": id}))