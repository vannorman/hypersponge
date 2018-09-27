from django.conf.urls import *

import hypersponge.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hypersponge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', hypersponge.views.home),
	url(r'^blog/$', hypersponge.views.blog_base), 
	url(r'^base/$', hypersponge.views.simple_page('base.html')), 
	url(r'^resume/$', hypersponge.views.simple_page('resume.html')), 
	url(r'^portfolio/$', hypersponge.views.simple_page('portfolio.html')), 
	url(r'^address/$', hypersponge.views.simple_page('address.html')), 
	url(r'^blog/(.*)/$', hypersponge.views.blog), 
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', hypersponge.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', hypersponge.views.file_b),


	url(r'^messages/whatyouwant$', hypersponge.views.simple_page('messages/isthiswhatyouwant.html')), 




]
