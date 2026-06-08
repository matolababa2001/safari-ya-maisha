from django.db import models
from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('neno', 'Neno la Mungu'),
    ('lishe', 'Tiba Lishe'),
    ('ndoa', 'Mahusiano ya Ndoa'),
)

class Post(models.Model):

    CATEGORY_CHOICES = (
        ('neno','Neno la Mungu'),
        ('lishe','Tiba Lishe'),
        ('ndoa','Mahusiano ya Ndoa'),
    )

    title = models.CharField(max_length=255)
    title_en = models.CharField ( max_length=255 , blank=True , null=True )

    content = models.TextField(blank=True)
    content_en = models.TextField ( blank=True , null=True )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    audio = models.FileField(
        upload_to='audio/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    likes = models.ManyToManyField (
        settings.AUTH_USER_MODEL ,
        blank=True ,
        related_name='liked_posts'
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
