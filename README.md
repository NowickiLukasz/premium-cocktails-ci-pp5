The purpose of this site is to allow user to be able to view a selection of pre-made cocktails, books and recipes. The user, if they so choose, may have a choice of products to purchase via the on site payment portal.
If the user wishes, they may create an account, which will allow the user to view past purchases or leave a review on any of the products or recipes. 
The Site Consists of 2 main sections. 
First section is the purchasable products, books or bottled drinks. 
Second section is the recipes. The recipes for the scope of this project will be classic 3 ingredient drinks. 

## Live Link 
This is the [live link](https://premium-cocktails.herokuapp.com/) for the site

# Table of Contents
- [User Experirence(UX)](#user-experience-ux)
    - [User Stories](#user-stories)
    - [Site Owner](#site-owner)
- [Site Structure](#site-structure)
- [Database Models](#database-models)
- [WireFrames](#wireframes)
- [Site features](#site-features)
- [Business Model](#business-model)
- [SEO](#seo)
- [Marketing](#marketing)
- [Techonologies Used](#techonologies-used)
- [Future Features](#future-features)
- [Deployment]()
- [Credits]()

# User Experience (UX)
## User Stories
- As a new user 
    - I want to easily navigate throughout the site.
    - I want to understand the purpose of the site easily so that I can see what is offers me.
    - I want a clear layout of the site so that i can navigate easily.
    - I want the site to be responsive across all devices.

- As an unregistered user:

    - I want to be able to search and filter products easily and efficiently.
    - I want to be able to sort and view products according by price and name.
    - I want to be able to be able to view product detail so I can find information about priceand description.
    - I want to be able to complete the checkout process and be able to enter payment information easily.
    - I want to be able to view a confirmation of my order once the checkout process is complete.
    - I want to be able to received an email confirmation of my order. -- mebe
    - I want to be able to read reviews from previous users of the product.
    - I want to be able to register easily for an account.
    - I want to be able to add products to my shopping basket.
    - I want to be able to view my shopping basket.
    - I want to be able to edit my shopping basket.
    - I want to be able to remove items from my shopping basket.
    - I want to be able to view the total amount of my basket.
    - I want to be able to see instructions appear to notify me if I have succeeded in purchasing a product etc.
    - I want to be able to send a message to the company if I have any queries
    - I want to be able to sign up to a news letter from the company to be able to receive updates on products.
    
- As a registered user:

    - I want to be able to receive a confirmation email upon registration.
    - I want to be able to access my account.
    - I want to be able to edit information on my account.
    - I want to be able to view my order history.
    - I want to be able to login and logout.
    - I want to be able to leave, edit and delete reviews on products.
    - I want to be able to see instructions appear to notify me if I have succeeded in posting a comment or review etc.
    - I want to be able to add products to my shopping basket.
    - I want to be able to view my shopping basket.
    - I want to be able to edit my shopping basket.
    - I want to be able to remove items from my shopping basket.

- As a reccurign user:

    - I want to be able to find social media links.
    - I want to be able to contact the site owner.

## Site Owner
- As a site owner:

    - I want to be able to add new products.
    - I want to be able to edit or delete products.
    - I want to be able to edit or delete recipes.
    - I want to be able to access the Django admin portal easily

# Site Structure
This project has been designed with multiple applications for the ease of manipulation of data and a logical approach to building the site with the Django framework. 

- Home
    - This app contains the information needed to allow the user to easliy browse through the site. 

- Products
    - This app contains all of the products that are sold on the site. The user may view each product, add a product to the basket and search for items ont the pages. 
    Each item on the page may be selected and the details of the item will be displayed, alongside any reviews that may have been left by previous buyers or previous consumers.
- Recipes 
    - This app allows the users to view a listing of recipes of popular mixed drinks. Once a recipe has been selected, it will display the recipe method and the ingredients needed to create the drink.

- Checkout
    - This app allows the user to purchase items they have selected. They may adjust the items quantity or remove entitrely if required. 

- Basket 
    - This app allows the user to view the selected items though their shopping experience.

- Profiles
    - This app allows the user to save their details so that the checkout app may prepoulate a shipping details form so that they may purchase products quicker. 

- Shop
    - This app allows the user to select a page they with to head to. They may choose to eaither go to pages they may purchase goods from or to view repices

- Contact form
    - This app allows the users to send a message to the site owner to let them know how they view their goods and what can be imporved with new products.

# Database Models
This is a database schema on the connection of the database models. 
<img src="readme-images/database/database-model.png">

# Wireframes

### Home Page
<details>
<img src="readme-images/wireframes/home.png">
</details>
<br>

### Shop Page
<details>
<img src="readme-images/wireframes/shop.png">
</details>
<br>

### Cocktail List Page

<details>
<img src="readme-images/wireframes/cocktail-list-page.png">
</details>
<br>

### Book List Page

<details>
<img src="readme-images/wireframes/book-list.png">
</details>
<br>

### Cocktail Details Page

<details>
<img src="readme-images/wireframes/cocktail-details-page.png">
</details>
<br>

### Book Details Page

<details>
<img src="readme-images/wireframes/book-details.png">
</details>
<br>

### Basket

<details>
<img src="readme-images/wireframes/basket.png">
</details>
<br>

### Checkout

<details>
<img src="readme-images/wireframes/checkout.png">
</details>
<br>

### Profile

<details>
<img src="readme-images/wireframes/profile.png">
</details>
<br>

# Site Features

## Navigation
<img src="readme-images/features/nav-bar.png">

The navigation section of the pages contains a logo, a search bar, link to view profile for regular user and additional fields for site admin and a basket button. 

The footer allows the user the contact the site owner or to signup to a site newsletter.

<img src="readme-images/features/account-button.png">

<img src="readme-images/features/footer.png">

## Products Pages

The initial page a user will view will be to allows them to select a category of product to view or recipes. 

<img src="readme-images/features/shop-page.png">
The user may select one of these and browse through items on the page. 

Items that may be purchased have a a sort function. 

<img src="readme-images/features/sort-function.png">
Site admin may edit or delete unwanted items on the site. 

<img src="readme-images/features/edit-delete.png">

## product details 

<img src="readme-images/features/product-details.png">
On this page a user may select a quantity of items they wish to purchase and add the items to the basket 

<img src="readme-images/features/quantity-selector.png">

## Register/ Log-in / Log-out

Here the a user may register for the site or if the user has an account they may login or out of the the site. 

<img src="readme-images/features/log-in.png">

## Review Page

A user is required to have an account set up and be logged in, in order to leave a review on a product that can be purchased.

<img src="testing-images/review-log-in.png">

## Profile

Here the current logged in user may view their details and view their previous purchase history 

<img src="readme-images/features/profile-page.png">

## Basket Page

A user of the site that has added items to the basket may adjust the items they have selected. 

They may remove all items if necessary

The user may then proceed to the checkout page to finalise their purchase. 

<img src="readme-images/features/shopping-basket.png">

## Checkout

A user may enter their delivery details on the form provided or if they have an account registered, the details will be filled out.

The user must fill out a card detail form which, once filled out will permit the user to purchase the items selcted

<img src="readme-images/features/checkout.png">

## Confirmation 

A user will be taken to the confirmation page once the purchase has been made. 

<img src="readme-images/features/confirmation.png">

## Contact Us

The user will be able to fill out a form with their details and a message to the site owner. 

<img src="readme-images/features/contact-us.png">

# Business Model

This project is designed for the use of cocktail enthusiasts where they can buy drinks, study material and view recipes. 
The business model is a Business to Customer(B2C). 

# SEO
To imporve the SEO for search engines, keywords and description was user in the HTML meta head section. 
The images have related names to what users would search for while looking for drinks. One such name is "porn-star-martini", which is one of the most cocktails in the world. 

<img src="readme-images/features/seo.png">

# Marketing
## Facebook Page
To allow the span of the business to be broader than just a website, there will be a dedicated Facebook page. 

A broad layout of the viable site is vivible in the below image. 

<details>
<img src="readme-images/facebook-mockup.png">
</details>
<br>


# Techonologies Used
## Dependencies
- asgiref==3.5.2
- backports.zoneinfo==0.2.1
- boto3==1.24.72
- botocore==1.27.72
- dj-database-url==0.5.0
- Django==3.2
- django-allauth==0.41.0
- django-countries==7.3.2
- django-crispy-forms==1.14.0
- django-storages==1.13.1
- gunicorn==20.1.0
- jmespath==1.0.1
- oauthlib==3.2.0
- pathspec==0.10.1
- Pillow==9.2.0
- psycopg2-binary==2.9.3
- python3-openid==3.2.0
- pytz==2022.2.1
- requests-oauthlib==1.3.1
- s3transfer==0.6.0
- sqlparse==0.4.2
- stripe==4.1.0

## Technologies
- [Django](https://www.djangoproject.com/) - Project Framework
- [Heroku](https://id.heroku.com/login) - Deployed site server
- [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Styling for the site
- [Git Hub](https://github.com/) - Repository for storing code
- [Git](https://git-scm.com/) - An open source distributed version control system
- [Git Pod](https://gitpod.io/) - An IDE for code creation
- [HTML Validator](https://validator.w3.org/) - Used for validating HTML code
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - Used for validating CSS code
- [JSHint](https://jshint.com/) - Used for validating JavaScript code
- [AWS](https://aws.amazon.com/) - For static file hosting
- [Balsamiq](https://balsamiq.com/) - For drawing wireframes for the project
- [FontAwesome](https://fontawesome.com/v5/docs/) - For icons on the website

## Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5) - Markup language for content creation
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Styling language
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - For dynamic features on the site
- [Python3](https://www.python.org/) - Used to provide logic to the project




# Future Features
- Ability to ask the user to be age verified at the entry to the site as of the sales of alcohol. 
- Ability for the site owner to reply derectly to contact us forms from the site
- Ability to send mass emails to all newsletter subscriber
- Allow for dynamic addition of extra ingredients in the recipe 
- Allow for a search feature for ingredient names in a drop down format

# bugs through work 
1. Images would not load. 
- found that i needed to have an if statement to load images if there was no image loaded for a certain item the page qould crash


2. Needs to be fixed 
- header section is very tall

3. Sorting function would not work throught te development. 
- Had to place the category into the products view rather than the shop one


# Deployment

## Setting up the Workspace:

1. Install Django with version 3.2:
    * ```pip install django3.2 ```
2. Install gunicorn:
    * ```pip install gunicorn```
3. Install supporting libraries:
    * ```pip install dj_database_url psycopg2```
4. Create requirements.txt:
    * ```pip freeze --local > requirements.txt```
5. Create an empty folder for your project in your chosen location.
6. Create a project in the above folder:
    * django-admin startproject <PROJECT_NAME> 
7. Create an app within the project:
    * ```python manage.py startapp APP_NAME``` 
8. Add a new app to the list of installed apps in setting.py
9. Migrate changes: 
    * ```python manage.py migrate```
10. Test server works locally: 
    * ```python manage.py runserver```  (You should see the default Django success page)
11. Run ```python3 manage.py createsuperuser``` to create a super/admin user
12. Run ```python3 manage.py loaddata db.json``` to load the database. 

## Create Heroku App:
The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.
1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
2. Give the app a unique name:
    * Will form part of the URL 
3. Select the nearest location:
    * For me, this was Europe.
4. Add Database to the Heroku app:
    * Navigate to the Resources tab of the app dashboard. Under the heading "Add ons," search for "Heroku Postgres" and click on it when it appears. 
    * Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
5. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.

## Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket named "premium-cocktails"
3. Uncheck the "Block All Public access setting"
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit
5. Enable the setting, and set the index.html and the error.html values
<br>![AWS Static](readme-images/aws-deployment-images/aws-static.png)

6. In the Permissions section, click edit on the CORS configuration and set the below configuration
<br>![AWS CORS](readme-images/aws-deployment-images/aws-cors.png)

7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)
<br>![AWS Bucket Policy](readme-images/aws-deployment-images/aws-s3-bucket-policy.png)

8. In the permissions section, click edit on the Access control list(ACL)
9. Set Read access for the Bucket ACL for Everyone(Public Access)
10. The bucket is created, the next step is to open the IAM application to set up access
11. Create a new user group named "	manage-premium-cocktails"
12. Add the "AmazonS3FullAccess" policy permission for the user group
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource" to the following
<br><code>"Resource": [</code>
<br><code>" "arn:aws:s3:::premium-cocktails",</code>
<br><code>" "arn:aws:s3:::premium-cocktails/*"</code>
<br><code>]</code>

16. Give the policy a name and click "Create Policy"
17. Add the newly created policy to the user group
<br>![AWS Bucket Policy](readme-images/aws-deployment-images/aws-user-policy.png)

18. Go to Users and create a new user
19. Add the user to the user group manage-scubasport
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup

22. The user is now created with the correct user group and policy
<br>![AWS Bucket Policy](readme-images/aws-deployment-images/aws-user-policy.png)

23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage
<br>![AWS Settings](readme-images/aws-deployment-images/aws-settings.png)

24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files 


## Google emails
To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
2. Turn on 2-step verification and follow the steps to enable
3. Click on app passwords, select Other as the app and give the password a name, for example Django
<br>![App password](readme-images/emails/email-pass.png)

4. Click create and a 16 digit password will be generated, note the password down
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
7. Set and confirm the following values in the settings.py file to successfully send emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>

8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

## Local Deployment


# Credits

- Cocktail images - https://www.punch.com
- Cocktail books - https://www.cocktailkingdon.com
- Cocktail bottles  - https://www.cosmopolitan.com/uk/worklife/g37664570/best-bottled-cocktails/
