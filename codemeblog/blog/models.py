from django.db import models

class Ctegory(models.Model):
     tittle = models.CharField(max_length=255)
     slug = models.SlugField()
     
     class Meta:
         ordering = ('tittle',)
         verbase_name_plural = 'Categories'
         
         def __str__(self):
             return self.tittle
    

class post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICES_STATUS =(
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    
    category = models.Foreignkey(Category, related_name='posts', on_delete=models.CASCADE)
    tittle = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = model.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    class Meta:
        ('-created_at',)
        
    def __str__(self):
             return self.tittle
    
class Comment(models.Model):
    post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = model.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name