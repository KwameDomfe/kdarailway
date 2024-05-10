from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse


""" Categories and Sub Categories Start"""
# Categories Model
class Category(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length =128)

    slug=models.SlugField(
        blank=True,
        null=True )

    description=models.TextField(
        max_length=512,
        blank=True,
        null=True )

    thumbnail=models.FileField(
        blank=True,
        )

    is_active=models.BooleanField(
        default=True)

    created=models.DateTimeField(
        auto_now_add=True)

    updated=models.DateTimeField(
        auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['created','updated','name',]
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)

def category_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        instance.slug = slugify(instance.name)

pre_save.connect(category_pre_save, sender = Category)

def category_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        instance.slug = slugify(instance.name)
        instance.save()

post_save.connect(category_post_save, sender = Category)

# Families Model
class Family(models.Model):
    
    id=models.AutoField(
        primary_key=True)

    category=models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True)

    name=models.CharField(
        'Sub Category Name',
        max_length=128)

    slug=models.SlugField(
        blank=True,
        null=True )

    description=models.TextField(
        'Sub Category Description',
        max_length=512,
        null=True)

    thumbnail=models.FileField(
        blank=True)

    pub_date=models.DateField(
        'Date Published', 
        auto_now=True,
        blank= True, 
        null=True)

    is_active=models.BooleanField(
        default=True)

    created_at=models.DateTimeField(
        'Date Created',
        auto_now_add=True,
        blank= True, 
        null=True)

    class Meta:
        verbose_name_plural = 'Families'
        ordering = ['id']

    def __str__(self):
        return self.name

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg)

# Types Model
class Type(models.Model):

    id=models.AutoField(
        primary_key=True)

    family=models.ForeignKey(
        Family, 
        on_delete=models.SET_NULL, 
        null=True)

    name=models.CharField(
        'Sub Category Name',
        max_length=128)

    slug=models.SlugField(
        blank=True,
        null=True )

    description=models.TextField(
        'Sub Category Description',
        max_length=512,
        null=True)

    thumbnail=models.FileField(
        blank=True)

    pub_date=models.DateField(
        'Date Published', 
        auto_now=True,
        blank= True, 
        null=True)

    is_active=models.BooleanField(
        default=True)

    created_at=models.DateTimeField(
        'Date Created',
        auto_now_add=True,
        blank= True, 
        null=True)

    class Meta:
        verbose_name_plural = 'Families'
        ordering = ['id']

    def __str__(self):
        return self.name

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg)

""" Categories and Sub Categories End"""