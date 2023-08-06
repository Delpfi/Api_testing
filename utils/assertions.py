from jsonschema import validate
from pydantic import BaseModel
class Assert:
    @staticmethod
    def validate_schema(instance: dict):
        validate(instance = instance, schema = BaseModel.schema())