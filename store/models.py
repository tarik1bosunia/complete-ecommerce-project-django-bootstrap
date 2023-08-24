from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="img/products", blank=True, null=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ('-created_at',)

    @property
    def discount_percentage(self):
        try:
            return int((self.regular_price - self.selling_price) * 100 / self.regular_price)
        except ZeroDivisionError:
            return 0

    # def get_url(self):
    #     return reverse('product_details', args=[self.category.slug, self.slug])
    #
    # def __str__(self):
    #     return self.product_name
    #
    # def averageReview(self):
    #     reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
    #     avg = 0
    #     if reviews['average'] is not None:
    #         avg = float(reviews['average'])
    #     return avg
    #
    # def countReview(self):
    #     reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
    #     count = 0
    #     if reviews['count'] is not None:
    #         count = int(reviews['count'])
    #     return count