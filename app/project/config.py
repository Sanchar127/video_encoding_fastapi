import os
from dotenv import load_dotenv
import pathlib
from functools import lru_cache
from urllib.parse import quote


# env_path = pathlib.Path('.') / '.env'

# load_dotenv(
#     dotenv_path=env_path
# )

load_dotenv()

class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    API_KEY:str = os.getenv("API_KEY")
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")
    RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")

    PROJECT_NAME: str = os.environ.get("PROJECT_NAME")
    PROJECT_VERSION: str = "0.0.1"

    APP_ENV = os.getenv("APP_ENV")
    APP_DEBUG = os.getenv("APP_DEBUG")
    APP_LOG_LEVEL = os.getenv("APP_LOG_LEVEL")
    CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY")

    ORIGIN_URL:str = os.getenv("APP_URL")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = quote(os.getenv("MYSQL_USER_PASSWORD"))
    MYSQL_SERVER: str = os.getenv("DB_HOST", "localhost")
    MYSQL_PORT=os.getenv("DB_DEFAULT_PORT", 3306)
    MYSQL_DB: str = os.getenv("MYSQL_DATABASE")
    DATABASE_URL = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTE = 60 * 24  # 24 hours
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 90  # 90 days
    ALGORITHM = "HS256"
    PUBLIC_PATH = os.path.join(os.getcwd(), os.getenv("APP_PROJECT_FOLDER"), "static")
    FILE_SAVE_PATH = str(ORIGIN_URL) + "/static"

    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # time format
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    DATETIME_FORMAT_MOMENT = "YYYY-MM-DD HH:mm:ss"
    DATE_FORMAT_MOMENT = "YYYY-MM-DD"

    # redis cache
    CAPTCHA_ID = "captcha:{captcha_id}"
    LOGIN_ERROR_TIMES = "login_error_times:{ip}"
    LOGIN_USER = "login_user:{token}"

    # Spaces details
    S3_KEY=os.getenv("S3_KEY")
    S3_SECRET=os.getenv("S3_SECRET")
    S3_ENDPOINT=os.getenv("S3_ENDPOINT")
    S3_REGION=os.getenv("S3_REGION")
    S3_BUCKET=os.getenv("S3_BUCKET")

    REDIS_URL=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")

    # Email Related Settings
    MAIL_DRIVER=os.getenv("MAIL_DRIVER")
    MAIL_SERVER=os.getenv("MAIL_HOST")
    MAIL_PORT=os.getenv("MAIL_PORT")    
    MAIL_USERNAME=os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
    MAIL_ENCRYPTION=os.getenv("MAIL_ENCRYPTION")
    MAIL_FROM = os.getenv("MAIL_FROM")
    MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")

    SMTP_TLS: bool = True

    EMAIL_TEMPLATE_FOLDER:str = os.path.join(os.getcwd(), 'templates', 'email_templates/')


    MAILGUN_DOMAIN=os.getenv("MAILGUN_DOMAIN")
    MAILGUN_API_KEY=os.getenv("MAILGUN_API_KEY")


class DevelopmentConfig(BaseConfig):
    app_log_level = 10 #used for logging purpose only

class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "dev": DevelopmentConfig,
        "prod": ProductionConfig,
        "test": TestingConfig
    }

    config_name = os.environ.get("APP_ENV", "dev")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()