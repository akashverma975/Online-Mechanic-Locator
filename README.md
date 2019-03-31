# Online Mechanic Locator 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2561cd85d8954b7db6f66dc8f981e1e6)](https://app.codacy.com/app/akashverma975/Online-Mechanic-Locator?utm_source=github.com&utm_medium=referral&utm_content=akashverma975/Online-Mechanic-Locator&utm_campaign=Badge_Grade_Dashboard)
[![CodeFactor](https://www.codefactor.io/repository/github/akashverma975/online-mechanic-locator/badge)](https://www.codefactor.io/repository/github/akashverma975/online-mechanic-locator)
[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

## Follow the Steps given below to setup the project on your local machine
1.  Make sure python 3.7 or higher version, PostgreSQL11 and Redis Server is installed on your computer.
2.  Clone this repository on your PC using command prompt: 
```bash
git clone https://github.com/akashverma975/Online-Mechanic-Locator.git
```
3.  cd into Online-Mechanic-Locator folder:
```bash
cd Online-Mechanic-Locator
```
4.  Create Virtual Environment. Make sure **`virtualenv`** package is installed on your PC(Windows):
```bash
virtualenv [virtual_environment_name]
```
5.  Activate Virtual Environment by typing:
```bash
[virtual_environment_name]\Scripts\activate
```
6.  Now install all project dependencies from requirements.txt:
```bash
pip install -r requirements/local.txt
```
7.  Overwrite **`.env.example`** with appropriate values and rename it to **`.env`**

8.  Congratulations you've done the project setup. 
Now **`migrate`** and **`run`** the Project by typing the following in the command prompt:
```bash
python manage.py migrate
python manage.py runserver
```

### Third Year Project by Akash Verma 
[![Akash's Twitter](https://img.shields.io/twitter/follow/akashvermapro.svg?label=Follow&style=social)](http://www.twitter.com/akashvermapro) [![Akash's Github](https://img.shields.io/github/followers/akashverma975.svg?label=Follow&style=social)](https://github.com/akashverma975)
