class GeneralUser:
    def can_view_own_profile(self): return True
    def can_update_own_profile(self): return True
    def can_view_all_users(self): return False
    def can_create_users(self): return False
    def can_update_users(self): return False
    def can_blacklist_own_tokens(self): return True
    def can_blacklist_other_tokens(self): return False
    def can_view_blacklisted_tokens(self): return False
    def can_view_all_tokens(self): return False
    def can_create_encode_profile(self): return False
    def can_create_encode_profile_details(self): return False
    def can_get_all_encode_profiles(self): return False
    def can_get_encode_profile_by_id(self): return False
    def can_update_encode_profile(self): return False
    def can_get_all_encode_profile_Details(self): return False
    def can_get_encode_profileDetail_By_Id(self): return False
    def can_update_encode_profileDetails(self): return False
    def can_get_all_jobs(self): return False

class Admin(GeneralUser):
    def can_view_all_users(self): return True
    def can_create_users(self): return True
    def can_update_users(self): return True
    def can_blacklist_other_tokens(self): return True
    def can_view_blacklisted_tokens(self): return True
    def can_create_encode_profile(self): return True
    def can_create_encode_profile_details(self): return True
    def can_get_all_encode_profiles(self): return True
    def can_get_encode_profile_by_id(self): return True
    def can_update_encode_profile(self): return True
    def can_get_all_encode_profile_Details(self): return True
    def can_get_encode_profileDetail_By_Id(self): return True
    def can_update_encode_profileDetails(self): return True
    def can_get_all_jobs(self): return True
    def can_retry_failed_job(self): return True

class SuperAdmin(Admin):
    def can_view_all_tokens(self): return True
