def usuario_schema(user) -> dict:
    return {
        "id": user[0],
        "name": user[1],
        "surname": user[2]
    }

def schema_user(usuarios) -> list[dict]:
    return [usuario_schema(user) for user in usuarios]
