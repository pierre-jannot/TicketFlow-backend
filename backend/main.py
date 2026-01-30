from fastapi import FastAPI, HTTPException, Request
from script import *
from pydantic import BaseModel, Field
from typing import List
from enum import Enum
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "code": 422,
            "message": "Unprocessable content",
            "value": ""
        }
    )

class Priority(str, Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"

class Status(str, Enum):
    Open = "Ouvert"
    InProgress = "En cours"
    Closed = "Fermé"

class SortMethod(str, Enum):
    Status = "Status"
    Priority = "Priority"
    Id = "Id"
    Date = "Date"
    NoSort = ""

class SortAndFilter(BaseModel):
    sortMethod: SortMethod
    filterMethod: List[str]

class UpdateTicket(BaseModel):
    status: Status

class NewTicket(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=0, max_length=100)
    priority: Priority
    tags: List[str]

@app.get("/")
def read_root():
    return "Bonjour !"

@app.get("/tickets")
def show_tickets():
    try:
        return readTickets()
    except:
        raise HTTPException(status_code=404, detail="Tickets not found")

@app.post("/tickets/sort")
def sort_tickets(sortAndFilter: SortAndFilter):
    try:
        sortMethod = sortAndFilter.sortMethod
        filterMethod = sortAndFilter.filterMethod
        tickets = readTickets()
        if sortMethod:
            tickets = sortTickets(sortMethod,tickets)
        print(len(tickets))
        if filterMethod:
            for filter in filterMethod:
                tickets = filterTickets(filter,tickets)
        if len(tickets)==0:
            raise ValueError
        return tickets
    except:
        if not tickets:
            raise HTTPException(status_code=404, detail="No tickets with this sort/filter method")
        else:
            raise HTTPException(status_code=400, detail="Bad sort/filter method request")

@app.post("/tickets")
def add_ticket(item: NewTicket):
    title = item.title
    description = item.description
    priority = item.priority
    tags = item.tags
    return addTicket(title,description,priority,tags)

@app.patch("/tickets/{id}")
def update_ticket(id: int, item: UpdateTicket):
    status = item.status
    try:
        return updateTicket(id,status)
    except:
        raise HTTPException(status_code=404, detail="Ticket not found")

@app.delete("/tickets/{id}")
def remove_ticket(id: int):
    try:
        return deleteTicket(id)
    except:
        raise HTTPException(status_code=404, detail="Ticket not found")
