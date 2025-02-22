from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Mlflow(BaseSettings):
    host: str
    port: str

    @property
    def uri(self):
        return f"http://{self.host}:{self.port}"

    model_config = SettingsConfigDict(env_prefix="MLFLOW_", env_file=".env", extra="ignore")


class Model(BaseSettings):
    name: str
    alias: str

    @property
    def uri(self):
        return f"models:/{self.name}@{self.alias}"
    
    model_config = SettingsConfigDict(env_prefix="MODEL_", env_file=".env", extra="ignore")


class Settings(BaseModel):
    mlflow: Mlflow = Mlflow()
    model: Model = Model()


settings = Settings()
print("Settings object is created with values:\n", settings)