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

class Requirement (models.Model):
    
    RAM_CHOICES = {
        ('1 GB', '1 GB'),
        ('2 GB', '2 GB'),
        ('4 GB', '4 GB'),
        ('8 GB', '8 GB'),
        ('16 GB', '16 GB')
    }
    
    processor = models.CharField(max_length=200)
    os = models.CharField(max_length=200, verbose_name='OS')
    ram = models.CharField(verbose_name='RAM', max_length='4', choices=RAM_CHOICES, default='2 GB')
    hard_disk = models.IntegerField(verbose_name='Hard Disk Space', max_length=4, help_text='Enter the number of GB of free space required for the product')
    network = models.TextField(verbose_name='Network Requirements', max_length=200)
    other = models.TextField(verbose_name='Special Considerations', max_length=200)
    product = models.OneToOneField(ProductSuite, verbose_name="Product Suite")
    
    def __unicode__(self):
        return "%s Requirements" %self.product.name
    
    class Meta:
        ordering = ('product',)
