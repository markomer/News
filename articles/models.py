# from django.db import models
# from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models



class Section(models.Model):
  name = models.CharField(max_length=96)
  description = models.TextField()

  def __str__(self):
    return self.name


class Article(models.Model):
  title = models.CharField(max_length=128)

  body = models.TextField()
  author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE)
  created_on = models.DateTimeField()


# class Post(models.Model):
#   title = models.CharField(max_length=256)
#   author = models.ForeignKey(
#     'auth.User',
#     on_delete=models.CASCADE
#     )
#   body = models.TextField()
#   created_on = models.DateTimeField(
#     auto_now_add=True
#     )

#   def __str__(self):
#     return self.title

#   def get_absolute_url(self):
#     return reverse('post_detail', args=[self.id])
# ----------------------------
#    class UserType(models.Model):
#      name = models.CharField(max_length=128)
#      description = models.TextField()
#
#      def __str__(3self):
#        return self.name
#
#
#    class Language(models.Model):
#      key = models.CharField(max_length=4)
#      name = models.CharField(max_length=128)
#
#      def __str__(self):
#        return self.name