# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import *


class BlogTestCase(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User

        self.john = User.objects.create(username='john', email='john@lennon.com')
        self.george = User.objects.create(username='george', email='george@mail.com')
        self.fan = User.objects.create(username='fan', email='fan@yahoo.com')

        self.jblog = Blog.objects.create(user=self.john)

    def test_read_marks_deletion(self):
        self.jblog.subscribers.add(self.fan, self.george)

        post = self.jblog.posts.create(title='Post 1', text='Всем привет!')
        post.read_by.add(self.fan, self.george)
        self.assertEqual(post.read_by.count(), 2)

        self.jblog.subscribers.remove(self.george)
        self.assertEqual(post.read_by.count(), 1)

        self.assertEqual(PostReadBy.objects.filter(post=post, user=self.george).count(), 0)
        self.assertEqual(PostReadBy.objects.filter(post=post, user=self.fan).count(), 1)

    def test_send_emails_to_subscribers(self):
        from django.core import mail

        self.assertEqual(len(mail.outbox), 0)

        self.jblog.subscribers.add(self.fan, self.george)
        post = self.jblog.posts.create(title='Post 1', text='Всем привет!')
        self.assertEqual(len(mail.outbox), 2)
        
