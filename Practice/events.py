# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.on_event("startup")
# async def start():
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
# items = {}
#
#
# @app.on_event("startup")
# async def startup_event():
#     items["foo"] = {"name": "Fighters"}
#     items["bar"] = {"name": "Tenders"}
#
#
# @app.get("/items/{item_id}")
# async def read_items():
#     return items
x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"
