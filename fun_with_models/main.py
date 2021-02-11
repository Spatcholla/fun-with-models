import actions
import getters
import mutations
from models import FullName


user_instance = mutations.build_user_create(actions.mock_create_request_data())
print(user_instance.dict(include={"slug", "email"}))

print(user_instance.dict(exclude={"slug"}))

print("UserCreate instance using actions and mutations to build")
print(user_instance)

print(getters.get_user_fullname(user_instance))
print(getters.get_user_slug(user_instance))

user_create_in_db = actions.mock_create_responce(user_instance)
# OR
# Use actions to get user data, think endpoint
# then use mutations to build UserCreate instance
# followed by using actions to send to DB
print("\nFull operation to create user in DB")
print(actions.mock_create_responce(mutations.build_user_create(actions.mock_create_request_data())))

mutations.update_firstname(user_instance, "Bob")

print("\nUpdated state")
print(getters.get_user_fullname(user_instance))
print(getters.get_user_slug(user_instance))

user_in_db_dict = getters.get_user_response_dict(mutations.build_user(actions.mock_db_fetch()))
print("\nUser Dict using getters. Getters is an example for clarity but seems overkill.")
print(user_in_db_dict)

user_in_db_json = getters.get_user_response_json(mutations.build_user(actions.mock_db_fetch()))
print("\nUser JSON using getters. Getters is an example for clarity but seems overkill.")
print(user_in_db_json)

print("\nUser Dict without getters")
print(mutations.build_user(actions.mock_db_fetch()).dict(by_alias=True))

print("\nUser JSON without getters")
print(mutations.build_user(actions.mock_db_fetch()).json())

my_fullname = FullName(first="Samuel", last="Moore")
print(mutations.full_name_read(my_fullname))
