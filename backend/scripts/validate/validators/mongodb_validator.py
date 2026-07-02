from .base_validator import BaseValidator


class MongoValidator(BaseValidator):

    @property
    def name(self):
        return "MongoDB Validation"

    def validate(self): ...

    # client = self.check(
    #     "Create Mongo Client",
    #     create_client,
    # )

    # self.check(
    #     "Ping Database",
    #     client.admin.command,
    #     "ping",
    # )
