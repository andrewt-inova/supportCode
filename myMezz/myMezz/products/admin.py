from django.contrib import admin
from products.models import Product
from products.models import FAQ
from products.models import ProductSuite

# Register your models here.
class prodSuiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'product_suite')
    
    fieldsets = [
        (None,                  {'fields' : ['name','description']}),
        ('Product Associations',{'fields' : ['product_type','product_suite']})
    ]

class faqAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)
    
    fieldsets = [
        (None,                  {'fields': ['question','answer']}),
        ('Associated Products', {'fields': ['products']})
    ]
    
    list_display = ('question', 'answer')
    
    
admin.site.register(ProductSuite, prodSuiteAdmin)
admin.site.register(Product, productAdmin)
admin.site.register(FAQ, faqAdmin)