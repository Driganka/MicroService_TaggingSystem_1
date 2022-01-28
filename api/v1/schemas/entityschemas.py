def entitySchemas(item) -> dict:
    return {
        "entity_id": item["entity_id"],
        "entity_name": item["entity_name"],
        "webhook_url": item["webhook_url"],
        "valid_tags": item["valid_tags"] 
    }

def entitiesSchema(entity) -> list:
    return [entitySchemas(item) for item in entity]