from django.db import models

class Product(models.Model):
    product_id      = models.AutoField(primary_key=True)
    product_name    = models.CharField(max_length=50)
    product_desc    = models.CharField(max_length=300)
    product_price   = models.IntegerField(default= 0)
    product_flavour = models.CharField(max_length=50, default="")
    product_image   = models.ImageField(upload_to="shop/images", default="")
    pub_date        = models.DateTimeField()

    def __str__(self):
        return self.product_name