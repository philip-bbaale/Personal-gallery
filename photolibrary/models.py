from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=50)

    def save_location(self):
        self.save()

    def delete_location(self):
        Location.objects.filter(pk=self.id).delete()

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length =50)

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter(pk=self.id).delete()

    def __str__(self):
        return self.category


class Pictures(models.Model):
    image = models.ImageField(upload_to = 'img/', blank=False)
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
    image_category = models.ManyToManyField(Category, related_name='posts')
    image_location = models.ForeignKey(Location, related_name='posts', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @classmethod
    def search_by_category(cls,search_term):
        search_picture = cls.objects.filter(image_category__category__icontains=search_term)
        return search_picture

    def save_picture(self):
        self.save()

    def delete_picture(self):
        Pictures.objects.all.filter(pk=self.id).delete()

    def __str__(self):
        return self.image_name
