from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from email.policy import default

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
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
    candidate_image=models.ImageField(blank=True,null=True)
    vote_count= models.IntegerField(default=0)
    def __str__(self):
        return self.candidate_name

def upload_path(instance,filename):
    return '/'.join(['covers',str(instance.title),filename])
class Imagerec(models.Model):
    title=models.CharField(max_length=32,blank=False)
    cover=models.ImageField(blank=True,null=True,upload_to=upload_path)

class Vote(models.Model):
    election_foreign=models.ForeignKey(Election,on_delete=models.CASCADE,null=True,blank=True)
    candidate_foreign=models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Vote - {self.candidate_foreign.candidate_name}"
    
    
class UserDetail(models.Model):
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    actual_name=models.CharField(max_length=200,blank=True,null=True)
    mobile_number=models.CharField(max_length=200,blank=True,null=True)
    voters_id=models.CharField(max_length=100,blank=True,null=True)
    adhar_number=models.CharField(max_length=100,blank=True,null=True)
    pan_number=models.CharField(max_length=100,blank=True,null=True)
    user_image=models.ImageField(upload_to='user_images',blank=True,null=True)
    def __str__(self):
        return(self.actual_name)    

# class Userdetail(models.Model):
#     email = models.EmailField(max_length=255, unique=True)
#     username=models.CharField(max_length=255,unique=True,null=True)
#     voters_id = models.CharField(max_length=20,null=True)
#     aadhaar_number = models.CharField(max_length=12,null=True)
#     user_img = models.ImageField(blank=True,null=True)
