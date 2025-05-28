from pydantic import BaseModel
from typing import Optional

class SubtitleStyle(BaseModel):
    font: Optional[str] = "Arial"
    font_size: Optional[int] = 24
    color: Optional[str] = "#FFFFFF"
    outline_color: Optional[str] = "#000000"
    position: Optional[str] = "bottom-center"

class SubtitleRequest(BaseModel):
    language: Optional[str] = "pt"
    format: Optional[str] = "vertical"
    style: Optional[SubtitleStyle] = SubtitleStyle()
