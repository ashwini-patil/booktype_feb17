# This file is part of Booktype.
# Copyright (c) 2012 Aleksandar Erkalovic <aleksandar.erkalovic@sourcefabric.org>
#
# Booktype is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Booktype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Booktype.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *
#from django.conf.urls import patterns, include , url

urlpatterns = patterns('',
    url(r'^$', 'booki.account.views.view_accounts', name='view_accounts'),

#Added this path for transcripts    
    url(r'^todays_transcript/$', 'booki.account.views.todays_transcript', name='todays_transcript'),
    url(r'^newexplain/$', 'booki.account.views.newexplain', name='newexplain'),
    url(r'^slide1/$', 'booki.account.views.slide1', name='slide1'),
    url(r'^interact/$', 'booki.account.views.interact', name='interact'),
    url(r'^explain/$', 'booki.account.views.explain', name='explain'),
    url(r'^question/$', 'booki.account.views.question', name='question'),
    url(r'^summary/$', 'booki.account.views.summary', name='summary'),
  # url(r'^default/$', 'booki.account.views.default', name='default'),
    url(r'^hello/$', 'booki.account.views.hello', name='hello'),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^signin/$', 'booki.account.views.signin', name='signin'),  
    url(r'^login/$', 'booki.account.views.signin', name='login'),  
    url(r'^forgot_password/$', 'booki.account.views.forgotpassword', name='forgotpassword'),  
    url(r'^forgot_password/enter/$', 'booki.account.views.forgotpasswordenter', name='forgotpasswordenter'),  

    url(r'^signout/$', 'booki.account.views.signout', name='signout'),  

# to be removed                       
#    url(r'^register/$', 'booki.account.views.register', name='register'),

    # Username
    # Letters, digits and @/./+/-/_ only.
    # For now, even space.                       

    url(r'^(?P<username>[\w\d\@\.\+\-\_\s]+)/$', 'booki.account.views.view_profile', name='view_profile'),

    url(r'^(?P<username>[\w\d\@\.\+\-\_\s]+)/_create_book/$', 'booki.account.views.create_book', name='create_book'),
    url(r'^(?P<username>[\w\d\@\.\+\-\_\s]+)/_create_group/$', 'booki.account.views.create_group', name='create_group'),
    url(r'^(?P<username>[\w\d\@\.\+\-\_\s]+)/_import_book/$', 'booki.account.views.import_book', name='import_book'),

 #url(r'^(?P<username>[\w\d\@\.\+\-\_\s]+)/_todays-transcript/$', 'booki.account.views.todays-transcript', name='todays-transcript'),

   url(r'^(?P<username>[\w\d\@\.\+\-\_\s]+)/_/$', 'booki.account.views.create_book', name='create_book'),

   url(r'^(?P<username>[\w\d\@\.\+\-\_\s]+)/_save_settings/$', 'booki.account.views.save_settings', name='save_settings')
)
