# from enum import Enum
from fastapi import FastAPI

# from typing import Union
# from pydantic import BaseModel
# app = FastAPI()

app = FastAPI()


@app.get('/')
def base_page():
    return {
        'Details': 'Simple FastAPI Interface',
        'Extra': 'Hello World!!'
    }


@app.get('/users/me')
def get_current_user():
    return {
        "info": "This is the current user's info",
        'hello': 'Hello Again'

    }


@app.get('/users/{user_id}')
def get_user_info(user_id: str):
    return {
        'info': user_id,
        'hello': 'Hello Again'
    }


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# learning required query
@app.get('/items/{item_id}')
async def required_query(item_id:int, required:str):
    return {
        'item_id':item_id,
        'required query': required
    }

@app.get("/items/{item_id}")
async def get_items(item_id: int, q: str | None = None, q1: str | None = None):
    if q and q1:
        return {
            'items_id': item_id,
            'query': {
                'q': q,
                'q1': q1
            }
        }
    else:
        return {
            'item_id': item_id,
            'more': 'There is no query!!'
        }


@app.get('/users/{user_id}/items/{items_id}')
async def get_multiple_path(user_id: int, items_id: str, q: str | None = None, short: bool = False):
    base_dict = {'user_id': user_id, 'items_id': items_id}
    if q:
        base_dict.update({'query-object': q})
    if not short:
        base_dict.update(
            {'descriptions': 'This is a very long descriptions stating something\
 very important, please read it all well.'})
    return base_dict



# class user(BaseModel):
#     name: Union[str, int, bool]
#     price: Union[float, None]
#     is_offer: Union[bool, None]


# class FoodEnum(str, Enum):
#     fruits = 'fruits'
#     vegetables = 'Vegetables'
#     dairy = 'Dairy'

# # food_test = FoodEnum("Vegetables")


# @app.get('/foods/{food_name}')
# def get_food(food_name: FoodEnum):
#     if food_name.value in ['fruits', 'Vegetables', 'Dairy']:
#         return {'food': f'{food_name.value} is very good for heath'}

#     else:
#         return {'Error': 'No Valid Food Given',
#                 'food_name.value': food_name.value
#                 }


# @app.get('/')
# async def read_root():
#     await time.sleep(5)
#     return {
#         'Hello': 'World',
#         'Test': 'Data',
#     }


# @app.put('/users/{user_id}')
# def update_user(user_id: int, user: user):
#     return {
#         'user_name': user.name,
#         'user_id': user_id
#     }


# @app.get('/users/{user_id}')
# def read_test(user_id: str, q: Union[str, None] = None):
#     # q_return = q if
#     return {'users': {
#         'user_id':  user_id,
#         'q': q
#     }}
