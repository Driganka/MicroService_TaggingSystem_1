from fastapi import APIRouter
from api.v1.config.db import connection
from api.v1.schemas.tagsschemas import tagEntity, tagsEntity
from api.v1.models.tagmodel import Tags

Tagsrouter = APIRouter()

@Tagsrouter.get('/find-tag/{id}')
async def find_Tag_by_id(id):
    return tagEntity(connection.local.TagsC.find_one({"id": id}))

@Tagsrouter.get('/get-tags')
async def find_all_Tags():
    return tagsEntity(connection.local.TagsC.find())
    
@Tagsrouter.post('/create-tags')
async def create_Tags(Tags: Tags):
    connection.local.Entities.insert_one(dict(Tags))
    return tagsEntity(connection.local.TagsC.find())

@Tagsrouter.put('/update-tags/{id}')
async def update_Tags(id, Tags: Tags):
    connection.local.Entities.find_one_and_update( {"id": id}, { "$set": dict(Tags)})
    return tagEntity(connection.local.TagsC.find_one( {"id": id}))
    
@Tagsrouter.delete('/delete-tags/{id}')
async def delete_Tags(id):
    return tagEntity(connection.local.TagsC.find_one_and_delete({"id": id}))