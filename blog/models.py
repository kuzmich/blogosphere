# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver


class Blog(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='пользователь')
    name = models.CharField('название', max_length=150)
    subscribers = models.ManyToManyField('auth.User',
                                         related_name='subscriptions',
                                         verbose_name='подписчики',
                                         blank=True)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return '{0.name} ({0.user})'.format(self)

class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts', verbose_name='блог')
    title = models.CharField('заголовок', max_length=100)
    text = models.TextField('содержание')
    created = models.DateTimeField('создан', auto_now_add=True)
    read_by = models.ManyToManyField('auth.User',
                                     related_name='read_posts',
                                     verbose_name='прочитано пользователями',
                                     blank=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return '{0.title} ({0.blog})'.format(self)


Subscriptions = Blog.subscribers.through
PostReadBy = Post.read_by.through


@receiver(m2m_changed, sender=Subscriptions)
def subscribers_changed(sender, **kwargs):
    if kwargs['action'] == 'post_remove':
        users = kwargs['pk_set']
        blog = kwargs['instance']
        PostReadBy.objects.filter(post__in=blog.posts.all(), user__in=users).delete()

@receiver(post_save, sender=Post)
def new_post_created(sender, **kwargs):
    from django.core.mail import send_mail

    if kwargs['created']:
        post = kwargs['instance']
        blog = post.blog

        for subscriber in blog.subscribers.exclude(email=''):
            send_mail('В блоге {} новая публикая: {}'.format(blog, post.title),
                      post.text,
                      from_email='news@blogosphere.com',
                      recipient_list=[subscriber.email])


