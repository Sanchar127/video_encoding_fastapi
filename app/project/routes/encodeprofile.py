from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.database import get_db, SessionLocal
from ..models.encodeprofile import EncodeProfiles, EncodeProfileDetails
from ..schemas.encodeprofile import EncodeProfileCreate, EncodeProfileDetailsCreate,EncodeProfileResponse,EncodeProfileDetailsResponse
from .user import get_admin_user
from ..models.user import User
from ..schemas.encodeprofile import EncodeProfileResponse
from typing import List

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/encode-profile", response_model=EncodeProfileResponse)
async def create_encode_profile(profile: EncodeProfileCreate, db: Session = Depends(get_db),  current_user: User = Depends(get_admin_user)):
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
    try:
        profiles = db.query(EncodeProfiles).all()
        return profiles
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve the encode profiles.")



@router.get("/encodeprofile/${id}", response_model=EncodeProfileResponse)
def get_encode_profile_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    try:
        profile = db.query(EncodeProfiles).filter(EncodeProfiles.id == id).first()
        if not profile:
            raise HTTPException(status_code=404, detail="Encoding profile not found.")
       
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve encoding profile.")

@router.put("/encodeprofile/update/{id}", response_model=EncodeProfileResponse)
def update_encode_profile(
    id: int,
    update_data: EncodeProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    # Function body

    try:
        
        profile = db.query(EncodeProfiles).filter(EncodeProfiles.id == id).first()

        if not profile:
            raise HTTPException(status_code=404, detail="Encode profile not found.")

        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(profile, key, value)

        db.commit()
        db.refresh(profile)
        return profile

    except Exception as e:
        raise HTTPException(status_code=500 , detail= "Failed to update encode profile")


@router.get("/encodeprofileDetals", response_model=List[EncodeProfileDetailsResponse])
def get_all_encode_profile_Details(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    try:
        profileDetails = db.query(EncodeProfileDetails).all()
        return profileDetails
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve the encode profiles.")


@router.get("/encodeprofileDetails/{id}", response_model=EncodeProfileDetailsResponse)
def get_encode_profileDetail(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
        
        profileDetails = db.query(EncodeProfileDetails).filter(EncodeProfileDetails.id == id).first()
   

        if not profileDetails:
            raise HTTPException(status_code=404, detail="Encode profileDetails not found.")
        
        return profileDetails
        


    

    
@router.put("/encodeprofileDetails/update/{id}", response_model=EncodeProfileDetailsResponse)
def update_encode_profileDetails(
    id: int,
    update_data: EncodeProfileDetailsCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):


    try:
        
        profileDetails = db.query(EncodeProfileDetails).filter(EncodeProfileDetails.id == id).first()
        # profiles= db.query(EncodeProfiles)
        # if profiles.id != update_data.profile_id :       
        #     raise HTTPException(status_code==404 , detail="Encode Profile not found")

        if not profileDetails:
            raise HTTPException(status_code=404, detail="Encode profileDetails not found.")
        
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(profileDetails, key, value)

        db.commit()
        db.refresh(profileDetails)
        return profileDetails

    except Exception as e:
        raise HTTPException(status_code=500 , detail= "Failed to update encode profile Details ")
    






