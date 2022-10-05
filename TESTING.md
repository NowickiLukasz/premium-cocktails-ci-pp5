# Testing
# Table of Content
- [Validation](#validation)
    - HTML
    - CSS
    - Python
    - JavaScript
    - Lighthouse
- [Testing User Stories](#testing-user-stories)
- [Manual Testing](#manual-testing)
    - Navigation Bar
    - Footer
    - Home Page
    - Register
    - Log-in/ Log out
- [Products](#product)
    - Shop Page
    - Products Page
    - Product Details Page
    - Product Reviews
    - Basket Page
    - Checkout Page
    - Profile Page
    - Shop Management
- [Contact Us](#contact-us)
- [Newsletter](#newsletter)
- [Social Links](#social-links)


## Validation
- HTML

    <details>
    <summary> Shop Page</summary>
    <img src="testing-images/validation/html/shop-page.png">
    </details>
    <br>

    <details>
    <summary> Register Page</summary>
    <img src="testing-images/validation/html/register-page.png">
    </details>
    <br>
    
    <details>
    <summary> Recipes List Page</summary>
    <img src="testing-images/validation/html/recipes-list-page.png">
    </details>
    <br>

    <details>
    <summary> Products Page</summary>
    <img src="testing-images/validation/html/products-page.png">
    </details>
    <br>
    
    <details>
    <summary> Products Details Page</summary>
    <img src="testing-images/validation/html/products-details-page.png">
    </details>
    <br>

    <details>
    <summary> Login/out Page</summary>
    <img src="testing-images/validation/html/login-page.png">
    </details>
    <br>

    <details>
    <summary> Home Page</summary>
    <img src="testing-images/validation/html/home-page.png">
    </details>
    <br>
 
    <details>
    <summary> Contact Us Page</summary>
    <img src="testing-images/validation/html/contact-us-page.png">
    </details>
    <br>

    <details>
    <summary> Cocktail List Page</summary>
    <img src="testing-images/validation/html/cocktails-list-page.png">
    </details>
    <br>

    <details>
    <summary> Books List Page</summary>
    <img src="testing-images/validation/html/books-list-page.png">
    </details>
    <br>
 
    <details>
    <summary> Basket Page</summary>
    <img src="testing-images/validation/html/basket-page.png">
    </details>
    <br>
 
- CSS
    <details>
    <summary>CSS</summary>
    <img src="testing-images/validation/css/css-validation.png">
    </details>
    <br>

- Python

    - Python testing was done throught the use of pep8 complience with the GitPod workspace. 


        [Autopep8](https://pypi.org/project/autopep8/) was used to aid in the validation of the code. 

        Each python file created by the user has been checked and adjusted manualy via the <br>
        <code>$ autopep8 --in-place --aggressive --aggressive filename</code> command. 

        For each of the files, the command realigns and formats the entire file to conform with PEP8 rules.

- JavaScript
    <details>
    <summary>Country Fields</summary>
    <img src="testing-images/validation/js/country-field-validation.png">
    </details>
    <br>

    <details>
    <summary>Stripe</summary>
    <img src="testing-images/validation/js/stripe-elements-validation.png">
    </details>
    <br>

- LightHouse

    <details>
    <summary>Homepage</summary>
    <img src="testing-images/lighthouse/homepage-desktop.png">
    </details>
    <br>

    <details>
    <summary>Shop Page</summary>
    <img src="testing-images/lighthouse/shop-desktop.png">
    </details>
    <br>

    <details>
    <summary>Product List</summary>
    <img src="testing-images/lighthouse/product-list-desktop.png">
    </details>
    <br>

    <details>
    <summary>Product Details</summary>
    <img src="testing-images/lighthouse/product-details-desktop.png">
    </details>
    <br>

    <details>
    <summary>Contact Us</summary>
    <img src="">
    </details>
    <br>

    <details>
    <summary>Newsletter</summary>
    <img src="testing-images/lighthouse/newsletter-desktop.png">
    </details>
    <br>

    <details>
    <summary>Basket</summary>
    <img src="testing-images/lighthouse/basket-desktop.png">
    </details>
    <br>

    <details>
    <summary>Checkout</summary>
    <img src="testing-images/lighthouse/checkout-desktop.png">
    </details>
    <br>
    


    

## Testing User Stories
- General
    - As a user I want to be able to uderstand that the page is for, once the home page loads. 
    <!-- Home page image -->
    <img src="testing-images/home-page.png">

    - As a user, once i visit the shop page, I can view what categories are there. 
    <!-- Shop main imd -->
    <img src="testing-images/shop-page.png">

    - As a user I can search for selling items, view the basket or head to the home page.
    <!-- Navigation -->
    <img src="testing-images/navigation.png">

    - As a User I want to be able to sign up to a newsletter
    <!-- Newsletter footer -->
    <img src="testing-images/footer.png">


- Basket
    - As a user I want to be able to view the items added to the basket. 
    <!-- Basket items -->
    <img src="testing-images/basket.png">

    - As a user I want to be able to view the total price of the items that i am about to purchase.
    <!-- Total items price -->
    <img src="testing-images/basket-total.png">

    - As a user, I want to be able to view the basket items once an item has been added to the basket.
    <!-- Basket drop down -->
    <img src="testing-images/basket-pop-up.png">

    - As a user I want to be able to adjust item quantity before i commit to buying. 
    <!-- Adjust message and page -->
    <img src="testing-images/basket-quantity-adjust.png">


- Checkout
    - As a User i want to be able to view my billing details in the chekout page. 
    <!-- checkout page details -->
    <img src="testing-images/checkout-billing-details.png">

    - As a user I want to be able to view the total of the items i am about to purchase. 
    <!-- Totla purchase items -->
    <img src="testing-images/checkout-total.png">

    - As a user I want to be able to give my card details to the site so that my account can be charged. 
    <!-- Card details -->
    <img src="testing-images/checkout-card-details.png">

    - As a User I want to be able to view a confirmation details page once my purchase is completed. 
    <!-- Confirmatio page -->
    <img src="testing-images/checkout-confiramation.png">


- Contact Form
    - As a User i want to be let known if my form has not been filled out correctly. 
    <!-- Validation  -->
    <img src="testing-images/contact-us-validation.png">

    - AS a user I want to be shown a message once my form has been sent to the site owner. 
    <!-- Message once the form is sent -->
    <img src="testing-images/contact-us-message.png">

    - As an Admin, I want to be able to view the submitions from the users
    <!-- Admin view contact-us -->
    <img src="testing-images/contact-us-view-forms.png">


- Products
    - As a User I want to be able to view the books and drinks pages. 
    <!-- show books and drinks page -->
    <img src="testing-images/shop-page.png">

    - As a user i want to be able to add a quantity of a selected product to the basket.
    <!-- show the add to basket buttona dn quantity selector -->
    <img src="testing-images/products-quantity-selector.png">

    - As a user I want to be notified of the items that i ahev just added to the basket. 
    <!-- Add Basket notification  -->
    <img src="testing-images/products-added-to-basket.png">


- Profile
    - As a user i want to be able to view previous purchases if i have an account.
    <!-- Display previous purchases -->
    <img src="testing-images/profile-previous-purchases.png">

    - As a user I want my details to be filled out if I have an account on the site. 
    <!-- Details filled out -->
    <img src="testing-images/profile-details.png">


- Recipe
    As the site owner i want to be able to add a recipe to the site 
    <!-- recipe add page -->
    <img src="testing-images/recipe-method.png">

    - As a site owner i want to be able to add ingredients to the recipe that has been created.
    <!-- Ingredients -->
    <img src="testing-images/recipe-ing.png">

    - As the site owner i want to be able to edit a recipe on the site 
    <!-- recipe edit page -->
    <img src="testing-images/recipe-edit.png">

    - As the site owner i want to be able to remove a recipe from the site 
    <!-- recipe remove page -->
    <img src="testing-images/recipe-edit-delete.png">


## Manual Testing

### Navigation Bar
- Navigation bar buttons and links tested and worked correctly &check;
- Drop down sections of the navigation menu render correctly once the link is selected &check;
- Navigation logo "Premium Coktails" takes user back to lading page. &check;
- Navigation search bar allows the user to search for queries, and returns a page with related query &check;
- Searches that cannot return a valid query, inform the user of no products found &check;
- Basket button displays current value of the items selected for purchase and updates accordingly &check;


### Footer
- Contact Us page link works correctly and sends the user to the correct page &check;
- Newsletter link in the footer sends the user to newsletter page so the user may sign up &check;

### Home Page
- Viewing the home page the user is easily informed about what the site is about &check;
- The "Go to shop" button takes the user to the shop categories page &check;

### Register
- Register link in the navbar takes the user to the correct page &check;
- User may regiter for the site &check;
- Registration form validates each field, if a field is missed a message will notify the user. &check;
- Relative messages for the length, strength and how common the password is are displayed as neccesary &check;
- Once registration form is validated, an email is sent to the user &check;
- Link in the email is correct and validates the user, then sends the user to the log in page &check;


### Log-in/ Log out
- Log in page validates if not all of the fields are filled out. &check;
- Message shows if the fields filled out are incorrect &check;
- A User may log-in with their email and password &check;

- A user may log out by clicking on their account, which willtake them to the log out page &check;
- Once a user logs out they will be informed they have done so my a message on screen &check;

### Products 

#### Shop Page
- Each of the sections present on the shop page takes the user to the respective pages &check;
- Shop page contains links in the footer of the page to go to contact us and newsletter page &check;


#### Products Page
- Products page displays amount of prpoducts related in the category selected &check;
- Products page allows the user to sort products according to price or alphabet &check;
- Each product displayed, will take the user to the respective product detail page &check;


#### Product Details Page
- Admin is able to view the edit and delete links &check;
- Edit and Delete links work as expected &check;
- Item image and decription renders correctly &check;
- Item description renders ABV if the recipe has abv stated &check;
- User is able to select quantity of items to add to basket. &check;
- Buttons work correctly for adding quantity. &check;
- Add to basket button works correctly &check;
- message displays once item has been added to basket &check;
- Reviews are shown on the bottom of the screen &check;


#### Product Reviews
- Logged in users may leave a review on the products that you can buy &check;
- Any user may view left reviews. &check;
- Admin has the ability to delete a review that they deem to be vulgar or inappropriate. &check;
- A message appears to notify user that the review has been left &check;

#### Basket Page
- When a user adds an item to the basket a pop up message appears and shows the user what items area added. &check;
- The user may click on the basket icon in the naviagation header to acces the basket page &check;
- The user may access the full basket details by clicking the secure checkout button in the pop up basket message &check;
- The user may adjust the quantity of items on the basket page &check;
- The user may remove the items entirely from the basket &check;
- The user may go back to the shop page if they wish to buy more items &check;
- The subtotal will be shown near the secure check out button &check;
- The amount due for payment will change accodingly to items in the basket. &check;
- The user may procede to the payment page from the basket page &check;

#### Checkout Page
- When a user views this page, they can view the the items they are about to purchase &check;
- When a user is not registered. The user will need to fill out the shipping details. &check;
- When a user is registered, their shipping details fill be autofilled in &check;
- The user will be able to view the total the items will cost &check;
- The user will be able to fill out a card details section &check;
- The card details input will validate if the card number is not correct &check;
- If a user has no profile details saved yet, the user may choose to save the shipping details as their profile details &check;
- The user may complete a purchase &check;
- The user will be prompted with a loading screen when payment is processing &check;
- Once the payment is processed, the user will be shown a confirmation page &check;
- The user will be sent an email with their confirmation details. &check;

#### Profile Page
- A new user with an account may fill out their profile details. &check;
- A User with an account may update their profile details &check;
- A user with an account may view their previous purchases. &check;
- A user may select a previous purchase and view the details of a previous purchase. &check;

#### Shop Management
- The admin is taken to the correct page when a link is clicked on the drop down selection menu. &check;
- The admin can add a new product to sell &check;
- The admin can add a new recipe for the users to view &check;
- The form on the add recipe page valides correctly when all fields are filled out &check;
- The add image field works as correctly and adds a recipe image &check;
- The delete recipe button works correctly and removes a recipe &check;
- The edit button works correctly and allows the user to update the recipe &check;
- The create recipe button work correctly and allows the user to add a recipe &check;
- The add image field works as correctly and adds a product image &check;
- The delete recipe button works correctly and removes a product &check;
- The edit button works correctly and allows the user to update the product &check;
- The create recipe button work correctly and allows the user to add a product &check;


### Contact Us
- The contact us link in the footer takes the user to the contact form page &check;
- The form on the page validates correctly when all the fields are filled in &check;
- A message informs the user that they submited a contact form &check;


### Newsletter
- The newsletter link in the footer takes the user to the newsletter form page &check;
- The newsletter form validates when all of the fields are filled &check;
- A message informs the user that they signed up to a newsletter. &check;


### Social Links
- All social links take the user to a blank new page according to the link clicked &check;







