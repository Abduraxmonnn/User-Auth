## Welcome to

# User Auth

test project

### About the Project

Project Description: User Authentication and Profile Management System

The User Authentication and Profile Management System is a Django-based web application designed to provide secure user
authentication and versatile profile management capabilities. This system is developed to meet the demands of modern
user-centric applications, offering features such as phone number authorization, invitation codes, and user profile
interaction.

Key Features:

* Phone Number Authorization:
  Users can authenticate themselves using their phone numbers. Upon entering their phone number, the system simulates
  the sending of a 4-digit authorization code.

* Invitation Codes:
  Users are assigned a randomly generated 6-digit invite code upon their initial authorization. This code serves as an
  invitation for other users to join the platform. Users can also input other users' invite codes during their profile
  setup.

* Custom User Model:
  The system utilizes a custom user model created by extending Django's AbstractBaseUser and PermissionsMixin. This
  allows
  for a tailored authentication process, improved user data management, and the inclusion of custom methods and fields.

* Profile Management:
  Users have access to their profiles, where they can view and manage their information. They can input other users'
  invite codes to establish connections and activate those codes.

* Invite Code Tracking:
  The profile includes a list of users (phone numbers) who have entered the invite code of the current user. This
  feature
  fosters a sense of community and allows users to see the connections they have established.

* We used
  to [Python 3.10](https://www.python.org/) for mainly language and [Django](https://www.djangoproject.com/) Framework
  and [Django REST framework (DRF)](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for
  building Web APIs to users

### About the BackEnd

This project raised in architecture `MVT` `(Model View Template)`. There are email verification, multilanguage, user
token,
calculate statistics each centers and other features.


***

## Tech

* [Django](https://www.djangoproject.com/) - is a high-level `Python Web framework`
* [Django REST framework](https://www.django-rest-framework.org/) - `Django REST Framework` is a powerful and flexible
  toolkit for building Web `APIs`
* [PostgreSQL](https://www.postgresql.org/) - open source object-relational database system

And many other libraries.

Dillinger requires [Python](https://www.python.org) `v3.10` or higher.

```shell
$ git clone https://github.com/Abduraxmonnn/User-Auth.git
$ cd User-Auth/
```

***

## Setting project

* `Linux`

```shell
$ virtualenv -p /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `Windows`

```shell
$ python -m venv ./venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `MacBook`

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

***

## Development

### Configure `PostgreSQL`

Create clear database named `test_db`.

Create `test_user` db user with password `test1234` and grand privileges to him.

If you want to create a database with a different name, user and password, you can change the initial configuration to
your own configuration.

```shell
$ sudo -u postgres psql
postgres=# ...
CREATE DATABASE test_db;
CREATE USER test_user WITH PASSWORD 'test1234';
ALTER ROLE test_user SET client_encoding TO 'utf8';
ALTER ROLE test_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE test_user SET timezone TO 'Tashkent/Asia';
GRANT ALL PRIVILEGES ON DATABASE ocean_db TO test_user;
\q
```

Migrate to database and run project.

```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

`Output`

```shell
System check identified no issues (0 silenced).
Month date, year - hh:mm:ss
Django version 4.1.7, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open http://127.0.0.1:8000 in your browser for see result.

## Note:

I have used `models.Model` for `CustomUser` instead of `AbstractBaseUser` and `PermissionsMixin` because for the
specific task you've described, using a model to handle phone number authorization is likely more suitable than using 
Django's `AbstractBaseUser` and `PermissionsMixin`. Here's why:

1. **Simplicity and Task Fit**:
   Using a model dedicated to phone number authorization simplifies the implementation of the specific task you're
   trying to achieve. The main goal here is to handle the process of sending authorization codes to phone numbers
   and verifying those codes. Creating a dedicated model for this purpose allows you to focus on this task without
   needing to implement more extensive features provided by `AbstractBaseUser` and `PermissionsMixin`.

2. **Overhead**:
   `AbstractBaseUser` and `PermissionsMixin` are more geared towards creating a custom authentication system with
   full-fledged user accounts, including features like password management, role-based permissions, and custom user
   attributes. For a simple task like phone number authorization, using these classes might introduce unnecessary
   complexity and overhead. I didn't have to use Permissions for such a simple project.

3. **Customization**:
   If you're only looking to handle phone number authorization and don't need to store additional user-related
   information, a custom model can be tailored to your specific needs. This means you won't be burdened by additional
   fields and methods that come with `AbstractBaseUser` and `PermissionsMixin`.

4. **Maintainability**:
   When you create a separate model for phone number authorization, it helps maintain the single responsibility
   principle. Each component of your application is responsible for one task, making the codebase more organized and
   easier to understand.

5. **Scalability**:
   If you plan to expand the functionality of your application beyond phone number authorization, you can still
   integrate your custom model into a more comprehensive authentication system. In the future, if you find the need for
   a more complex authentication mechanism, you can explore integrating with `AbstractBaseUser` and `PermissionsMixin`
   as part of that expansion.

In summary, if your primary goal is to implement phone number authorization as described, using a dedicated model is a
more straightforward and appropriate approach. It keeps your code focused on the specific task and avoids the
unnecessary complexity that comes with `AbstractBaseUser` and `PermissionsMixin`.
