def parse_db_response(response):
    if isinstance(response, list):
        result = []
        for item in response:
            item_id = str(item.pop("_id"))
            result.append({"id": item_id, **item})
        return result
    elif isinstance(response, dict):
        result = {}
        item_id = str(response.pop("_id"))
        result = {"id": item_id, **response}
        return result
    else:
        raise TypeError(
            f"Tipo de dato invalido: {response} -> type: {type(response)}")
