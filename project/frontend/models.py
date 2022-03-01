from django.db import models
from project.settings import MEDIA_ROOT
import os

class CustomManager(models.Manager):
    def delete(self):
        for obj in self.get_queryset():
            obj.delete()

class Audio(models.Model):
    audioid = models.AutoField(primary_key=True)
    audio = models.FileField()  
    freqwrd = models.TextField()
    tnscript = models.CharField(max_length=255)
    diraize = models.FileField()
    duration = models.FileField() 
    nospeaker = models.PositiveIntegerField(null=True)
    
    objects = CustomManager() # just add this line of code inside of your model

    def delete(self, using=None, keep_parents=False):
        if self.audio:
            if os.path.exists(self.audio.path):
                os.remove(self.audio.path)
        if self.diraize:
            if os.path.exists(self.diraize.path):
                os.remove(self.diraize.path)
        if self.duration:
            if os.path.exists(self.duration.path):
                os.remove(self.duration.path)
        super().delete()


class Speaker(models.Model):
    spid = models.AutoField(primary_key=True)
    audioid = models.ForeignKey(Audio, on_delete= models.CASCADE)
    sp_audio = models.FileField()
    sp_emo = models.FileField()
    sp_emobar = models.FileField()

    objects = CustomManager() # just add this line of code inside of your model

    def delete(self, using=None, keep_parents=False):
        if self.sp_audio:
            if os.path.exists(self.sp_audio.path):
                os.remove(self.sp_audio.path)
        if self.sp_emo:
            if os.path.exists(self.sp_emo.path):
                os.remove(self.sp_emo.path)
        if self.sp_emobar:
            if os.path.exists(self.sp_emobar.path):
                os.remove(self.sp_emobar.path)
        super().delete()