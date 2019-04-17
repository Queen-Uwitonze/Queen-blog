from django.db import models


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

    # def delete_images(self):
    #   self.remove()
    
    # def update_images(self):
    #   self.remove()
    
    # def get_image_by_id(id):
    #   pass
     
    # def search_results(images):
    #   pass
    
    # def filter_by_location(request,location_id):
    #   pass
    # class Meta:
    #     ordering = ['images_name']