from time import time_ns

from django.db import models
from django.core.validators import MinLengthValidator
from computedfields.models import ComputedFieldsModel, computed


class Student(ComputedFieldsModel):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    registration_number = models.PositiveBigIntegerField()
    gender = models.CharField(max_length=6, choices=GENDERS)
    date_of_admission = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)  # brings more precision than a datefield
    last_updated_on = models.DateTimeField(auto_now=True)  # brings more precision than a datefield

    @computed(models.CharField(max_length=22, primary_key=True), depends=[['self', ['first_name', 'last_name']]])
    def id(self):
        if not self.pk:
            return f'{self.first_name[0]}{self.last_name[0]}{time_ns()}'
        return self.pk

    def __str__(self):

        return self.id

    class Meta:

        db_table = 'students'
