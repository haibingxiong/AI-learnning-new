from pydantic import BaseModel, Field
from typing import List
class text_type(BaseModel):
    title:List[str] = Field('小红书文本的5个标题',max_items=5,min_items=5)
    context: str = Field('小红书文本的正文内容')