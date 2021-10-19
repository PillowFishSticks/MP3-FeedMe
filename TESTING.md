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

All steps on desktop were repeated in browsers: Firefox, Chrome and Safari. 

#### Elements on every page

1. Navbar 
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirm that when logged out the options "Register" and "Log in" are visible and that "My Recipes", "Add Recipes" and 
      "Log out" are not.
    - Log into the site, confirm that options "My Recipes", "Add Recipe" and "Log out" are visible and that "Register" and 
      "Log in" are not.

2. Footer
    - Hover over links in the footer, confirm the animation works as expected.
    - Click all links in the footer, confirm that they take the user to the relevant pages within the site.
    - Click the social icons, confirm that they open a new tab and take the user to the correct page.
    - Check date of copyright information, confirm year displayed matches the current year.

#### Home
1. Top Recipes 
    - Adjust width of browser window, confirm hero image is responsive. 
    - Ajust browser width, confirm top recipes change to taken to the correct recipe page. 
    - When hovering over the image, ensure it fades and 'See Recipe' appears. 

2. Home Banner 
    - Adjust width of browser window, confirm that the image is not present on iPad and mobile device screens. 
    - Click on the 'See All Recipes' button to check that is directs the user to the FeedMe Recipes page. 
    - When hovering over the button, ensure that the colors are reversed. 

3. Search by Category
    - Click each of the category's to ensure that they take show the correct recipes. 

#### Log in

- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to the My Recipes page.

#### Register

- Log out then go to the register page. Confirm that the register form is displayed as expected.
- Fill in the form with a username already in the database, confirm that the user is informed that the username already exists. 
- Fill in the registration form correctly, confirm that the user is automatically directed to the My Recipes page, and the message 
  "Weclome `<username>`." is displayed above. 

#### FeedMe Recipes

- Go to the FeedMe Recipes page and check that it is laid out correctly, 3 recipes to a row. 
- Ajust browser width, confirm top recipes change to the correct cloumn sizing. 
- Click on each of the recipes and ensure the user is taken to the correct recipe page. 
- When hovering over the image, ensure it fades and 'See Recipe' appears. 
- Search for recipes in the search bar using keywords to ensure it works. 
- Search for a recipe or keyword that does not exist, with the message "Sorry, we couldn't find any recipes matching your search..." displaying. 

#### My Recipes

- Go to the FeedMe Recipes page and check that it is laid out correctly, 3 recipes to a row. 
- Ajust browser width, confirm top recipes change to the correct cloumn sizing. 
- Click on each of the recipes and ensure the user is taken to the correct recipe page. 
- When hovering over the image, ensure it fades and 'See Recipe' appears. 

**Recipe page**

- Check that the page is displayed correclty. 
- Adjust browser width, ensure the the recipe page is responsive. 
- Click the "See All Recipes' button to check that is takes the user to the FeedMe Recipes page.

#### Add Recipes

- Go to the Add Recipe page and ensure the form is laid out correctly. 
- Try and publish the form with information missing to ensure that it doesn't send. 
- Fill out the form correctly and click the publish button, ensure that the user is redirected to the My Recipes page and that the message 
  "Recipe successfully added" displays at the top of the page. 
- Check that when a recipe has been added, that is displays on the My recipes page and the information is added to the database. 

#### Edit Recipes

- Go to the My Recipes page and click on the edit button of a recipe added, to open up the Edit recipe page. 
- Check that the form is laid out correctly, with all previous recipe information present in the form. 
- Edit the content and click the publish button, ensure that the user is redirected to the My Recipes page and that the message 
  "Recipe successfully updated" displays at the top of the page. 
- Check that when a recipe has been edited, that the changes are displayed on the My Recipes page and the information has been updated in 
  the database. 

#### 401 error

- Try and access a page not displayed when logged out. 
- The following flash message is displayed 'Sorry, you are unable to access this page". 

#### 404 error

- Try and access a page that does not exist, by adding text onto the url. 
- Ensure that the user is redirected to the 404 page, stating that the page does not exist and giving them the option to return to the home page. 

#### Log out

- Click Logout in the navbar to ensure that the user is logged out and redirected to the log in page with the following message 
  displayed "You have been logged out". 

### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile and tablet specific elements on my iPhone and iPad, in both the Safari browser and Google 
Chrome browser.

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar 
    - Open the website on mobile and tablet, confirm that the navbar is collapsed into a burger icon
    - click the burger icon, confirm that the navbar list appears are expected.

2. Footer
    - Scroll to the bottom of the page, confirm that the footer content is displayed as expected with the bootstrap grid.
    - No content squashed or squeezed or disproportionate in size.
    - Confirm that all links and buttons in footer are easy to click with a finger on the smallest screen sizes.

3. Club picks and Your picks pages
    - Confirm that the books ar displayed 2 to a row on mobile, and 3 to a row on tablet.
    - Confirm that all clicks and swipes operate as expected on touch screen.
    - Check that modals are the correct proportions and that all their buttons are easily clickable with a finger.

5. All pages
    - Navigate to all pages on the site, check that the layout is as expected for the screen size.
    - Check that all buttons, forms and other elements are the correct proportions and easily clickable with a finger.

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