from django.db import models

ROL_CHOICES = [
        ('Manager', 'Manager'),
        ('Assistant', 'Assistant'),
        ('Doctor', 'Doctor'),
        ('Conditioning Coach', 'Conditioning Coach')
    ]

class TechnicalStaffManager(models.Manager):

    def get_technicalStaff(self):
        return super().get_queryset().all()

    def get_oldest_tecnicalStaff(self):
        return super().get_queryset().order_by('birthDate').first()

class TechnicalStaff(models.Model):
    objects=TechnicalStaffManager()
    
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField()
    nationality = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, choices=ROL_CHOICES)

    # Relationships
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        related_name='technicalStaff'
    )

    class Meta:
        db_table = "TechnicalStaff"