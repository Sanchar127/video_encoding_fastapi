# routers/init_admin.py

from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from project.db.database import get_db
from project.models.user import User
from project.utils.security import hash_password 
from project.utils.init_check import is_first_run

router = APIRouter()

@router.get("/admin/init", response_class=HTMLResponse)
async def show_init_form(request: Request, db: AsyncSession = Depends(get_db)):
    if not await is_first_run(db):
        return RedirectResponse(url="/login")
    return HTMLResponse("""
        <form method="post">
            <input name="username" placeholder="Username" required />
            <input name="email" type="email" placeholder="Email" required />
            <input name="password" type="password" placeholder="Password" required />
            <button type="submit">Create Super Admin</button>
        </form>
    """)

@router.post("/admin/init")
async def create_super_admin(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    if not await is_first_run(db):
        return RedirectResponse(url="/login")
    
    new_admin = User(
        username=username,
        email=email,
        password=hash_password(password),
        role="super_admin",
        is_activated=True,
        status="active"
    )
    db.add(new_admin)
    await db.commit()
    return RedirectResponse(url="/login", status_code=302)
