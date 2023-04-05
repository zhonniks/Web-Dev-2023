from django.db import models
"""
create table product (
     id INTEGER , 
     name Varchar(255)
     price NUMERIC 
);
"""
class Category(models.Model):
    name = models.CharField(max_length = 255)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model): # django database 
    name = models.CharField(max_length=255)
    price = models.FloatField(default = 0)
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField(default = True)
    category = models.ForeignKey( Category, on_delete = models.CASCADE)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price':self.price,
            'description': self.description,
            'count':self.count,
            'is_active':self.is_active,
            'category': self.category.to_json()
        }



