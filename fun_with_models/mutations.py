from typing import Any, Dict
from slugify import slugify

from models import UserCreate, User


def update_firstname(state: UserCreate, firstname: str) -> None:
    """Update UserCreate instance firstname

    Args:
        state (UserCreate): UserCreate instance
        firstname (str): New user firstname
    """
    state.name.first = firstname
    state.slug = slugify(f"super-user: {state.name.first} {state.name.last}")


def build_user_create(data: Dict[Any, Any]) -> UserCreate:
    """Build UserCreate instance

    Args:
        data (Dict[Any, Any]): Data used to build UserCreate instance

    Returns:
        UserCreate: UserCreate instance
    """
    user = UserCreate(
        **data, slug=slugify(f"super-user: {data['name']['first']} {data['name']['last']}")
    )
    print(id(user))
    return user


def full_name_read(fullname):
    return {"first": fullname.first, "Last": fullname.last}


def build_user(data: Dict[Any, Any]) -> User:
    """Build User response instance

    Args:
        data (Dict[Any, Any]): Data from source

    Returns:
        User: User response instance
    """
    return User(**data)
