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

naira = Person(first_name="Naira", last_name="Reyes",
               phone="2350985467", email="naira.reyes@company.com")
naira.save()

# Person.get(Person.first_name == 'John')
# grabbing_test = Person.get(Person.first_name == 'John')
# print(grabbing_test.first_name)
