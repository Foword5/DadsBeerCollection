import peewee as p

#Connect to the database
db = p.SqliteDatabase('DataBase.db')

#Create the tables
class Brewery(p.Model):
    id = p.AutoField(primary_key=True)
    name = p.CharField()
    country = p.CharField(null=True)

class Shop(p.Model):
    id = p.AutoField(primary_key=True)
    name = p.CharField()
    city = p.CharField(null=True)

class Beer(p.Model):
    id = p.AutoField(primary_key=True)
    name = p.CharField()
    photo = p.BlobField(null=True)
    shortDescr = p.CharField(null=True)
    description = p.CharField(null=True)
    date = p.DateField(null=True)
    note = p.IntegerField(null=True)
    brewery = p.ForeignKeyField(Brewery,null=True)
    shop = p.ForeignKeyField(Shop,null=True)

