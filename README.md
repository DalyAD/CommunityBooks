# Community Books

https://ms3-community-books.herokuapp.com//

Welcome to the site and I hope you enjoy it. This site is used as a library for recommending books and looking for books to read that have been recommended by other users. 

I created this site as a community resource to see book recommendations as once a book has been recommended to me I can sometimes forget.
 
## UX
 
I created this project as a place for people to share book recommendations between each other. Giving users full access to add, edit and delete entries as they see fit.

Wireframes

All wireframes were made using Balsamiq.

index.html

 


map.html

 


contact.html

 


User Stories

— As a reader I would like to find new book recommendations added by other users.
  
— If I see a book with incorrect information I would like the option to edit a book..

— As I receive a lot of recommendations I would like to make sure the site is only displaying the best books, so if I see a book I don't like I would like to delete it.

— As it goes both ways I would like to add books that I enjoy to the site

Features

app.py

In my app I use routes and view to direct to app pages and functions on the site.

I make regular use of redirects after a form has been submitted.

index.html
— On this page I just made a card detailing the idea behind the site and some simple instructions.

library.html
— I used this page to loop through all books from MongoDB and display them nicely in their own card accompanied by "Edit" and "Delete" buttons.

addbook.html
— I used form elements on this page to accept user input and upload it to MongoDB. Once done, the user is redirected to the Library page where they can see their entries.
I also gave a button to return to the Library should the user wish to go back without making an addition.

I have form validation active on the front end to ensure no fields are left blank. This display s message to the user if the field is left blank, the border on the input box also changes from red to green. Red if left blank and green if it is populated with text.

editbook.html
— I used form elements on this page to accept user input for an existing entry and update the relevant book on MongoDB. The user is then redirected to the Library where they
can view their entry. As in the "addbook.html" section there is again a button allowing users to return to the library without making changes.

— I have form validation active on the front end to ensure no fields are left blank. This display s message to the user if the field is left blank, the border on the input box also changes from red to green. Red if left blank and green if it is populated with text.

base.html
— This page contains the pages nav element and extends it to all other pages. I also added all my links for CSS, JS, JQuery and Materialize here.

— This page also includes a button for returning to the top of the page to save the user time scrolling should they have gone far down the page. 
 
Existing Features
— Across the site I have implemented all CRUD features.

— I activated form validation on the front end for all forms.

— I have added a scroll to top button using JS and JQuery so that users can jump to the top of the page if they have scrolled far down.

— I have included a.gitignore file to conceal my environment variables in env.py and in __pycache__/.

### Features Left to Implement
— In future development I would like to include form validation on the back end also to prevent any security breaks.

— I would like to include alert buttons on the "Edit" and "Delete" pages to confirm the users input before the either commit changes or remove an entry. 

## Technologies Used

— [JQuery](https://jquery.com)
 — The project uses **JQuery** to support some design and functionality.

— [Materialize](https://materializecss.com/)
 — The project uses **Materialize** to simplify the design process.
    
— [Flask](https://flask.palletsprojects.com/en/1.1.x/)
 — Flask was used to create my application.

## Testing

1. index.html
 — I tested all buttons to make sure everything is linked correctly.

2. library.html
 — I again tested all buttons to make sure everything is linked correctly. 
 — I clicked on the delete button. I then made sure the entry was no longer on my MongoDB cluster or the library page.

3. addbook.html
 — I again tested all buttons to make sure everything is linked correctly. 
 — I added entries to all fields and then clicked the "Add Book" button. I then made sure the book was added to both the Library page and my MongoDB cluster.
    — I went through the following tests with my form validation.
     1. Left all fields empty and tried to submit. Form validation worked.
     2. Left the first field empty and tried to submit. Form validation worked.
     3. Left the second empty and tried to submit. Form validation worked.
     4. Left the third field empty and tried to submit. Form validation worked.
     5. Left the fourth field empty and tried to submit. Form validation worked.
     6. Left the fifth field empty and tried to submit. Form validation worked.
     7. Populated all fields and there were no errors.

4. editbook.html
 — I again tested all buttons to make sure everything is linked correctly. 
 — I edited an existing entry on all fields. I then made sure the entry had changed both on the Library page and in my MongoDB cluster.
     — I went through the following tests with my form validation.
     1. Left all fields empty and tried to submit. Form validation worked.
     2. Left the first field empty and tried to submit. Form validation worked.
     3. Left the second empty and tried to submit. Form validation worked.
     4. Left the third field empty and tried to submit. Form validation worked.
     5. Left the fourth field empty and tried to submit. Form validation worked.
     6. Left the fifth field empty and tried to submit. Form validation worked.
     7. Populated all fields and there were no errors.

## Deployment

I used Heroku to deploy my site using the following steps.

1. Create a requirements.txt file.
2. Create a Procfile. (Case sensitive)
3. Create a new app with Heroku.
4. Add IP and PORT config variables to Heroku.
5. Push my code to Heroku.

This site can also be deployed by selecting the 'Clone' option from the below GitHub repository.

https://github.com/DalyAD/CommunityBooks

### Content
— The design elements were used from the Materialize site.
— I customized a scroll to top button that I got from W3schools from the following link (https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)

### Media
— The background image I used was found using Google images.
