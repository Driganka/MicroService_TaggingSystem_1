def tagEntity(item) -> dict:
    return {
        "entity_id": item["entity_id"],
        "entity_name": item["entity_name"],
        "valid_tags": item["valid_tags"] 
    }
def tagsEntity(entity) -> list:
    return [tagEntity(item) for item in entity]