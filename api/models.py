from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from email.policy import default

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,username=None,password=None,voters_id=None,aadhaar_number=None,user_img=None,**extra_fields):
        

        if email is None:
            raise TypeError("Users should have a email")
        if password is None:
            raise TypeError("Users should have a password")
        if aadhaar_number is None:
            raise TypeError("Users should have a adhar number")
        if user_img is None:
            raise TypeError("Users should have a user_img")

        

        user=self.model(email=self.normalize_email(email),username=username,voters_id=voters_id,aadhaar_number=aadhaar_number,user_img=user_img,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True,db_index=True)
    username=models.CharField(max_length=255,unique=True,db_index=True,null=True)
    voters_id = models.CharField(max_length=20,null=True)
    aadhaar_number = models.CharField(max_length=12,null=True)
    user_img = models.ImageField(upload_to='user_photos', blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['voters_id', 'aadhaar_number']

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        return ''

  

class Election(models.Model):
    election_name=models.CharField(max_length=100)
    election_date=models.DateField()
    def __str__(self):
        return self.election_name
    
class Candidate(models.Model):
    candidate_name=models.CharField(max_length=100)
    party=models.CharField(max_length=50)
    election=models.ForeignKey(Election,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.candidate_name

def upload_path(instance,filename):
    return '/'.join(['covers',str(instance.title),filename])
class Imagerec(models.Model):
    title=models.CharField(max_length=32,blank=False)
    cover=models.ImageField(blank=True,null=True,upload_to=upload_path)