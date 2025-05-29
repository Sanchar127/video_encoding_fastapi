from .roles import GeneralUser, Admin, SuperAdmin
from project.schemas.user import Role 
ROLE_HIERARCHY = {
    "super_admin": 3,
    "admin": 2,
    "user": 1
}

def has_permission_to_manage(requester_role: str, target_role: str) -> bool:
    return ROLE_HIERARCHY.get(requester_role, 0) > ROLE_HIERARCHY.get(target_role, 0)

def enforce_role_hierarchy(target_role: str, current_user, target_user_role: str = None):
    if not has_permission_to_manage(current_user.role, target_role):
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to assign this role."
        )
    if target_user_role and not has_permission_to_manage(current_user.role, target_user_role):
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to update a user with this role."
        )

def get_role_instance(user) -> GeneralUser:
  
    if user.role == Role.super_admin:
        return SuperAdmin()
    elif user.role == Role.admin:
        return Admin()
    return GeneralUser()
