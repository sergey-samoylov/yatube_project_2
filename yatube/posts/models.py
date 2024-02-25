from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

"""
в каждом объекте модели User автоматически будет создано свойство с таким же названием (posts), и в нём будут храниться ссылки на все объекты модели Post, которые ссылаются на объект User.
На практике это означает, что в объекте записи есть поле author, в котором хранится ссылка на автора (например, на пользователя admin), а в объекте пользователя admin появилось поле posts, в котором хранятся ссылки на все посты этого автора. И теперь можно получить список постов автора, обратившись к его свойству posts.
"""
