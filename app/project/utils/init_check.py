

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from project.models.user import User  

async def is_first_run(db: AsyncSession) -> bool:
    result = await db.execute(select(User).where(User.role == "super_admin"))
    return result.scalar_one_or_none() is None
