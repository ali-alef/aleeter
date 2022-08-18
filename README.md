# aleeter

this project is like twitter but better

## blog App
  * models:
    * Post: it should have a title and content and author
  * Views:
    * postView: this view is the home page and shows all of the posts and it is paginated and if the number of posts are more than 4 it will create another page for showing the rest of the posts
    * postDetailView: this will show a post separate in a page
    * postDeleteView: this view is for deleting a post and it only let you update a post if the user that is logged in was created that post (test_func)
    * postCreateView: this view is for creating a post and before checking the validation it will set author the user that is logged in 
    * postUpdateView: this view is for updating a post and it only let you update a post if the user that is logged in was created that post (test_func)
    
## user App   
  * models:
    * Profile: each profile is for one user and it has image for that user you can change the image in '/admin' or it will use the defualt
  * views: 
    * register: this view is for register 
    * profile: this view is for showing profile and you can see this view if you are logged in
    * for the login and logout views i used the defualt django views
    
## superuser info
**username**: ali\
**password**: Passw0rd$96

(or you can create a new superuser by `python manage.py createsuperuser`)
