# FeedMe - Testing details

[Main README.md file](README.md)

[View website on Heroku](http://flask-feedme-project.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation](#validation)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)


## Automated Testing

### Validation

CSS - Validated using [Jigsaw](https://jigsaw.w3.org/css-validator/) with no errors found.

| Page | Test | 
--- | --- | 
style.css | PASS

HTML - Validated using [W3C](https://validator.w3.org/#validate_by_input) 

| Page | Test | 
--- | --- | 
base.html |PASS
index.html |PASS
recipe_1.html |PASS
recipe_2.html |PASS
recipe_3.html |PASS
recipe_4.html |PASS
site_recipes.html | PASS
your_recipes.html | PASS
feedme_recipe.html | PASS
recipe.html | PASS
add_recipe.html | PASS
edit_recipe.html | PASS
register.html | PASS
login.html | PASS
404.html | PASS

Javascript - Validated using [JSHint Validator](https://jshint.com/) with no errors found.

Python - Validated using [PEP 8](http://pep8online.com/) with no errors found.

## User Stories Testing

The following section goes through the user stories identified in the [Ux section of README.md](README.md#UX) to check that the site meets those needs.

**As a visitor to the FeedMe website I expect/want/need:**

1. **To be able to easily find the information I am looking for, the layout needs to make sense so that I am not put off.**
    - Arrangement of site elements such as navbar, footer, icons, and forms conform to expected placement.

1. **The site to be laid out in a way that is easy to navigate, so that I can find what I need.**
    - The navbar offers easy navigation for the user and is clearly labeled.
    - Icons and images are used to help the user digest information quickly.

1. **The site to be responsive and navigable for various device sizes; desktop, tablet, and phone. For the content to look good on all of the devices.**
    - The use of the site has been extensively tested on desktop, tablet and phone size screens.
    - The user can load the website on mobile, tablet, and desktop devices.
    - All elements have been given a responsive design, so nothing to too squashed, squeezed or hard to read on any screen size a user might be using.
    - The navbar has a collapsed menu for tablet and mobile viewing, this makes navigation easier for smaller devices.

1. **To be able to connect to FeedMe's social media accounts.**
    - The footer contains links to FeedMe's different social media accounts, including Facebook, Instagram, Pinterest, and Twitter. 

1. **To be able to click on recipes for further information about them.**
    - The recipe image can be clicked on for further information on each of the recipes.
    - The recipe contains the recipe name, recipe image, author, course type, time, servings, ingredients, directions, and notes. 

1. **To be able to add, edit, and delete recipes that I would like to share with others.**
    - The Add Recipes page allows users to add recipes that they would like to share with others, by filling in the form and submitting the information.
    - Members are able to edit their own recipe additions by clicking the edit button on the Your Recipe page or the full recipe page. The edit recipe page allows members to cancel or save their edited recipe information.
    - Members are able to delete their own recipe additions by clicking the delete button on the Your Recipe page or the full recipe page. This brings up a modal askng whether they are sure they want to delete this recipe, giving them the option to cancel or delete.

1. **To be able to search for recipes on the website using keywords.**
    - Users are able to search for recipes on the top of FeedMe Recipes page, within the search bar. 
    - If no recipes are found, the page will displaly 'No results found'. 

1. **To be able to log in and out with ease.**
    - Both log in and log out pages are displayed in the navbar, making it easy to do both functions.
    - The log in form is able to store your username and password if desired, making it easier and faster to log in.

1. **To be notified that I have logged in or out of my account.** 
    - When a member logs into their account, they are taken to their profile page, where a flash message displays 'Nice to see you again (Username)'.
    - When logged out, a flash message displays 'You have been logged out', and bringing them back to the log in page.

1. **To be notified about changes that are made, inlcluding adding, editing, and deleting recipes.**
    - Flash messages have been designed to notify members when any changes have been made.
    - When a member has added a recipe, a flash message displays 'Recipe successfully added'.
    - When a book has been edited, a flash message displays 'Recipe successfully updated'.
    - When a member deletes a recipe, a flash message displays 'Recipe successfully removed'.

## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

#### Elements on every page

1. Navbar 
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirm that when logged out the options "Register" and "Log in" are visible and that "Log out" is not.
    - Log into the site, confirm that "Log out" is visible and that "Register" and "Log in" are not.
    - Click the "Shop" link in the navbar, confirm that all sections of the shop are listed in the dropdown menu.
    - Add an item to the users cart, confirm that the grand total appears under the shopping cart icon with the correct grand total. 
    - Delete all items from the users cart, confirm that the grand total is no longer visible in the navbar.

2. Search bar
    - Enter a search word that applies to many items. 
        - Confirm that the items returned match the items. Confirm that the message "0 items found for (item)" is displayed when hitting enter.

3. Footer
    - Hover over links in the footer, confirm the animation works as expected.
    - Click all links in the footer, confirm that they take the user to the relevant pages within the site.
    - Click the social icons, confirm that they open a new tab and take the user to the correct page.
    - Check date of copyright information, confirm year displayed matches the current year.

#### Home Page

1. Carousel images
    - Click slider buttons, confirm that they work as expected.
    - Adjust width of browser window, confirm image is responsive.

2. On Sale section
    - Click on each of the items to ensure it takes the user to the correect item detail page.

3. Shop by pet
    - Hover over each of the buttons to ensure that the pet name display. 
    - Click each of the buttons to ensure the user is taken to the correct items display page. 

#### Pet pages

1. Types of items
    - Click tag buttons, confirm they work and go to the correct locations.
    - Click each of the dropdown links, confirm they go to the correct location. 
    - Click the All items link, confirm all items for that pet are displayed. 
    - Confirm that the image and prices displayed are correct.
    - Click multiple items, confirm that the user is taken to the correct items detail page.

2. Sorting options
    - Select the different sorting options from the menu one by one, confirm that the iteems are sorted in the orders selected.

#### On Sale Page

1. Prices 
    - Ensure that the original price is displayed in red, with a line through it. 
    - Ensure the on sale price is slightly bigger and is displayed in blue. 
    - Check that the on sale price is used when the item is added to the cart. 

#### Register Page

- Log out then go to the register page again. Confirm that the register form is displayed as expected.
- Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Fill in the form with two different passwords, confirm the error is caught again and the user is informed of their mistake.

#### Login Page

- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to the hoome page. 

#### Account Page

- Go to the account page of a newly created user. Confirm that te profile info form is populated with the users username and email address.
- Confirm that the first name and last name fields are also available.
- Fill in the form with a non-email address, confirm that the applicable error is shown to the user
- Fill in the form correctly, confirm that the "Your account info has been updated." message is shown to the user and that the reloaded form is now populated with the new data.
- Confirm that a user with no previous orders has the "no orders to show" text in the Orders section.
- Make 2 separate orders on the website. 
- Return to the account page, confirm that the orders are displayed in the Orders section of the account page. With the top order being the most recent and open to show the full details. Confirm that all orders after it in the list are closed accordions, but that can be opened with a click.
- Confirm that all data in the orders on the account page is accurate.
- Go into the admin panel, mark one of the orders as shipped. Confirm that the information to the user in their account page is updated to show that the order selected has been shipped.

#### Log Out Page

- Attempt to log out and ensure the the user is taken to the log out page, asking if they are sure they want to log out.
- Click cancel, and ensure tthat the user is redirected to the home page. 
- Log out and and ensure that the user is redirected to the home page. 

#### Cart Page

- Log in and go to the cart page with nothing in the cart. Confirm that the message "Your cart is empty!" is shown and the call to action button "Let's go shopping" is provided and that the checkout button is not displayed. 
- Click the button and confirm it takes the user to the all items page.
- Add items to the cart and return to the cart page, confirm that all items in the cart are displayed correctly, with the correct amounts requested by the user.
- Adjust the quantity field, confirm that the shopping cart subtotal is updated to reflect the change.
- Click the delete button on an item, confirm that the item removed from the cart.
- Delete all items from the cart, confirm that the cart is empty. 

#### Checkout Pages

- Go to the checkout page when not logged in to the site, confirm that the user is taken to the login page to sign in.
- Confirm that the items are displayed correctly in the order summary, that the quantity, subtotal, and grand total are correct
- Try to send the form without all the required fields filled in. Confirm that the appropriate error message is given to the user.
- Return to the payment page , use the stripe checkout test [card numbers](https://stripe.com/docs/testing) to check the various responses to different errors.
- Make a successful payment. Confirm that the user is returned to checkout success page.
- Check that the checkout success page loads all item and delivery information correctly. 

### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile and tablet specific elements on my Samsung phone and tablet, in both the firefox browser and samsung internet browser.

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar 
    - Open the website on mobile, confirm that the navbar is collapsed into a burger icon
    - click the burger icon, confirm that the navbar list appears are expected.
    - Add something to the cart, confirm that the user shopping cart grand total appears and displays correctly.

2. Footer
    - Scroll to the bottom of the page, confirm that the footer contents is displayed as expected with the bootstrap grid.
    - No content squashed or squeezed or disproportionate in size.
    - Confirm that all links and buttons in footer are easy to click with a finger on the smallest screen sizes.

3. Pet pages
    - Confirm that the item list is displayed one on top of each other on mobile, and 3 or 2 to a row on tablet, depending on its size.
    - Confirm that all clicks and swipes operate as expected on touch screen.

4. All pages
    - Navigate to all pages on the site, check that the layout is as expected for the screen size.
    - Check that all buttons, menus, forms and other elements are the correct proportions and easily clickable with a finger.

## Bugs discovered: 
### Solved bugs

1. **Was getting the following error on the console**

<div align="center">
    <img src="/static/images/readme/console-error.png" target="_blank" rel="noopener" alt="console error"               aria-label="console error"/>
</div>


    ```js
    document.getElementById("defaultOpen").click();
    }
    ```

    was changed to


    ```js
    if (document.getElementById("openDefault")) {
        const element = document.getElementById("defaultOpen").click();
    }
    ```

2. **Secret keys were not being read by gitpod** 
    - Secret keys were not being read by gitpod, despite being added as gitpod variables. 
    - Created an env.py file to store the secret keys in. 

3. **Tab in item details was not changing tabs** 
    - Tab in items details was not changing tabs, all content was displaying the the first tab. 
    - JS was in a link tag and loading as a style sheet as follows:


    ```html
    <link rel="stylesheet" href="{% static 'js/scripts.js' %}">
    ```

    was changed to 


    ```html
    <script src="{% static 'js/scripts.js' %}"></script>
    ```

4. **Reptile tag buttons were not displaying at the top of the reptile page**
    - This was because friendly_name and Name were written incorrectly. 


### Unsolved bugs

1. **Duplicate id in reviews.html**
    - A duplicate id, Reviews, was found in reviews.html. If one id is removed or changed, the content in that div is not displayed. 
    - I decided to leave tackling this bug for a future release.

## Further testing: 
1. Asked friends and family to look at the site on their devices and report any issues they found.
2. FeedMe viewed on all devices and orientations available in Chrome DevTools. 