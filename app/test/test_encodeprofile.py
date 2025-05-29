import pytest
from unittest.mock import AsyncMock, Mock, patch
from project.routes.encodeprofile import (
    create_encode_profile,
    create_encode_profile_details,
    get_all_encode_profiles,
    get_encode_profile_by_id,
    update_encode_profile,
    get_all_encode_profile_Details,
    get_encode_profileDetail_By_Id,
    update_encode_profileDetails,
    EncodeProfileCreate,
    EncodeProfileDetailsCreate,
)
from fastapi import HTTPException

# ----------------
# Mocks
# ----------------

class MockUser:
    def __init__(self, id=1, is_admin=True):
        self.id = id
        self.is_admin = is_admin

class MockEncodeProfiles:
    def __init__(self, id=1, name="Test Profile", user_id=1):
        self.id = id
        self.name = name
        self.user_id = user_id

class MockEncodeProfileDetails:
    def __init__(self, id=1, profile_id=1, width=1920, height=1080, video_bitrate=5000,
                 audio_bitrate=128, audio_channel=2, audio_frequency=44100, sc_threshold=0,
                 profile="main", level="4.0", max_bitrate=6000, bufsize=10000, movflags="faststart",
                 pix_fmt="yuv420p", acodec="aac", vcodec="h264", force_format="mp4"):
        self.id = id
        self.profile_id = profile_id
        self.width = width
        self.height = height
        self.video_bitrate = video_bitrate
        self.audio_bitrate = audio_bitrate
        self.audio_channel = audio_channel
        self.audio_frequency = audio_frequency
        self.sc_threshold = sc_threshold
        self.profile = profile
        self.level = level
        self.max_bitrate = max_bitrate
        self.bufsize = bufsize
        self.movflags = movflags
        self.pix_fmt = pix_fmt
        self.acodec = acodec
        self.vcodec = vcodec
        self.force_format = force_format

# ----------------
# Fixtures
# ----------------

@pytest.fixture
def mock_db():
    db = Mock()
    db.add = Mock()
    db.commit = Mock()
    db.refresh = Mock()
    db.query = Mock()
    return db

@pytest.fixture
def mock_user():
    return MockUser()

@pytest.fixture
def mock_profile_create():
    return EncodeProfileCreate(name="Test Profile", user_id=1)

@pytest.fixture
def mock_profile_details_create():
    return EncodeProfileDetailsCreate(
        profile_id=1,
        width=1920,
        height=1080,
        video_bitrate=5000,
        audio_bitrate=128,
        audio_channel=2,
        audio_frequency=44100,
        sc_threshold=0,
        profile="main",
        level="4.0",
        max_bitrate=6000,
        bufsize=10000,
        movflags="faststart",
        pix_fmt="yuv420p",
        acodec="aac",
        vcodec="libx264",
        force_format="mp4"
    )


# Test Cases

@pytest.mark.asyncio
async def test_create_encode_profile(mock_db, mock_user, mock_profile_create):
    mock_profile = MockEncodeProfiles(name=mock_profile_create.name, user_id=mock_profile_create.user_id)

    with patch("project.routes.encodeprofile.EncodeProfiles", return_value=mock_profile):
        result = await create_encode_profile(mock_profile_create, mock_db, mock_user)

    assert result == mock_profile
    mock_db.add.assert_called_once_with(mock_profile)
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_profile)

@pytest.mark.asyncio
async def test_create_encode_profile_details(mock_db, mock_user, mock_profile_details_create):
    mock_profile = MockEncodeProfiles(id=1)
    mock_db.query().filter().first.return_value = mock_profile

    mock_details = MockEncodeProfileDetails(**mock_profile_details_create.dict())

    with patch("project.routes.encodeprofile.EncodeProfileDetails", return_value=mock_details):
        result = await create_encode_profile_details(mock_profile_details_create, mock_db, mock_user)

    assert result == mock_details
    mock_db.add.assert_called_once_with(mock_details)
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_details)

@pytest.mark.asyncio
async def test_create_encode_profile_details_profile_not_found(mock_db, mock_user, mock_profile_details_create):
    mock_db.query().filter().first.return_value = None

    with pytest.raises(HTTPException) as exc:
        await create_encode_profile_details(mock_profile_details_create, mock_db, mock_user)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Encode Profile not found"

@pytest.mark.asyncio
async def test_get_all_encode_profiles(mock_db, mock_user):
    mock_profiles = [MockEncodeProfiles(id=i, name=f"Profile {i}") for i in range(1, 3)]
    mock_db.query().all.return_value = mock_profiles

    result = get_all_encode_profiles(mock_db, mock_user)  


    assert len(result) == 2
    assert result[0].name == "Profile 1"
    assert result[1].name == "Profile 2"

@pytest.mark.asyncio
async def test_get_all_encode_profiles_error(mock_db, mock_user):
    mock_db.query().all.side_effect = Exception("Database error")

    with pytest.raises(HTTPException) as exc:
        await get_all_encode_profiles(mock_db, mock_user)

    assert exc.value.status_code == 500
    assert exc.value.detail == "Could not retrieve the encode profiles."

@pytest.mark.asyncio
async def test_get_encode_profile_by_id(mock_db, mock_user):
    mock_profile = MockEncodeProfiles(id=1, name="Test Profile")
    mock_db.query().filter().first.return_value = mock_profile

    result = get_encode_profile_by_id(1, mock_db, mock_user)


    assert result == mock_profile
    assert result.name == "Test Profile"

@pytest.mark.asyncio
async def test_get_encode_profile_by_id_not_found(mock_db, mock_user):
    mock_db.query().filter().first.return_value = None

    with pytest.raises(HTTPException) as exc:
        await get_encode_profile_by_id(999, mock_db, mock_user)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Encoding profile not found."

@pytest.mark.asyncio
async def test_get_encode_profile_by_id_error(mock_db, mock_user):
    mock_db.query().filter().first.side_effect = Exception("Database error")

    with pytest.raises(HTTPException) as exc:
        await get_encode_profile_by_id(1, mock_db, mock_user)

    assert exc.value.status_code == 500
    assert exc.value.detail == "Failed to retrieve encoding profile."

@pytest.mark.asyncio
async def test_update_encode_profile(mock_db, mock_user, mock_profile_create):
    mock_profile = MockEncodeProfiles(id=1, name="Old Profile")
    mock_db.query().filter().first.return_value = mock_profile

    result = update_encode_profile(1, mock_profile_create, mock_db, mock_user)


    assert result.name == mock_profile_create.name
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_profile)

@pytest.mark.asyncio
async def test_update_encode_profile_not_found(mock_db, mock_user, mock_profile_create):
    # Simulate profile not found (return None for the query)
    mock_db.query().filter().first.return_value = None  
    
    # Ensure HTTPException is raised when the profile doesn't exist
    with pytest.raises(HTTPException) as exc:
        await update_encode_profile(999, mock_profile_create, mock_db, mock_user)
    
    # Check that the status code is 404 (not 500)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Encode profile not found."

@pytest.mark.asyncio
async def test_update_encode_profile_error(mock_db, mock_user, mock_profile_create):
    mock_db.query().filter().first.side_effect = Exception("Database error")

    with pytest.raises(HTTPException) as exc:
        await update_encode_profile(1, mock_profile_create, mock_db, mock_user)

    assert exc.value.status_code == 500
    assert exc.value.detail == "Failed to update encode profile"

@pytest.mark.asyncio
async def test_get_all_encode_profile_details(mock_db, mock_user):
    mock_details = [MockEncodeProfileDetails(id=i, profile_id=1) for i in range(1, 3)]
    mock_db.query().all.return_value = mock_details

    result = get_all_encode_profile_Details(mock_db, mock_user)

    assert len(result) == 2
    assert result[0].profile_id == 1

@pytest.mark.asyncio
async def test_get_all_encode_profile_details_error(mock_db, mock_user):
    mock_db.query().all.side_effect = Exception("Database error")

    with pytest.raises(HTTPException) as exc:
        await get_all_encode_profile_Details(mock_db, mock_user)

    assert exc.value.status_code == 500
    assert exc.value.detail == "Could not retrieve the encode profiles."

@pytest.mark.asyncio
async def test_get_encode_profile_detail_by_id(mock_db, mock_user):
    mock_details = MockEncodeProfileDetails(id=1, profile_id=1)
    mock_db.query().filter().first.return_value = mock_details

    result =  get_encode_profileDetail_By_Id(1, mock_db, mock_user)

    assert result == mock_details
