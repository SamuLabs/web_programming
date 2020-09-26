#!/usr/bin/env python
from fastapi import FastAPI

from routers import students, basics

app = FastAPI()

app.include_router(basics.router,
    tags=["basic"], responses={404:{"description": "Not found"}})

app.include_router(students.router,
    tags=["students"], responses={404:{"description": "Not found"}})