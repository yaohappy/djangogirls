from django.shortcuts import render
from trips.models import Post
from datetime import datetime

# Create your views here.

def home(request): 
	# get all the posts
    post_list = Post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list})

def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})

def post_detail(request, idx):
    post = Post.objects.get(id=idx)
    return render(request, 'post.html', {'post': post})

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            posts = Post.objects.filter(location__icontains=q)
            return render(request, 'search_result.html',
                {'posts': posts, 'query': q})
    return render(request, 'search_form.html',
        {'errors': errors})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })