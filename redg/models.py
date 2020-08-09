from django.db import models

from taggit.managers import TaggableManager
# Create your models here.

class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	comment_content = models.TextField()
	# TODO
	author = models.TextField()
	voting_score = models.IntegerField(default=0)

class CommentThread(models.Model):
	id = models.AutoField(primary_key=True)
	comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.PROTECT)

class Finding(models.Model):
	id = models.AutoField(primary_key=True)
	comment_thread = models.ForeignKey(CommentThread, on_delete=models.CASCADE, null=True, blank=True)
	finding_url = models.URLField(max_length=200, default="")
	finding_name = models.CharField(max_length=100, default="")
	finding_description = models.CharField(max_length=100, default="")
	finding_date = models.DateTimeField('Published on', null=True, blank=True)
	finding_voting_score = models.IntegerField(default=0)
	finding_tags = TaggableManager()
	finding_image = models.ImageField(upload_to ='uploads/', blank=True) 

	def __str__(self):
		return str(self.finding_name)