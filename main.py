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

# naira = Person(first_name="Naira", last_name="Reyes",
#                phone="2350985467", email="naira.reyes@company.com")
# naira.save()
# john = Person(first_name="John", last_name="Doe",
#               phone="8760985467", email="john.doe@company.com")
# john.save()
# jane = Person(first_name="Jane", last_name="Smith",
#               phone="8760295467", email="jane.smith@company.com")
# jane.save()
