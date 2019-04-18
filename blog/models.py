from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author= models.CharField(max_length =60)
    blog =models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length =200)
    description = models.CharField(max_length =500)
    date =models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
      return self.title

    @classmethod
    def get_posts(cls,post_id):
        posts = Post.objects.get(id=post_id)
        return posts     

    @classmethod
    def get_all_posts(cls,id):
            posts = Post.objects.all()
            return posts 
        
    
    def save_posts(self):
        self.save()

    def delete_Posts(self):
      self.remove()
    
    def update_images(self):
      self.remove()
    
    def get_post_by_id(id):
      pass
     
    # def search_results(images):
    #   pass
    
    # def filter_by_location(request,location_id):
    #   pass
    # class Meta:
    #     ordering = ['images_name']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=30)
    prof_image = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)
    

    def __str__(self):
        return self.name



    # def delete_profile(self):
    #     self.delete()

    @classmethod
    def get_profile(cls):
        profile = cls.objects.get()
        return profile
    
    def update_profile(self,bio):
        self.profile = profile
        self.save()
        
    # @classmethod
    # def search_by_name(cls,search_term):
    #     profile = cls.objects.filter(name__icontains=search_term)
    #     return profile

class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
    
    def update_comment(self):
       self.remove()
        
    def delete_comment(self):
        self.delete()

class Like(models.Model):
    likes= models.IntegerField(default=0)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='messages_received')

    def __str__(self):
        return self.likes

class SubscriptionForm(models.Model):
    email = models.EmailField()
 