from peewee import*

db = PostgresqlDatabase('car_2')


class BaseModell(Model):
    class Meta:
        database = db
