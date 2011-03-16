from django.db import models

# Create your models here.

class Blog(models.Model):

	title = models.CharField(max_length=256)
	post_date = models.DateTimeField('Post Date')
	reply_to = models.EmailField('Reply To')
	content = models.TextField()

	def __str__(self):
		return "Blog(title = '%s')"%(self.title)

	def rating(self):
		#@To Do : Rating Calcuation
		return None

#	def __unicode__(self):
#       	return self.title

	RATING_CHOICES = (
		 (1 , 'Lame'),
		 (2 , 'Weak'),
		 (3 , 'OK'),
		 (4 , 'Nice'),
		 (5 , 'Rocks'),
		 )

class Comment(models.Model):

	in_reference_to = models.ForeignKey(Blog)
	content = models.TextField(max_length=256)
	rating = models.IntegerField(choices=Blog.RATING_CHOICES)

	def __str__(self):
		return "Comment(content = '%s', rating = %s)"% (self.content, str(self.rating))

	def ratingText(self):
		return Blog.RATING_CHOICES[self.rating-1][1]




