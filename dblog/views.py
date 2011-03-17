# Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response ,get_object_or_404
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dblog.models import Blog ,Comment

import datetime


def index(request):
     '''Generate the context for the main summary page'''
     print "In Index...."
	
     latest_blog_list = Blog.objects.all().order_by('-post_date')
     return render_to_response('dblog/index.html',{'latest_blog_list': latest_blog_list})

def readblog(request, blog_id):
    p = get_object_or_404(Blog, pk=blog_id)
    return render_to_response('dblog/readblog.html', {'blog': p},context_instance=RequestContext(request))

def comment(request, blog_id):
    """ To view the comments related to Blog
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    return render_to_response('dblog/comment.html',{'comments': blog.comment_set.all(),'blog': blog})

def addComment(request, blog_id):
    """Generate the context for the form in which new
	comments are entered"""
    blog = get_object_or_404(Blog, pk=blog_id)
    return render_to_response('dblog/addComment.html', {'blog': blog},context_instance=RequestContext(request))


def postComment(request, blog_id):
	
	"""Accepts the HTTP POST data of a new blog comment
       and updates the database accordingly"""
	
	blog = get_object_or_404(Blog, pk=blog_id)
	if request.POST['content']:	
		comment = blog.comment_set.create(content=request.POST['content'], rating=request.POST['rating'])
		comment.save()
		return HttpResponseRedirect(reverse('dblog.views.comment', args=(blog.id,)))
	else:
		  return HttpResponse('Please Add Some Comment')

def writeBlog(request):
	return render_to_response('dblog/blogEntry.html',context_instance=RequestContext(request))

def postEntry(request):
	'''Accepts the HTTP POST data of a new blog entry and
	updates the database accordingly'''
	b = Blog()
	b.title = request.POST['title']
	b.reply_to = request.POST['reply_to']
	b.content = request.POST['content']
	b.post_date = datetime.datetime.now()
	b.save()
	return HttpResponseRedirect('/blog/%s/' % b.id)
