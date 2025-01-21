from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Micronutrient(models.Model):

    class MicronutrientObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    CATEGORY_CHOICES = (
        ("V", "Vitamin"),
        ("M", "Mineral"),
        ("TrE", "Trace element"),
        ("Ph", "Phytonutrient"),
        ("O", "Other"),
    )
    category = models.CharField(
        max_length=3,
        choices = CATEGORY_CHOICES,
        default = "O",
        )
    name = models.CharField(max_length=200, unique=True)
    supplement_sources = models.CharField(max_length=800, blank=True)
    contraindications = models.CharField(max_length=800, blank=True)
    cofactors = models.CharField(max_length=800, blank=True)
    benefits = models.CharField(max_length=800)
    toxicity_symptoms = models.CharField(max_length=800)
    dosage_unit = models.CharField(max_length=200)
    upper_limit = models.IntegerField(blank=True, null=True)
    therapeutic_dose = models.IntegerField(blank=True, null=True)
    rdi = models.IntegerField(blank=True, null=True)
    est_av_req = models.IntegerField(blank=True, null=True)
    adequate_intake = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='published')
    is_archived=models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)
    objects = models.Manager() # default manager
    micronutrient_objects = MicronutrientObjects() # custom manager

    class Meta:
        ordering = ('name',)

    def __str__(self):
            return self.name

class NutrientFeedback(models.Model):
    nutrient = models.ForeignKey(
        'Micronutrient',
        on_delete=models.CASCADE,
        related_name='nutrient_feedback'
    )
    feedback = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='authored_nut_feedback'
    )

class AlternativeNutrientName(models.Model):
    name = models.CharField(max_length=200)
    associated_nutrient = models.ForeignKey(
        'Micronutrient',
        on_delete=models.CASCADE,
        related_name='alternative_nutrient_names'
    )