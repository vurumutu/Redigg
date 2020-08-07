from django.db import models

# Create your models here.

class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	comment_content = models.TextField()
	# TODO
	author = models.TextField()
	voting_score = models.IntegerField(default=0)

class CommentThread(models.Model):
	id = models.AutoField(primary_key=True)
	comment = models.ForeignKey(Comment, on_delete=models.PROTECT)

class Finding(models.Model):
	id = models.AutoField(primary_key=True)
	comment_thread = models.ForeignKey(CommentThread, on_delete=models.CASCADE, default="Null")
	finding_name = models.CharField(max_length=100, default="")
	finding_date = models.DateTimeField('Published on', null=True, blank=True)
	voting_score = models.IntegerField(default=0)