from django.db import models


class Company(models.Model):
    name = models.CharField(verbose_name='company name', max_length=20)
    ricCode = models.CharField(max_length=20)


class CompanyInfo(models.Model):
    esg_score = models.CharField(max_length=20)
    social = models.CharField(max_length=20)
    governance = models.CharField(max_length=20)
    comparisson_and_rank = models.CharField(max_length=20)
    company = models.OneToOneField(Company, related_name='company_info', on_delete=models.CASCADE)
