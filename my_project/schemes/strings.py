from pydantic import BaseModel


class InputStr(BaseModel):
    choice: str