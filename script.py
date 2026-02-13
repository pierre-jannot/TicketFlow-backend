import json
from datetime import date
from classes import *

def readTickets():
    with open('./tickets.json', 'r', encoding='utf-8') as file:
        tickets = json.load(file)
    return tickets

def writeTickets(tickets):
    with open('./tickets.json','w', encoding='utf-8') as file:
        json.dump(tickets, file, indent=2)

def buildTicket(id,title,description,priority,tags,createdAt):
    newTicket = {"id":id,
                 "title":title,
                 "description":description,
                 "priority":priority,
                 "status":"Ouvert",
                 "tags":tags,
                 "createdAt":createdAt}
    return newTicket

def addTicket(title, description, priority, tags):
    tickets = readTickets()
    id = max(tickets, key=lambda x: x["id"])["id"]+1
    createdAt = str(date.today())
    newTicket = buildTicket(id,title,description,priority,tags,createdAt)
    tickets.append(newTicket)
    writeTickets(tickets)
    return newTicket

def updateTicket(id, status):
    tickets = readTickets()
    newTicket = []
    found = False
    for ticket in tickets:
        if ticket["id"] == id:
            ticket["status"] = status
            newTicket = ticket
            found = True
    if found:
        writeTickets(tickets)
        return newTicket
    else:
        raise ValueError("Ticket not found")

def deleteTicket(id):
    tickets = readTickets()
    found = False
    for i, ticket in enumerate(tickets):
        if ticket["id"] == id:
            tickets.pop(i)
            found = True
            break
    if found:
        writeTickets(tickets)
        return "Ticket " + str(id) + " deleted."
    else:
        raise ValueError("Ticket not found")

def filterTickets(value,tickets):
    ticketList = []
    for ticket in tickets:
        if value in ticket["tags"]:
            ticketList.append(ticket)
    return ticketList
    
def sortTickets(sortMethod,tickets):
    if sortMethod==SortMethod.Status:
        ticketList = []
        ticketDictionnary = {"Ouvert" : [], "En cours" : [], "Fermé" : []}
        for ticket in tickets:
            ticketDictionnary[ticket["status"]].append(ticket)
        for key in ticketDictionnary:
            for value in ticketDictionnary[key]:
                ticketList.append(value)
        return ticketList
    elif sortMethod==SortMethod.Priority:
        ticketList = []
        ticketDictionnary = {"High" : [], "Medium" : [], "Low" : []}
        for ticket in tickets:
            ticketDictionnary[ticket["priority"]].append(ticket)
        for key in ticketDictionnary:
            for value in ticketDictionnary[key]:
                ticketList.append(value)
        return ticketList
    elif sortMethod==SortMethod.IdAsc:
        return sorted(tickets, key=lambda x: x["id"])
    elif sortMethod==SortMethod.IdDesc:
        return sorted(tickets, key=lambda x: x["id"], reverse=True)
    elif sortMethod==SortMethod.DateAsc:
        return sorted(tickets, key=lambda x: x["createdAt"])
    else:
        return sorted(tickets, key=lambda x: x["createdAt"], reverse=True)

def countTickets():
    tickets = readTickets()
    statusDict = {"Open" : 0, "In progress" : 0, "Closed" : 0}
    for ticket in tickets:
        tempStatus = ticket.get("status")
        statusDict[tempStatus] += 1
    return statusDict