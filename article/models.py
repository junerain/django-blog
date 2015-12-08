# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model) :
    title = models.CharField(max_length = 100)  #������Ŀ
    category = models.CharField(max_length = 50, blank = True)  #���ͱ�ǩ
    date_time = models.DateTimeField(auto_now_add = True)  #��������
    content = models.TextField(blank = True, null = True)  #������������

    def __unicode__(self) :
        return self.title
 #��ȡURL��ת����url�ı�ʾ��ʽ
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
    
    class Meta:  #��ʱ���½�����
        ordering = ['-date_time']