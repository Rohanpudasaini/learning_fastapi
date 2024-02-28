from fastapi import FastAPI

from typing import Union
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer : Union[bool, None]


@app.get('/')
def read_root():
    return {
        'Hello':'World',
        'Test':'Data',
        }
    
@app.get('/items/{item_id}')
def read_test(item_id:int, q:Union[str,None]= None):
    # q_return = q if 
    return{'items':{
        'item_id':  item_id,
        'q': q
    }}
    
    

@app.put('/items/{item_id}')
def update_item(item_id:int, item:Item):
    return {
        'item_name': item.name,
        'item_price': item.price,
        'item_id': item_id
    }