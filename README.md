[FeedMe](https://flask-feedme-project.herokuapp.com/) was designed, built, and deployed, by myself, Mark Percy as the third project for the Code Institute Full Stack Web Development diploma. The purpose of FeedMe is to be a recipe website that allows members to view FeedMe recipes, as well as add and share recipes of the users own liking.

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Elements on every page](#elements-on-every-page)
        - [Who we are](#who-we-are)
	    - [Login](#log-in)
	    - [Register](#register)
        - [Club picks](#club-picks)
        - [Your picks](#your-picks)
        - [Add book](#add-book)
        - [Edit book](#edit-book)
   	    - [Log out](#log-out)
    - [Features for Future Releases](#features-for-future-releases)

3. [Information Arcitecture](#information-architecture)
	- [Database choice](#database-choice)

4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

5. [Testing](#testing)
    - See seperate [TESTING.md](TESTING.md) file.

6. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)
 
7. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

----

# UX

## Goals

### Visitor Goals

The target audience for FeedMe are:
- People who enjoy cooking. 
- People who are interested in joining an online recipe website.
- People who want to share good recipes they make. 
- People looking for recipe recommendations. 
- People looking for a website to store their recipes. 

User goals are:
- To join an online recipe website. 
- Find new recipes via the FeedMe website. 
- Share recipes that I have enjoyed with other FeedMe members. 
- To be able to add, edit, and delete my recipes on the website. 
- Be able to navigate the website easily and view the recipe in detail. 

### FeedMe's Goals

The goals of FeedMe are:
- Provide a platform where users can find recipe recommendations via the FeedMe website and its members. 
- For FeedMe members to be able to add, edit, and delete recipes that they would like to share. 
- Provide a platform for FeedMe members to share recipes they would like to add. 
- For FeedMe members to be able to view recipes in detail.  

## User Stories

As a visitor to the FeedMe website I expect/want/need:

1. To be able to easily find the information I am looking for, the layout needs to make sense so that I am not put off. 

2. The site to be laid out in a way that is easy to navigate, so that I can find what I need. 

3. The site to be responsive and navigable for various device sizes; desktop, tablet, and phone. For the content to look good 
   on all of the devices.

4. To learn more about FeedMe. 

5. To be able to connect to FeedMe's social media accounts. 

6. To be able to click on recipes for further information about them. 

7. To be able to add, edit, and delete recipes that I would like to share with others. 

8. To be able to search for recipes on the website using keywords.

9. To be able to log in and out with ease. 

10. To be notified that I have logged in or out of my account. 

11. To be notified about changes that are made, inlcluding adding, editing, and deleting recipes. 

## Design Choices

### Fonts
- The primary font 'Open Sans' was chosen to be the main text of this site as it is easy to read, looks professional, and goes well with the secondary font. "Open Sans Condensed' is used for headings and sub headings. 

- The secondary font 'Playfair Display' was chosen for the websites logo font, hoome banner and recipe headings as it looks fun, and is easy to read. 

### Colors
- The colour scheme for this site was rendered on [Cooler](https://coolors.co/) and can be seen below:

<div align="center">
    <img src="/static/images/color-palette.png" alt="Colors used in the FeedMe website" aria-label="Colors used in the FeedMe website"/>
</div>

- Cadet Grey: #91A3B0
- Columbia Blue: #BCD4DE
- Pale Pink: #EFD3D7
- Isabelline: #FCF7F2

- The grey was used in the navbar and footer when you hover over the nav links. 

- The blue was used as the background color for both the navbarr and footer.

- The pale pink was used as the background color for succesful flash messages and for the banner on the home page. 

- The cream color was used as the background color for the website. 

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the design and planning process for this project. 

- [Desktop - Home page](/static/images/wireframes/desktop-home-page.png)
- [Desktop - FeedMe recipes](/static/images/wireframes/desktop-feedme-recipes.png)
- [Desktop - Your recipes](/static/images/wireframes/desktop-your-recipes.png)
- [Desktop - Recipe page](/static/images/wireframes/desktop-recipe-page.png)
- [Desktop - Add a recipe](/static/images/wireframes/desktop-add-recipe.png)
- [Tablet - Home page](/static/images/wireframes/tablet-home-page.png)
- [Tablet - FeedMe recipes](/static/images/wireframes/tablet-feedme-recipes.png)
- [Tablet - Your recipes](/static/images/wireframes/tablet-your-recipes.png)
- [Tablet - Recipe page](/static/images/wireframes/tablet-recipe-page.png)
- [Tablet - Add a recipe](/static/images/wireframes/tablet-add-recipe.png)
- [Mobile - Home page](/static/images/wireframes/mobile-home-page.png)
- [Mobile - FeedMe recipes](/static/images/wireframes/mobile-feedme-recipes.png)
- [Mobile - Your recipes](/static/images/wireframes/mobile-your-recipes.png)
- [Mobile - Recipe page](/static/images/wireframes/mobile-recipe-page.png)
- [Mobile - Add a recipe](/static/images/wireframes/mobile-add-recipe.png)

# Features
 
## Existing Features

### Elements on every page

#### Navbar

![Navbar](/static/images/navbar.png)

- The navbar features on every page.

- **In desktop view**  The navigation bar features the website name ‘FeedMe' on the far left, and website pages on the far right.
  
- A user who is logged in will see the options of Home, FeedMe Recipes, Your Recipes, Add a recipe, and Log out. 

- A user or visitor who is not logged in will see the options of Home, FeedMe Recipes, Log in, and Register. 

- **In tablet and mobile view**  the name remains in the left side of the navigation bar, where users would expect it to be. The burger 
  icon to display the full navigation menu is on the far right. 

#### Footer

![Footer](/static/images/footer.png)

- The footer features on every page.

- The footer has four sections - social media icons, contact us, recipes, and my account. 

- The social icons are links to FeedMee's social media accounts for Facebook, Instagram, Pinterest, and Twitter. They are located under the FeedMe heading. 

- Contact us, includes an email address and telephone number for FeedMe.  

- Recipes, include all the different recipe categories. 

- My account, when logged in, shows 'Your Recipes' and 'Logout'. If not logged in, it shows 'Log in' and 'Register'. 

### Home

**Top Recipes**

![Toop Recipes](/static/images/readme/top-recipes.png)

- The first section of the home page displays top recipes of the week. 

- There are fur recipes, and if you click on them, they take you to the full recipe. 

**Home Banner**

![Home Banner](/static/images/readme/home-banner.png)

- This section includes a banner, which has been split in two. 

- The first half includes the phrase 'Feeling hungry? Checkout some of our recipes below', with the 'See All Recipes' button directly below. This button will take you to the FeeMe Recipes page. 

- The second half is a panorama image of pizza and pasta. 

**Search by Category**

![Search by category](/static/images/readme/search-by-category.png)

- This is the last section of the home page, with the sub-heading of 'Search by Category' and each of the categories below. 

- The categories are displayed via a circular image, with it's category name below. 

### Log in

- The login page features a standard login form asking for username and password.
- Validation for this form is handled in the back end and a flash message displays 'Welcome (username)'. 
- Once logged in they are taken directly to their profile page. 

### Register

- A user who is not logged in can create a new account using the register page. The page on this form includes a username 
 (which must be unique), and a password. 
- If a user who already has an account tries to register, a flash message display 'Username already exists'. 

### Club picks

![Clubs picks](/static/images/club-picks.png)

- This page displays all The Bookshelf's books added each month. There are four books in each row. 
- The book is displayed by its cover image with a button under each book, displaying the month and year it was added. 
- If the button is clicked on, it brings up a modal with futher information about the book. 

**Modals**

![Clubs picks modal](/static/images/club-picks-modal.png)

- The modal is divided into two parts. The first being further information about the book, and the second being a review of the 
  book by The Bookshelf. 
- The first part contains the books image, when it was added, the title of the book, the author, a synopsis, and a link to Amazon
  store if the member wishes to purchase the book. 
- The second part is just a detailed review of the book by The Bookshelf. 
- To close the modal, the member has the option of clicking the x icon on the top right hand side of the modal or the done button at 
  the bottom of the modal. 

### Your picks

![Your picks](/static/images/your-picks.png)

- The top of the page displays the members name, username's picks, indicating that this is their profile. 
- This page displays all if The Bookshelf's members books added. There are four books in each row. 
- The book is displayed by its cover image with a button under each book, displaying the member's name who added it. 
- If the button is clicked on, it brings up a modal with futher information about the book. 

**Modals**

![Your picks](/static/images/your-picks-modal.png)

- The modal is divided into two parts. The first being further information about the book, and the second being a review of the 
  book by the member. 
- The first part contains the books image, when it was added, the title of the book, the author, a synopsis, and a link to Amazon
  store if the member wishes to purchase the book. 
- The second part is just a detailed review of the book by The Bookshelf. 
- The modal also gives the option of editing or deleting the book. Clicking on the edit button will take the member to the edit book page,
  which is detailed further down. 
- If the user clicks on the delete button, they are met with another modal that pops up asking if they are sure they want to delete the 
  book. If they click cancel, it takes them back to their profile page. If they click delete, the book is deleted from their profile.  
- To close the modal, the member has the option of clicking the x icon on the top right hand side of the modal or the done button at 
  the bottom of the modal. 

### Add book

![Add book](/static/images/add-book.png)

- This page contains a form for members to add a book to their profile for other members to see. 
- It includes a section for the book title, author, a link to the book cover, a link to the Amazon store for the book, a synopsis, 
  and the members personal review of the book. 
- Once the book has been added, a flash message displays 'Book successfully added'. 

### Edit book

![Edit book](/static/images/edit-book.png)

- This page is accessed within the edit button of the book modals in Your picks. It contains a form for members to edit a book that they have 
  previously added.  
- It is identical to the Add book page. 
- Once the book has been edited, a flash message displays 'Book successfully updated'.
- Members only have access to edit their own books, and are unable to edit other members books. 

### Log out

![Log out](/static/images/logout.png)

- Any user who clicks on 'Log out' from the navigation bar is automatically logged out and their session data cleared. They are informed
  that they have been logged out with a flash message displaying 'You have been logged out'. 

## Features for Future Releases

1. **Being able to upvote books**
    - Having a star rating available in a book's modal for users to vote for. 
    - The star rating is displayed in each book's modal, giving the user an idea of how other members felt about the book. 

2. **Users being able to add reviews to The Bookshelf's picks and members books**
    - Having an option for users to write a reviews on books added by The Bookshelf and its members. 
    - The option would be available on each of the book's modals next to the done, edit, and delete buttons. 
    - The reviews would appear under the orginal review added. 

# Information Arcitecture

### Database Choice
- According to project instructions, the document-based database MongoDB is used. 

- The database 'FeedMeDB' has three collections 'categories', 'recipes' and 'users'.

**categories**

| Key | Data Type | Comment |
--- | --- | --- |
_id | ObjectId | Unique identification number
category_name | String | Name of category

- **categories** contains the various recipe categories on he FeedMe website, including a unique id, and category name. 

**recipes**

| Key | Data Type | Comment |
--- | --- | --- |
_id | ObjectId | Unique identification number
category_name | String | Name of category
recipe_name | String | Name of recipe
image_url | String | Recipe imge url
time | String | Total time of recipe
servings | String | Number of servings per recipe
created_by | String | The. user who added the recipe
ingredient_1 | String | Recipe ingredient
ingredient_2 | String | Recipe ingredient
ingredient_3 | String | Recipe ingredient
ingredient_4 | String | Recipe ingredient
ingredient_5 | String | Recipe ingredient
ingredient_6 | String | Recipe ingredient
ingredient_7 | String | Recipe ingredient
ingredient_8 | String | Recipe ingredient
ingredient_9 | String | Recipe ingredient
direction_1 | String | Recipe direction
direction_2 | String | Recipe direction
direction_3 | String | Recipe direction
direction_4 | String | Recipe direction
direction_5 | String | Recipe direction
direction_6 | String | Recipe direction
direction_7 | String | Recipe direction
direction_8 | String | Recipe direction
direction_9 | String | Recipe direction
notes | String | Additional recipe notes

- **recipes** contains information about the recipes added to the FeedMe website. 
- This includes the recipe category, recipe name, a url for the recipe image, the total time it takes to make the recipe, number of servings per recipe, which user added the recipe, recipe ingredients, recipe direections, and addditional recipe. notes. 

**users**

| Key | Data Type | Comment |
--- | --- | --- |
_id | ObjectId | Unique identification number
username | String | Name of user
password | String | Hashed password

- **users** contains information about the user, including a unique id, their username, and a hashed password. 

# Technologies Used

### Tools

- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Gitpod](https://www.gitpod.io/) - IDE (Integrated Development Environment) used to write the code.
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.
- [Heroku](https://id.heroku.com/) - Container-based cloud platform for deployment and running of apps.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Templating engine used.
- [Favicon](https://favicon.io/) used to created the favicon used on the site.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - Used to inspect page elements, test different CSS styles and debug site issues using the console.

### Databases
- [MongoDB](https://www.postgresql.org/) a NoSQL database program, using JSON-like documents. 

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) used to provide libraries and tools for the site such as Werkzeug.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing 
 
- See seperate [TESTING.md](TESTING.md) file. 

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Instructions
1. Save a copy of the github repository located at https://github.com/MAN95-dev/the-bookshelf by clicking the "download zip" button at 
   the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the 
   repository with the following command.
    ```
    git clone https://github.com/MAN95-dev/the-bookshelf
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
    ```
    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes you are working with a windows operating system. 
Your Python command may differ, such as `python3` or `py`_

4. Activate the .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](
    https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip.
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE. 

    - If using VSCode, locate the `settings.json` file within the .vscode directory and add your environment variables as below. 
      Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

    ```json
    "terminal.integrated.env.windows": {
        "HOSTNAME": "<enter hostname here>",
        "DEV": "1",
        "IP": "<your IP>",
        "MONGO_DBNAME": "<your database name on MongoDB>",
        "MONGO_URI": "<your URI to your MongoDB database>",
        "PORT": "<your port>",
        "SECRET_KEY": "<your secret key>" 
    }
    ```

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the 
      following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it 
      possible to have different settings for the two environments. For example setting DEBUG to True only when working in development 
      and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with 
   the command used at step 4.

9. You can now run the program locally with the following command: 
    ```
    python3 app.py
    ```

## Heroku Deployment

To deploy The Bookshelf website to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. 
   Give it a name and set the region to whichever is applicable for your location.

5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the heroku app to the correct GitHub repository.

7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8. Set the following config vars:

| Key | Value |
--- | ---
IP | `<your IP>`
MONGO_DBNAME | `<your database name on MongoDB>`
MONGO_URI | `<your URI to your MongoDB database>`
PORT | `<your port>`
SECRET_KEY | `<your secret key>`

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

12. Your heroku site should run as expected.

# Credits

## Content
- Recipe content was taken from [inspired taste](https://www.inspiredtaste.net/). 

## Images
- The hero image was taken from [Shutterstock](https://www.shutterstock.com/home). 
- The recipe images were taken from [inspired taste](https://www.inspiredtaste.net/). 

## Code

- The following websites helped me understand and create my website, by viewing examples and explanatons.
    - [W3schools](https://www.w3schools.com/)
    - [Bootsnipp](https://bootsnipp.com/)
    - [Code Institute](https://codeinstitute.net/)
    - [Stack Overflow](https://stackoverflow.com/)

- The following website provided inspiration for my website.
    - [Tasty](https://tasty.co/)
    - [Pick Up Limes](https://www.pickuplimes.com/)

- The 404 template was taken from [colorlib](https://colorlib.com/). 

- The README file was taken from Anna Greave's 'The House of Mouse' project to use as a template.
    - [The House of Mouse by Anna Greaves ](https://github.com/AJGreaves/thehouseofmouse)

## Acknowledgements

 - Special thanks to my mentor Precious, for his time, and guidance with this project. 
 - Code Institute tutors for helping support and guide me in the right direction with my code.