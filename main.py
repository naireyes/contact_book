from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()
    email = CharField()


db.create_tables([Person])

# test = Person(first_name="John", last_name="Doe",
#               phone="1234567890", email="john.doe@company.com")
# test.save()
