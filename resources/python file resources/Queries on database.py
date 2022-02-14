'''One to Many Relationship

1) See the reviews of the project.
>>> p = Project.objects.get(title = 'Ecommerce Web Application')
>>> p   
<Project: Ecommerce Web Application>
>>> p.review_set.all()
<QuerySet [<Review: up>, <Review: down>]>
>>> p.review_set.all()
<QuerySet []>


2)Add the new review into the Project

>>> p.review_set.create(body ='Nice',value='up')
<Review: up>
>>> p
My Portfolio
>>> p.review_set.all()
<QuerySet [<Review: up>]>

Another Method:
>>> p = Project.objects.get(title = 'Ecommerce Web Application')
>>> Review.objects.create(project = p,body='Next Level Project',value='up')
<Review: up>
>>> p.review_set.all()
<QuerySet [<Review: down>, <Review: up>, <Review: up>]>

3) Get the project and update the review 
>>> p = Project.objects.get(title = 'Ecommerce Web Application')
>>> p   
<Project: Ecommerce Web Application>
>>> p.review_set.all()
<QuerySet [<Review: up>, <Review: down>]>
>>> p.review_set.get(value='up')
<Review: up>
>>> r1 = p.review_set.get(value='up') 
>>> 
>>>
>>> r1.body = 'very good and nice'
>>> r1.save()
>>> r1
<Review: up>

4)Delete the review of the particular project

>>> r1.delete()
(1, {'projects.Review': 1})
>>> r1
<Review: up>
>>> p = Project.objects.get(title='Ecommerce Web Application')
>>> p.review_set.all()
<QuerySet [<Review: down>]>

Many to Many Relationship (Project and Tags)
1)Adding tags to single Project.
>>> p = Project.objects.get(title = 'Ecommerce Web Application') 
>>> t = Tag.objects.create(name = 'HTML5')
>>> p.tags.add(t)
>>> p.tags.all()
<QuerySet [<Tag: ROR>, <Tag: JavaScript>, <Tag: PHP>, <Tag: HTML5>]>

	Adding another tag
>>> t1 = Tag.objects.create(name = 'CSS3')
>>> p.tags.add(t1)
>>> p.tags.all()
<QuerySet [<Tag: ROR>, <Tag: JavaScript>, <Tag: PHP>, <Tag: HTML5>, <Tag: CSS3>]>

Get All the Projects:
>>> p =Project.objects.all()
>>> p
<QuerySet [<Project: Ecommerce Web Application>, <Project: Chat Application>, <Project: My Portfolio>]>

Searching for a Particular Project.

>>> p = Project.objects.get(title = 'Chat Application')
>>> p
<Project: Chat Application>


To get the List of Projects that matches the condition

>>> p = Project.objects.filter(title__contains = 'a') 
>>> p
<QuerySet [<Project: Ecommerce Web Application>, <Project: Chat Application>]>


>>> p = Project.objects.filter(title__icontains = 'my') 
>>> p
<QuerySet [<Project: My Portfolio>]>


>>> p = Project.objects.filter(title__startswith = 'my') 
>>> p
<QuerySet [<Project: My Portfolio>]>


>>> p = Project.objects.filter(vote_total__gt=100)
>>> p
<QuerySet [<Project: Ecommerce Web Application>]>

Working with dates:

>>> from django.utils import timezone 
>>> p = Project.objects.filter(created__lt=timezone.now())
>>> p
<QuerySet [<Project: Ecommerce Web Application>, <Project: Chat Application>, <Project: My Portfolio>]>
	

>>> p = Project.objects.filter(created__gt = '2022-1-20') 
D:\pythonProjects\venv\lib\site-packages\django\db\models\fields\__init__.py:1409: RuntimeWarning: DateTimeField Project.created received a naive datetime (2022-01-20 00:00:00) while time zone support is active.
  warnings.warn("DateTimeField %s received a naive datetime (%s)"
>>> p
<QuerySet [<Project: My Portfolio>]>


>>> p = Project.objects.filter(created__gt = '2022-1-20 05:20') 
D:\pythonProjects\venv\lib\site-packages\django\db\models\fields\__init__.py:1409: RuntimeWarning: DateTimeField Project.created received a naive datetime (2022-01-20 05:20:00) while time zone support is active.
  warnings.warn("DateTimeField %s received a naive datetime (%s)"
>>> p
<QuerySet [<Project: My Portfolio>]>


using exclude attribute

>>> p = Project.objects.exclude(title__icontains = 'a')
>>> p
<QuerySet [<Project: My Portfolio>]>


using order_by attribute 
>>> p = Project.objects.all().order_by('title') 
>>> p
<QuerySet [<Project: Chat Application>, <Project: Ecommerce Web Application>, <Project: My Portfolio>]>

descending order
>>> p = Project.objects.all().order_by('-title') 
>>> p
<QuerySet [<Project: My Portfolio>, <Project: Ecommerce Web Application>, <Project: Chat Application>]>

Sorting based on two columns
>> p = Project.objects.all().order_by('vote_total','title')       
>>> p
<QuerySet [<Project: Chat Application>, <Project: Hospital Management System>, <Project: My Portfolio>, <Project: Ecommerce Web Application>]>
>>> p[0].vote_total
50
>>> p[1].vote_total 
100
>>> p[2].vote_total 
100
>>>
'''