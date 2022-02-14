from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

def createProfile(sender,instance,created,**kwarg):
    if created:
        userobj = instance
        Profile.objects.create(
            user = userobj,
            name=userobj.username,
            username = userobj.username,
            email = userobj.email,
        )
        print('Same record created in Profile')
    
#@receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    try:
        user = instance
        user.delete()
        print('User also got deleted')
    except:
        print('user already deleted')
    

post_delete.connect(deleteUser,sender=Profile)
post_save.connect(createProfile,sender=User)