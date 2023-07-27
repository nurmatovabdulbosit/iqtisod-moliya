from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django.urls import reverse

STATUS = (
	('active','Chop_etildi'),
	('deactive','Qoralama')
)
# Create your models here.
class PublishMeneger(models.Manager): 
	def get_queryaet(self):
		return super().get_queryaet.filter(status='active')
	
	
class Post(models.Model):
	title = models.CharField(max_length=250, verbose_name='Sarlavha') 
	slug = AutoSlugField(populate_from="title")
	
	#charField bu sozlarni soni hisoblanadi
	body = models.TextField(verbose_name='Matn')  
	# bu ham text cheksiz
	photo = models.ImageField(upload_to='post_photo/%Y/%m/%d/', blank=True, null=True, verbose_name='Rasm')
	# bu rasmga yuklangan rasmlar qayerda joylashadi
	see = models.PositiveIntegerField(blank=True, null=True, verbose_name='Korishlar soni')
	publish = models.DateTimeField(default=timezone.now, verbose_name='Vaqti')
	status = models.CharField(max_length=100, choices=STATUS, verbose_name='Holati')
	
	create_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratish')
	update = models.DateTimeField(auto_now=True, verbose_name='Uzgartirish')
	create_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Muallif')
	
	objects = models.Manager()
	published = PublishMeneger()
									  
	class Meta:
		ordering = ('-publish',)
									  
	def __str__(self):
		return self.title
	
	def get_absolute_url(self, id, slug):
		return reverse('post:post_detail', args=[self.id, self.slug])