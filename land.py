from pydantic import BaseModel


class Tag(BaseModel):
    id: int
    tag:str


class City(BaseModel):
    city_id: int
    name: str
    tags: list[Tag]

input_json = """
{
   "city_id": "132"",
   "name": "Moscow",
   "tags": [{
       "id": 1, "tag": "capital"
    },{
        "id": 2, "tag": "big city"
    }]
}
"""

try:
    city = City.parse_raw(input_json)
except  ValidationError as e:
    print("Exeption", e.json())
else:
    some = city.tags[0].tag
    tag = city.tags[1]
    print(tag.json) 
