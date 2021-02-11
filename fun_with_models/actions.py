from typing import Any, Dict

from models import UserCreate


def mock_create_request_data() -> Dict[Any, Any]:
    """Function that fetches data from a source and returns a dictionary

    Returns:
        Dict[Any, Any]: Response data from source
    """
    return {
        "name": {
            "first": "Stan",
            "last": "Lee",
        },
        "email": "stan.lee@foo.bar",
    }


def mock_create_responce(user: UserCreate) -> Dict[Any, Any]:
    print(id(user))
    return {"message": "success", "payload": user}


def mock_db_fetch() -> Dict[Any, Any]:
    return {
        "id_user": "first_user",
        "name": {"first": "Stan", "last": "Lee"},
        "email": "stan.lee@foo.bar",
        "slug": "super-user-stan-lee",
    }
