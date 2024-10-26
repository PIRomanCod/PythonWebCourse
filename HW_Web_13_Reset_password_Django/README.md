# HW_Web_13 (Second part - Django) User's email verification + password reset

# Implemented required tasks:
- Implemented a password reset mechanism for a registered user;
  (password recovery process:

        - The user requests a password reset by entering their email address in the password reset form.
        - Django generates a unique password reset token and sends an email with a password reset link to the user's email address. The link enables the password reset token as a parameter.
        - When the user clicks on the reset password link, Django checks the password reset token and a form appears to enter a new password.
        - The user enters a new password and submits the form.
        - Django updates the user's password and notifies the user)
- All environment variables are stored in the .env file and used in the settings.py file;


# HW_Web_10_Django
 
# Folder "QUOTEPAGES":
 Try to make copy of website 'http://quotes.toscrape.com.'


Fulfilled conditions from the task:

-Implemented the possibility of registering on the site and entering the site + user profile.
-Only for registered users can adding a new author, a new tag, a new quote.
- All quotes are viewable without user authentication
- Search for quotes by tag. When you click on a tag, a list of quotes with this tag is displayed.
- Search for quotes by author. When you click on a author, a list of quotes with this author is displayed.
- Implement the "Top Ten tags" block and display the most popular tags.
- Implement pagination. These are the next and previous buttons

# Folder "SELENIUM"
- Instead of manually filling the database in the folder "SELENIUM" there is an auto-completion script using selenium from already existing json files from the previous homework

# Problems:
- Page styles are awful

# Start:
- python manage.py runserver - start app
- python manage.py makemigrations  - create migration
- python manage.py migrate - applying migration

# Deploy with Fly.io:
- powershell -Command "iwr https://fly.io/install.ps1 -useb | iex" -> install fly.io
- fly login -t <token> -> login to fly.io
- Dockerfile -> create Dockerfile
- fly launch -> create fly.toml
- fly deploy -> deploy app
- fly open -> open app in browser
- webinar - https://www.youtube.com/watch?v=Oiyk-9ErIjo&t=5241s - from 1:00:00 to 1:30:00

 
