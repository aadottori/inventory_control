from fastapi import FastAPI
import models, database, hashing
from database import engine, get_db
from routers import product, user, authentication, attribute
import uvicorn


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

get_db = database.get_db

app.include_router(authentication.router)
app.include_router(product.router)
app.include_router(attribute.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
