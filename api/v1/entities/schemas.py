def sEntity(item) -> dict:
    return {
        "entity_id": item["entity_id"],
        "entity_name": item["entity_name"],
        "tags": item["tags"],
    }

def sEntities(entity) -> list:
    return [sEntity(item) for item in entity]