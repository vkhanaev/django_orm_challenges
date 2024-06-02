from enum import Enum

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author_full_name = models.CharField(max_length=256)
    isbn = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Brand(models.TextChoices):
    APPLE = 'Apple', 'Apple'
    DELL = 'Dell', 'Dell'
    HP = 'HP', 'HP'
    LENOVO = 'Lenovo', 'Lenovo'
    ASUS = 'Asus', 'Asus'
    ACER = 'Acer', 'Acer'
    MICROSOFT = 'Microsoft', 'Microsoft'
    SAMSUNG = 'Samsung', 'Samsung'
    MSI = 'MSI', 'MSI'


class Laptop(models.Model):
    brand = models.CharField(max_length=50, choices=Brand.choices)
    year_of_release = models.IntegerField()
    ram_size = models.PositiveIntegerField(help_text="RAM size in GB")
    hdd_size = models.PositiveIntegerField(help_text="HDD size in GB")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Laptop(brand:{self.brand}, "
                f"year_of_release:{self.year_of_release}, "
                f"ram_size:{self.ram_size}, "
                f"hdd_size:{self.hdd_size}, "
                f"price:{self.price}), "
                f"stock_quantity:{self.stock_quantity}, "
                f"date_added:{self.date_added}")


class Status(models.TextChoices):
    PUBLISHED = 'PUBLISHED', 'Опубликован'
    UNPUBLISHED = 'UNPUBLISHED', 'Не опубликован'
    BANNED = 'BANNED', 'Забанен'


class Category(models.TextChoices):
    TECHNOLOGY = 'TECHNOLOGY', 'Технологии'
    HEALTH = 'HEALTH', 'Здоровье'
    EDUCATION = 'EDUCATION', 'Образование'
    ENTERTAINMENT = 'ENTERTAINMENT', 'Развлечения'
    TRAVEL = 'TRAVEL', 'Путешествия'


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.UNPUBLISHED,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        blank=True,
        null=True
    )

    def __str__(self):
        return (f"BlogPost(title:{self.title}, "
                f"text:{self.text}, "
                f"author:{self.author}, "
                f"status:{self.status}, "
                f"creation_date:{self.creation_date}), "
                f"publication_date:{self.publication_date}, "
                f"category:{self.category}")
