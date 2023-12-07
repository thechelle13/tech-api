# React + Vite + Tailwind + Python + Django

**TechPower - Project README**

Introduction:

Welcome to TechPower, a platform designed to connect employers with tech talent efficiently. This README provides an overview of the project, its purpose, development process, and key features.


Purpose and Motivation:

TechPower aims to simplify the process of finding and hiring tech talent by addressing fundamental employment questions. The platform allows users to register, create and manage posts for tech jobs, view a list of all posts, edit and delete their own posts, and more.


How It Works:

TechPower operates as a web application with user authentication. Users can register, log in, create, edit, and delete posts. The system also includes features such as viewing all posts and logging out securely.


How It Was Developed:

The development process followed the outlined user stories and criteria. The project utilizes a Sqlite database with user-related data, including at least one many-to-many relationship. Wireframes were created to illustrate the layout of each view, and an Entity-Relationship Diagram (ERD) was designed to visualize the database structure.


How to Install and Run the Apps Used in Development:

**To install and run the application, follow these steps:**

Clone the repository.

bash
Copy code
git clone <repository-url>
Install dependencies.

bash
Copy code
npm install
Run the application.

bash
Copy code
npm start
Access the application in your web browser at http://localhost:3000.


Difficulties and Challenges Faced During Process:

Throughout the development process, several challenges were encountered, including user authentication, database design, and form handling. These challenges were addressed and resolved to ensure a robust and user-friendly application.

**Public Links:**

Wireframes -  https://miro.com/app/board/uXjVMq9Opck=/?share_link_id=483286055911

ERD - https://dbdiagram.io/d/TechPower-MVP-656a0b0956d8064ca0360b0f

Problem Solved:

TechPower solves the challenge of efficiently connecting employers with tech talent by providing a streamlined platform for creating, managing, and viewing tech job posts.

Project MVP: Stories & Criteria:


Register:
As a potential user, I can create an account in the system.
Given a potential user wants to create an account
When they select the Register option
Then they should be directed to a form to enter their User Profile information
When the user clicks the Register button, a new User Profile is created in the database.

Log In:
As the Tech product owner, I want all users authenticated to record user activities.
Given an unauthenticated user in the Tech application
When they click any link
Then they should be prompted to log in using their email address
If the email matches an existing User Profile, they should be authenticated and directed to the home page
If the email does not match, display an error message.

View All Posts:
As a reader, I want to see a list of all Posts to choose an interesting one.
Given the user in the Rare application
When they select the Posts menu option
Then they should be directed to the Posts list page.

Create A Post:
As an author, I want to create Posts to post available tech jobs.
Given a user in the app
When they select the Create Post menu button
Then they should be directed to a form for creating a new post
When the user enters relevant information and clicks Save, the Post is saved to the database.

View My Posts:
As an author, I want to see a list of all my Posts.
Given the user in the Rare application
When they select the My Posts menu option
Then they should be directed to the "My Posts" list page.

Edit My Post:
As an author, I want to modify my Posts.
Given the user viewing the Post list
When they select the option to edit a Post
Then the user should be directed to a form to change the Post's information
When the user finishes updating and clicks Save, the updated Post is saved to the database
When the user decides not to edit and clicks Cancel, they are redirected back to the list page.

Delete A Post of Mine:
As an author, I want to remove a post I have written.
Given an author viewing their Post
When they select the delete option
Then they should be presented to confirm the deletion
If the author confirms, the Post is removed from the system
If the author rejects confirmation, the Post is not removed.

Log Out:
As a user, I want to log out of the system.
Given an authenticated user in the Tech application
When they select the Logout option
Then they should be logged out and directed to the Log In page.
Stretch Goals: Stories & Criteria

Create a New Skill:
As an author, I want to create a new Tag to better classify my posts.
Given an author on the Skill list page
When they select the Create Skill button
Then they should be directed to a form to enter a new Skill name
When the user enters a Skill name and clicks Save, a new Skill is saved to the database.
