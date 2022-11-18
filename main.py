from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class ResponseDTO(BaseModel):
    code : int
    mesege : str
    data : object

class Cat(BaseModel):
    name: str
    id: int

app = FastAPI()

@app.get("/first/{id}")
async def root(id : int):           
    return {"message" : "Hello World", "id" : id}

@app.get("/second")
async def second(skip:int = 0, limit: int = 10):
    return {"skip" : skip, "limit" : limit}

@app.post("/cat")
async def cat(cat : Cat):
    return cat

@app.get("/error")
async def error():
    dto = ResponseDTO(
        code=0,
        mesege="페이지가 없습니다.",
        data=None
    )
    return JSONResponse(status_code=404, content=jsonable_encoder(dto))

    # name = True
    # if name == True:
    #     return JSONResponse(status_code=200, content={"message" : "성공"})
    
    # else:
    #     return JSONResponse(status_code=404, content={"message" : "실패"})

@app.get("/error1")
async def error1():
    return HTTPException(status_code=404, detail={"message" : "Item not found"})