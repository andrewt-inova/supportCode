from django.db import models

# Create your models here.
class ProductSuite(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Product(models.Model):
    TYPE_CHOICES = (('SW','Software'),('HW','Hardware'))
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    product_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    product_suite = models.ForeignKey(ProductSuite, null=True)
    
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
    
class FAQ (models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=1000)
    products = models.ManyToManyField(Product)

    def __unicode__(self):
        return self.question
    
    class Meta:
        ordering = ('question',)
        
