from pydantic import BaseModel, Field
from typing import Optional, Union

# Category output class
class Category(BaseModel):
    predicted_category: str = Field(description="predicted category")
    prediction_possibility: Optional[float] = Field(description="predicted category possibility between 0 and 1")
    # second_prediction: str = Field(description="second possible matched category")
    # second_prediction_possiblity: str = Field(description="second possible matched category possibility between 0 and 1")

class CategoryNotFound(BaseModel):
    warning: str = Field(description="product category not found.")


class FinalResponse(BaseModel):
    final_output: Union[Category, CategoryNotFound]