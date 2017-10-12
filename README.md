library-system

1.Dependencies

	Django all-auth
	Crispy-from-tags
	python2.7
	Django 1.11.6


2. ./install.sh to install all the dependencies, run the server and populate the database. Put this url in chrome http://127.0.0.1:8000/

3. library-system
		
			bookstore (APP)
				migrations
				templates
					account
						login.html
						logout.html
						signout.html
					base.html
					checkout.html
					home.html
					product.html
                    thankyou.html
				_init_.py
				admin.py
				apps.py
				models.py
				tests.py
				urls.py
				views.py

			librarySystem
				_init_.py
				settings.py
				urls.py
				wsgi.py

			static
				images
				javascript(js files)
				styles(css files)

			manage.py


4. python version is 2.7 and Django Version is 1.11.6

5. Functionality of website(BookStore):

	1. Go to the given url.
	2. According to the category select the book.
	3. If you will checkout you have to login.
	4. After that you will be redirected to checkout page.
	5. New user can signup also.
	6. From any page you can directly go to the home page.
	7. Also after logout you will be directed to the home page.


6. There are 3 main files:

	viewes.py
		home()
		product()
		checkout()
                final()

	urls.py
		home/
		product/
		checkout/
		checkout/final/

	models.py
		Book


7. For user authentication Django all-auth package. Put all the dependeices in settings.py and you will be able to signup, login , logout. taken reference from - https://github.com/pennersr/django-allauth, http://django-allauth.readthedocs.io/en/latest/installation.html.

8. In install.sh command "python manage.py migrate" to populate the database. 

9. I referred following links:
	https://docs.djangoproject.com/en/1.11/
	https://v4-alpha.getbootstrap.com
	https://www.youtube.com/watch?v=9Wbfk16jEOk&t=9268s
	https://github.com/pennersr/django-allauth

	

