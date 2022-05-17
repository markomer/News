
Heroku Link (not successfully built completely):
https://dashboard.heroku.com/apps/mighty-brushlands-37650




1. Create a Section model that consists of "name" and "description".
2. Create an Article model that consits of the following:
  2.1 title
  2.2 author -> this should be a foreign key to "CustomUser"
  2.3 body
  2.4 created_on
  2.5 section -> This should be a foreign key to "Section".
3. Create a blank migration to populate the "Section" model.
4. Run migrations
5. Register models on admin panel.
6. Login via admin panel to visually confirm changes.

## Note:
class Message(models.Model):
  title = models.CharField(max_length=128)
  body = models.TextField()
  author = ForeignKey(
    get_user_model(),
  )

## Note 2 :
Suggestions for sections: "Frontpage", Sports", "Society", "Business", etc

name: "Sports"
description: "Articles realteing to sporting events"


Submit your full news app with the following criteria:

1. Must be able to sign up.

2. Must be able to reset my password (emails sent via sendgrid).

3. Must be able to change my password.

4. Must support multiple users plus admin.

5. Must display news articles in a list view.

6. Must be possible to create, view, update and delete articles.

7. Non-registered users cannot create, update or delete articles (only view).

8. Submission must be github link but also include a heroku URL in the README.