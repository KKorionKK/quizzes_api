from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from services.config import get_settings
from sqlalchemy.orm import sessionmaker


settings = get_settings()
if hasattr(settings, "DB_PORT"):
    connection_string = f"{settings.DB_ADAPTER}://{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
else:
    connection_string = f"{settings.DB_ADAPTER}://{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"

engine = create_async_engine(connection_string, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=True)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
