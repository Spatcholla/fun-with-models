from typing import Any, Dict, Union

from pydantic.types import Json

from models import User, UserCreate


def get_user_fullname(state: Union[User, UserCreate]) -> str:
    """Function to get user's fullname

    Args:
        state (User): User instance

    Returns:
        str: User fullname
    """
    return f"{state.name.first} {state.name.last}"


def get_user_slug(state: Union[User, UserCreate]) -> str:
    """Function to get user slug

    Args:
        state (User): User instance

    Returns:
        str: User slug
    """
    return state.slug


def get_user_response_dict(state: Union[User, UserCreate]) -> Dict[Any, Any]:
    """Function to return dictionary from User instance

    Args:
        state (User): User instance

    Returns:
        Dict[Any, Any]: Dictionary outpu of User instance
    """
    return state.dict()


def get_user_response_json(state: User) -> str:
    return state.json()
