from django.db import models

class Tag(models.Model):

    name = models.CharField(max_length=10)
    button_contents = models.TextField(blank=True)
    color = models.CharField(max_length = 7, default="#337ab7")
    id = models.SlugField(max_length=10, primary_key=True)

    def count(self):
        projects = Project.objects.filter(tags__id=self.id)
        codes = code.objects.filter(tags__id=self.id)
        return projects.count() + codes.count()

    def __str__(self):
        return self.name

class Project(models.Model):

    Source = ( ('<i class="icon-gamemaker"></i> <span class="network-name">Get source as GM</span></a>' , 'GM'),
               ('<i class="fa fa-github fa-fw"></i> <span class="network-name">Get source on Github</span></a>',
                'GITHUB'),
               ('<i class="fa fa-file-archive-o fa-fw"></i> <span class="network-name">Get source as ZIP</span></a>',
                'ZIP'))

    name = models.CharField(max_length=20)
    info = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateField()
    featured = models.BooleanField()
    in_development = models.BooleanField()
    image = models.CharField(max_length=200)
    tags =  models.ManyToManyField('Tag')
    source_type = models.CharField(choices=Source, max_length=200)
    source_url = models.CharField(max_length=200)
    download_url = models.CharField(max_length=200, blank=True)
    preview_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class codeGroup(models.Model):

    id = models.SlugField(primary_key=True,unique=True,max_length=10)
    featured = models.BooleanField()
    name = models.CharField(max_length = 20)
    info = models.CharField(max_length=50)
    source = models.URLField(blank=True)
    c = []
    date = models.DateField()

    def codes(self):
        c =  code.objects.filter(group__id = self.id)
        return c

    def __str__(self):
        return self.name

class code(models.Model):

    id = models.SlugField(primary_key=True,unique=True,max_length=10)
    name = models.CharField(max_length=20)
    suffix = models.CharField(max_length=4)
    tags =  models.ManyToManyField('Tag')
    description = models.TextField(blank = True)
    source = models.URLField()
    group = models.ForeignKey('codeGroup')


    def __str__(self):
        return self.name




