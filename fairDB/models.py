from django.contrib.auth.models import User
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Score(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sustainability_score = models.FloatField()
    human_rights_score = models.FloatField()
    origin_score = models.FloatField()
    overall_score = models.FloatField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Score for {self.product.name}"


class Certification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.certification_name} for {self.product.name}"


class UserReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"
