from django.contrib.auth.models import User
from django.db import models
from django_extensions.admin.filter import NotNullFieldListFilter


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    barcode = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    score = models.ForeignKey('Score', on_delete=models.CASCADE)
    reviews = models.ForeignKey('UserReview', on_delete=models.CASCADE, null=True)

    def update_average_rating(self):
        ratings = UserReview.objects.filter(product=self)
        if ratings:
            avg_rating = sum(r.rating for r in ratings) / len(ratings)
            return avg_rating
        return 0

    def average_rating(self):
        reviews = UserReview.objects.filter(product=self)
        if not reviews:
            return 0
        total_rating = sum(review.rating for review in reviews)
        average = total_rating / len(reviews)
        return round(average)

    def gold_stars(self):
        return self.average_rating()

    def gray_stars(self):
        return 5 - self.average_rating()


class Score(models.Model):
    sustainability_score = models.FloatField()
    human_rights_score = models.FloatField()
    origin_score = models.FloatField()
    overall_score = models.FloatField()
    review_date = models.DateField(auto_now_add=True)


class Certification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.certification_name} for {self.product.name}"


class UserReview(models.Model):
    rating = models.IntegerField()
