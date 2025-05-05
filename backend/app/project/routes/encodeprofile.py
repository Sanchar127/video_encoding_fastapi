from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.database import get_db, SessionLocal
from ..models.encodeprofile import EncodeProfiles, EncodeProfileDetails
from ..schemas.encodeprofile import EncodeProfileCreate, EncodeProfileDetailsCreate,EncodeProfileResponse,EncodeProfileDetailsResponse
from .user import get_admin_user
from ..models.user import User
from ..schemas.encodeprofile import EncodeProfileResponse
from typing import List
from fastapi import Query,Body
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/encode-profile", response_model=EncodeProfileResponse)
async def create_encode_profile(profile: EncodeProfileCreate, db: Session = Depends(get_db),  current_user: User = Depends(get_admin_user)):
    """
    It is use to create encode profile.
	"""
    db_profile = EncodeProfiles(name=profile.name,user_id=profile.user_id)

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@router.post("/encode-profile-details", response_model=EncodeProfileDetailsCreate)
async def create_encode_profile_details(details: EncodeProfileDetailsCreate, db: Session = Depends(get_db),  current_user: User = Depends(get_admin_user)):
    db_profile = db.query(EncodeProfiles).filter(EncodeProfiles.id == details.profile_id).first()

    if not db_profile:
        raise HTTPException(status_code=404, detail="Encode Profile not found")

    db_profile_details = EncodeProfileDetails(
        profile_id=details.profile_id,
        width=details.width,
        height=details.height,
        video_bitrate=details.video_bitrate,
        audio_bitrate=details.audio_bitrate,
        audio_channel=details.audio_channel,
        audio_frequency=details.audio_frequency,
        sc_threshold=details.sc_threshold,
        profile=details.profile,
        level=details.level,
        max_bitrate=details.max_bitrate,
        bufsize=details.bufsize,
        movflags=details.movflags,
        pix_fmt=details.pix_fmt,
        acodec=details.acodec,
        vcodec=details.vcodec,
        force_format=details.force_format
    )
    db.add(db_profile_details)
    db.commit()
    db.refresh(db_profile_details)

    return db_profile_details



@router.get("/encodeprofile", response_model=List[EncodeProfileResponse])
def get_all_encode_profiles(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    """
	Use to  get all data of encodeprofile 
	"""
    try:
        profiles = db.query(EncodeProfiles).all()
        return profiles
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve the encode profiles.")



def get_encode_profile_by_id(profile_id: int, db: Session, current_user: User):
    try:
        profile = db.query(EncodeProfiles).filter(EncodeProfiles.id == profile_id).first()
        if not profile:
            raise HTTPException(status_code=404, detail="Encoding profile not found.")
        return profile
    except HTTPException:
        raise  # re-raise HTTP exceptions without wrapping
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to retrieve encoding profile.")

@router.put("/encodeprofile/update", response_model=EncodeProfileResponse)
def update_encode_profile(
    id: int = Query(..., description="ID of the encode profile to update"),
    update_data: EncodeProfileCreate = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    """
    Use to update the encode profile.
    """
    try:
        # Fetch the profile
        profile = db.query(EncodeProfiles).filter(EncodeProfiles.id == id).first()
        
        # If the profile doesn't exist, raise a 404
        if not profile:
            raise HTTPException(status_code=404, detail="Encode profile not found.")

        # Update the profile fields with provided data
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(profile, key, value)

        # Commit and refresh the profile
        db.commit()
        db.refresh(profile)
        return profile

    except HTTPException as e:
        # Re-raise HTTP exceptions (such as 404 not found)
        raise e
    except Exception as e:
        # Log unexpected errors and raise 500
        print(f"Error while updating encode profile: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update encode profile")


@router.get("/encodeprofileDetals", response_model=List[EncodeProfileDetailsResponse])
def get_all_encode_profile_Details(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    """
	Use to get Encode Profile details. 
	"""
    try:
        profileDetails = db.query(EncodeProfileDetails).all()
        return profileDetails
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve the encode profiles.")


@router.get("/encodeprofileDetails", response_model=EncodeProfileDetailsResponse)
def get_encode_profileDetail_By_Id(
     id: int = Query(..., description="ID of the encode profile Deatils "),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
        """
	Use to get Encode Profile details by id.
     
        """
        
        profileDetails = db.query(EncodeProfileDetails).filter(EncodeProfileDetails.id == id).first()
   

        if not profileDetails:
            raise HTTPException(status_code=404, detail="Encode profileDetails not found.")
        
        return profileDetails
        



@router.put("/encodeprofileDetails/update", response_model=EncodeProfileDetailsResponse)
def update_encode_profileDetails(
    id: int = Query(..., description="ID of the encode profile details to update"),
    update_data: EncodeProfileDetailsCreate = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    """
    Use to update encode profile details.
    """
    try:
        profileDetails = db.query(EncodeProfileDetails).filter(EncodeProfileDetails.id == id).first()

        if not profileDetails:
            raise HTTPException(status_code=404, detail="Encode profileDetails not found.")
        
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(profileDetails, key, value)

        db.commit()
        db.refresh(profileDetails)
        return profileDetails

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update encode profile details")

    






