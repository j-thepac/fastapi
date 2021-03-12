from fastapi import FastAPI 
from pydantic import BaseModel #model
# import requests

app = FastAPI()
db = []

class Person(BaseModel):
    name: str

@app.get('/')
def index():return {'person' : 'name'}

@app.get('/persons')
def get_persons():
    results = []
    for person in db:results.append(person)
    return results

@app.get('/persons/{person_id}')
def get_person(person_id: int):return db[person_id-1]

@app.post('/persons')
def create_person(person: Person):
    db.append(person)
    return db[-1]

@app.delete('/persons/{person_id}')
def delete_person(person_id: int):
    db.pop(person_id-1)
    return {}