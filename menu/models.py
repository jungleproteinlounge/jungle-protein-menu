from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=240, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name_plural = "categorías"
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    name = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    price_cop = models.PositiveIntegerField(null=True, blank=True, help_text="Precio en pesos colombianos, sin puntos ni símbolo. Déjalo vacío si está por confirmar.")
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    sort_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    class Meta:
        ordering = ["sort_order", "name"]
        constraints = [models.UniqueConstraint(fields=["category", "name"], name="unique_product_per_category")]
    def __str__(self):
        return self.name
