# Fast APi
To run the server, `fastapi dev server.py`
This uses *uvicorn* to actively check the state of the server file 
and update when necessary

## Adding exceptions
`from fastapi import FastApi, HTTPException`  

## Multiple items
```python
@app.get("/items")
def get_items(limit int=10):
    return urls[0:limit]
```

## Custom Item Types
```python
from pydantic import BaseModel

items = []

class TodoItem(BaseModel):
    # Json Payload
    # Without a default, it becomes a Required parameter
    text : str = None
    is_done = False

# We can now use it to expect a json payload instead of query
@app.post("/item")
def create_item(item : TodoItem):
    items.append(item)
```

-  Can also be used to specify a response

```python
@app.get("/item/{id}")
def get_item(id : int)->TodoItem:
```

## Response model
```python
@app.get("/item/{id}")
def get_item(id : int,response_model=TodoItem):
    pass
@app.get("/items")
def get_items(limit: int=10,response_model=list[TodoItem]):
    pass
```
