from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Wholefood(models.Model):
    
    class WholefoodObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(max_length=200, unique=True)
    image = models.URLField()
    serving_size_grams = models.IntegerField()
    energy_per_serve_kj = models.IntegerField()
    protein_per_serve = models.IntegerField()
    carbs_per_serve = models.IntegerField()
    fat_per_serve = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=options, default='published')
    is_archived = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)
    objects = models.Manager() # default manager
    wholefood_objects = WholefoodObjects() # custom manager

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class WholefoodFeedback(models.Model):
    wholefood = models.ForeignKey(
        'Wholefood',
        on_delete=models.CASCADE,
        related_name='wholefood_feedback'
    )
    feedback = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='authored_wf_feedback'
    )

class AlternativeWholefoodName(models.Model):
    name = models.CharField(max_length=200)
    associated_wholefood = models.ForeignKey(
        'Wholefood',
        on_delete=models.CASCADE,
        related_name='alternative_wholefood_names'
    )