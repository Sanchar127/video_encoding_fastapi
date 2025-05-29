
# from fastapi import HTTPException,Depends
# from  project.models.user import User
# from project.auth.auth import get_current_user
# ROLE_HIERARCHY = {
#     "super_admin": 3,
#     "admin": 2,
#     "user": 1
# }

# def has_permission_to_manage(requester_role: str, target_role: str) -> bool:
#     return ROLE_HIERARCHY[requester_role] > ROLE_HIERARCHY[target_role]



# def get_role_instance(user: User):
#     if user.role == Role.SUPER_ADMIN:
#         return SuperAdmin()
#     elif user.role == Role.ADMIN:
#         return Admin()
#     return GeneralUser()


# def require_permission(permission: str):
#     def wrapper(user: User = Depends(get_current_user)):
#         role_instance = get_role_instance(user)
#         if not getattr(role_instance, permission, lambda: False)():
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail=f"Permission '{permission}' denied"
#             )
#         return user
#     return wrapper




# def enforce_role_hierarchy(target_role: str, current_user: User, target_user_role: str = None):
   
#     if not has_permission_to_manage(current_user.role, target_role):
#         raise HTTPException(
#             status_code=403,
#             detail="You don't have permission to assign this role."
#         )
    
#     if target_user_role and not has_permission_to_manage(current_user.role, target_user_role):
#         raise HTTPException(
#             status_code=403,
#             detail="You don't have permission to update a user with this role."
#         )


# class GeneralUser:
#     def can_view_own_profile(self) -> bool:
#         return True

#     def can_update_own_profile(self) -> bool:
#         return True

#     def can_view_all_users(self) -> bool:
#         return False

#     def can_create_users(self) -> bool:
#         return False

#     def can_update_users(self) -> bool:
#         return False

#     def can_blacklist_own_tokens(self) -> bool:
#         return True

#     def can_blacklist_other_tokens(self) -> bool:
#         return False

#     def can_view_blacklisted_tokens(self) -> bool:
#         return False

#     def can_view_all_tokens(self) -> bool:
#         return False
    
#     def can_create_encode_profile(self) -> bool:
#         return False
    
#     def can_create_encode_profile_details(self) -> bool:
#         return False
    
#     def can_get_all_encode_profiles(self) -> bool:
#         return False

#     def can_get_encode_profile_by_id(self) -> bool:
#         return False
    
#     def can_update_encode_profile(self) -> bool:
#         return False
    
#     def can_get_all_encode_profile_Details(self) -> bool:
#         return False

#     def can_get_encode_profileDetail_By_Id(self) -> bool:
#         return False
    
#     def can_update_encode_profileDetails(self) -> bool:
#         return False

#     def can_get_all_jobs(self) -> bool:
#         return False

# class Admin(GeneralUser):
#     def can_view_all_users(self) -> bool:
#         return True

#     def can_create_users(self) -> bool:
#         return True

#     def can_update_users(self) -> bool:
#         return True

#     def can_blacklist_other_tokens(self) -> bool:
#         return True

#     def can_view_blacklisted_tokens(self) -> bool:
#         return True
    
#     def can_create_encode_profile(self) -> bool:
#         return True
    
#     def can_create_encode_profile_details(self) -> bool:
#         return True
    
#     def can_get_all_encode_profiles(self) -> bool:
#         return True

#     def can_get_encode_profile_by_id(self) -> bool:
#         return True
    
#     def can_update_encode_profile(self) -> bool:
#         return True
    
#     def can_get_all_encode_profile_Details(self) -> bool:
#         return True

#     def can_get_encode_profileDetail_By_Id(self) -> bool:
#         return True
    
#     def can_update_encode_profileDetails(self) -> bool:
#         return True

#     def can_get_all_jobs(self) -> bool:
#         return True
    
#     def can_retry_failed_job(self) -> bool:
#         return True

# class SuperAdmin(Admin):
#     def can_view_all_tokens(self) -> bool:
#         return True