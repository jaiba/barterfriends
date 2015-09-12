from django.db import models
from django.contrib.auth.models import Group, User

class Collaboration(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user_owner = models.ForeignKey(User)
    group_owner = models.ForeignKey(Group)
    creator = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        history = CollaborationHistory()
        history.collaboration_id = self.id
        history.previous_user_owner = self.user_owner
        history.previous_group_owner = self.group_owner

        super(Collaboration, self).save(*args, **kwargs)

        history.new_user_owner = self.user_owner
        history.new_group_owner = self.group_owner
        history.save()

    def __str__(self):
        return self.name

class CollaborationHistory(models.Model):
    collaboration_id = models.ForeignKey(Collaboration)
    previous_user_owner = models.IntegerField()
    new_user_owner = models.IntegerField()
    previous_group_owner = models.IntegerField()
    new_group_owner = models.IntegerField()
