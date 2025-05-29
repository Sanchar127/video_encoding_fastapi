from fastapi import HTTPException, Depends, status
from .roles import GeneralUser, Admin, SuperAdmin
from project.schemas.user import Role
from .utils import get_role_instance
from typing import Callable
from project.auth.auth import get_current_user
def require_permission(permission: str) -> Callable:
    

    def wrapper(user = Depends(get_current_user)):
        role_instance = get_role_instance(user)
        if not getattr(role_instance, permission, lambda: False)():
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission '{permission}' denied"
            )
        return user

    return wrapper
