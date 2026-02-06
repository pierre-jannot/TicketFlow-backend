from enum import Enum

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
    IdAsc = "Id Asc"
    IdDesc = "Id Desc"
    DateAsc = "Date Asc"
    DateDesc = "Date Desc"
    NoSort = ""