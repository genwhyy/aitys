from typing import List, Optional
from fastapi import Request

class UserCreate:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.login: Optional[str] = None
        self.user_fname: Optional[str] = None
        self.usebr_sname: Optional[str] = None
        self.password: Optional[str] = None
    
    async def load_data(self):
        form = await self.request.form()
        self.login = form.get("login")
        self.user_fname = form.get("user_fname")
        self.user_sname = form.get("user_sname")
        self.password = form.get("password")
    
    async def is_valid(self):
        if not self.login:
            self.errors.append("Enter login")
        if not self.user_fname:
            self.errors.append("Enter name")
        if not self.user_sname:
            self.errors.append("Enter surname")
        if not self.password:
            self.errors.append("Enter password")
        if not self.errors:
            return True
        return False