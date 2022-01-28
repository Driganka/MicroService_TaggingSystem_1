from fastapi import APIRouter
from api.v1.config import connection
from api.v1.microservices.models import Microservices
from api.v1.microservices.schemas import microserviceEntity, microservicesEntity

Microservicesrouter = APIRouter()

@Microservicesrouter.get('/find-microservice/{id}')
async def find_Microservice_by_id(id):
    return microserviceEntity(connection.local.Microservices.find_one({"id": id}))

@Microservicesrouter.get('/get-microservices')
async def find_all_Microservices():
    return microservicesEntity(connection.local.Microservices.find())
    
@Microservicesrouter.post('/create-microservice')
async def create_Microservices(Microservices: Microservices):
    connection.local.Microservices.insert_one(dict(Microservices))
    return microservicesEntity(connection.local.Microservices.find())

@Microservicesrouter.put('/update-microservice/{id}')
async def update_Microservices(id, Microservices: Microservices):
    connection.local.Microservices.find_one_and_update( {"id": id}, { "$set": dict(Microservices)})
    return microserviceEntity(connection.local.Microservices.find_one( {"id": id}))
    
@Microservicesrouter.delete('/delete-microservice/{id}')
async def delete_Microservices(id, Microservices: Microservices):
    return microserviceEntity(connection.local.Microservices.find_one_and_delete({"id": id}))