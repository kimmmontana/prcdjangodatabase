import random
import string
from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    PersonalID = models.CharField(primary_key=True, max_length=6, default="")
    Surname = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100, null=True)
    Maiden_surname = models.CharField(max_length=50, null=True)
    Housenum = models.CharField(max_length=50)
    Village = models.CharField(max_length=50, null=True)
    Barangay = models.CharField(max_length=50)
    Municipality = models.CharField(max_length=50)
    Province = models.CharField(max_length=50)
    Rurban_code = models.CharField(max_length=6)
    SEX_CHOICES = [('M', 'M'), ('F', 'F')]
    Sex = models.CharField(max_length=1, choices= SEX_CHOICES)
    Citizenship = models.CharField(max_length=50)
    Contact_number = models.CharField(max_length=11)
    Email_address = models.EmailField(max_length=100)
    Civil_Stat = models.CharField(max_length=11)
    Birthdate = models.DateField()
    Birthplace = models.CharField(max_length=50)
    Birth_rurban_code = models.CharField(max_length=6)
    Spouse_name = models.CharField(max_length=50, null=True)
    Spouse_citizenship = models.CharField(max_length=50, null=True)
    Father_name = models.CharField(max_length=50, null=True)
    Father_citizenship = models.CharField(max_length=50, null=True)
    Mother_name = models.CharField(max_length=50, null=True)
    Mother_citizenship = models.CharField(max_length=50, null=True)
    BEEN_CONVICTED_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    Been_convicted = models.CharField(max_length=3, choices=BEEN_CONVICTED_CHOICES, verbose_name="Have Been Convicted?")

    def __str__(self):
         return self.Email_address

    def save(self, *args, **kwargs):
        if not self.PersonalID:
            self.PersonalID = self.generate_random_id()
        super().save(*args, **kwargs)

    def generate_random_id(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(6))
    
class ExamHistory(models.Model):
    Exam_num = models.CharField(primary_key=True, max_length=8, default="")
    PersonalID = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    Exam_name = models.CharField(max_length=50)
    EXAM_PLACE_CHOICES = [
        ('Manila', 'Manila'),
        ('Baguio', 'Baguio'),
        ('Cebu', 'Cebu'),
        ('Davao', 'Davao'),
    ]
    exam_place = models.CharField(max_length=10, choices=EXAM_PLACE_CHOICES)
    Date_Taken = models.DateField()
    exam_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    EXAM_RESULT_CHOICES = [
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
        ('Conditioned', 'Conditioned'),
        ]
    exam_result = models.CharField(max_length=50, null=True, choices=EXAM_RESULT_CHOICES)
    Rev_center = models.CharField(max_length=100, null=True)
    
    

    def save(self, *args, **kwargs):
        if not self.Exam_num:
            self.Exam_num = self.generate_random_id()
        super().save(*args, **kwargs)

    def generate_random_id(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

class Application(models.Model):
    application_id = models.CharField(primary_key=True, max_length=6, default="")
    Exam_num = models.ForeignKey(ExamHistory, on_delete=models.CASCADE)
    PersonalID = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    Exam_name = models.CharField(max_length=50)
    
    
    APPLICATION_STAT_CHOICES = [
        ('First Timer', 'First Timer'),
        ('Repeater', 'Repeater'),
        ('Conditioned', 'Conditioned'),
        ('Absent', 'Absent'),
    ]
    Application_stat = models.CharField(max_length=20, choices=APPLICATION_STAT_CHOICES)

    PREV_EXAMINEE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    Prev_examinee = models.CharField(max_length=3, choices=PREV_EXAMINEE_CHOICES, verbose_name="Previous Examinee?")

    def save(self, *args, **kwargs):
        if not self.application_id:
            self.application_id = self.generate_random_id()
        super().save(*args, **kwargs)

    def generate_random_id(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

class EducationInfo(models.Model):
    Educ_ID = models.CharField(primary_key=True, max_length=5, default="")
    PersonalID = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    PRC_sc = models.CharField(verbose_name = 'PRC School Code', max_length=4)
    School_name = models.CharField(max_length=100)
    School_add = models.CharField(max_length=255)
    PRC_cc = models.CharField(verbose_name = 'PRC Course Code', max_length=4)
    Degree_Course = models.CharField(max_length=100)
    Grad_date = models.DateField()
    PRC_bc = models.CharField(verbose_name = 'PRC Board Code', max_length=4)

    def save(self, *args, **kwargs):
        if not self.Educ_ID:
            self.Educ_ID = self.generate_random_id()
        super().save(*args, **kwargs)

    def generate_random_id(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(6))
    
