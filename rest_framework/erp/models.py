class Product(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    name     = models.CharField(max_length=255)
    code     = models.CharField(max_length=100, null=True)
    price    = models.FloatField()
    supplier = models.ForeignKey('Supplier', null=True)
    image    = models.ImageField(upload_to='product')

    def __unicode__(self):
        return "{0}".format(self.code, )

class ProductItem(models.Model):

    product = models.ForeignKey('Product', related_name="product_item")
    code    = models.CharField(max_length=255)
    ean13   = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0}".format(self.code, )

class Supplier(models.Model):

    name = models.CharField(max_length=255)
 
    def __unicode__(self):
        return "{0}".format(self.name, )
