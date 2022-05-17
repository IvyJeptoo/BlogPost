### PROJECT  NAME 
 +  BLOG ZONE

### AUTHOR 
 + Ivy Jeptoo
 
 ## DESCRIPTION 
 - A python web application that allow users to login and post blogs and can also comment on other blogs and also view random generated quotes.
 
 >Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Email  | Account email, ``eg user@gmail.com``|
| Password  | Account password, ``eg 12345678``|

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Email  | User email, ``eg johndoe@testmail.com``|
| Password  | Account password, ``eg password123``|
| Confirm Password  | Account password, ``eg password123``|

> Blog inputs

| Inputs | Description  |
|---|---|
|  Author | The one who posts the blog ie; ``your name``  |
|  Blog title| brief title of the blog|
|  Blog details| The actual blog body|
| Comment| A comment on the blog|

## User Story

- User can sign in if they have no account.

- User can login to their account.

- User can post a blog.

- User can comment on a blog and also delete any comment they want to.

- User can view all the blogs from their account and others. 

- User can logout of the application 

## <a href="https://ivyblog.herokuapp.com//">Live preview of the site</a>

## Cloning
* On your terminal, run the following commands:
* $ git clone https://github.com/IvyJeptoo/BlogPost.git
* $ cd Blog-Site
* Create a virtual environment $ pv -m venv --without-pip virtual
* Activate the virtual environment $ source virtual/bin/activate
* Install Dependancies $ pip install -r requirements.txt
* Inside your root directory create a new file ```start.sh``` and add the following:
* ```python(version) manage.py server```
* Run chmod a+x start.sh  
* Run the application $ ./start.sh
## Development
#### Want to make a contribution to enhance an existing module or fix a bug? Great!
* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request
## Technology Used
* python3.8
* flask
* Sqlite
## Known Bugs
#### 
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Contact Information
* For any inqueries feel free to write to me deniskisavi@gmail.com
## Licence
* MIT License
* Copyright (c) 2022 Ivy Jeptoo



