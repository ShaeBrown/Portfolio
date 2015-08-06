from django.db import models

class Tag(models.Model):


    name = models.CharField(max_length=10)
    button_contents = models.TextField(blank=True)
    color = models.CharField(max_length = 7, default="#337ab7")


    def __str__(self):
        return self.name

class Project(models.Model):

    Source = ( ('<i class="icon-gamemaker"></i> <span class="network-name">Get source as GMK</span></a>' , 'GMK'),
               ('<i class="fa fa-github fa-fw"></i> <span class="network-name">Get source on Github</span></a>','GITHUB'))

    name = models.CharField(max_length=20)
    info = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateField()
    featured = models.BooleanField()
    in_development = models.BooleanField()
    image = models.CharField(max_length=200)
    tags =  models.ManyToManyField('Tag')
    source_type = models.CharField(choices=Source, max_length=200)
    source_url = models.URLField()
    download_url = models.URLField(blank = True)

    def __str__(self):
        return self.name

