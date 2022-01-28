def microserviceEntity(item) -> dict:
    return {
        "id": item["id"],
        "webhook": item["webhook"],
    }

def microservicesEntity(entity) -> list:
    return [microserviceEntity(item) for item in entity]