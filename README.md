
# Devops-Metazord-Dockerize

This project is currently in development and is only for educational purposes. Anyone including students/staffs outside of Metazord can use this as their first DevOps project. Happy Coding ! 

Warning : This project is still WIP !!!


## Get Started locally

To get started, clone this repository using : 

```bash
  git clone https://github.com/IM-TECHNO/devops-meta.git
  cd devops-meta
```


Install all the dependencies using pip : 

```bash
  pip install -r requirements.txt
```

Then, start the webserver using :

```bash
  python main.py
```



## Installation with  Docker

Clone this repository :

```bash
  git clone https://github.com/IM-TECHNO/devops-meta.git
  cd devops-meta
```
Build using docker build : 

```bash
    docker build --no-cache -t metazord-devops .
```
Run using docker run on port 5005 : 

```bash
    docker run -p 5005:5005 metazord-devops
```
    
## Running Tests

- Before running any tests, create a 'reports' directory in the 'TestCase' folder.
To run tests, run the following command : 

```bash
  cd TestCase
  pytest -s -v testcase.py --disable-warnings --alluredir=reports
```

After completion, you can now view the report using : 

```bash
  allure serve reports
```
NOTE : you may need to install [Allure Command Line Tool](https://github.com/allure-framework/allure2/releases) and add it to your path.

## Setting up Jenkins

- Create a new Free-Style project with a title. 
- In the General>Advanced, enable 'Use custom workspace' and enter the project directory
- In Build steps, select 'Execute a Windows batch command and enter the commands given below'

```bash
  call .\venv\Scripts\activate.bat
  pytest -s -v --disable-warnings --alluredir=reports TestCase\testcase.py
```

- Select 'Post-build actions and select 'Allure Report'
- In the path field, enter 'reports'
- Click apply and you're done.

## Roadmap

- Additional browser support

- Fully automate Jenkins deployment

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Authors

- [@Pavithra Ragunathan (Trainer, Founder and Director of Metazord)](https://github.com/Pavithratrdev)

- [@Rahul(Student at Metazord)](https://www.github.com/IM-TECHNO)


<!---## House of Metazord
![Logo](https://i.ibb.co/DQzNLqR/Metazord-Logo.png)--->

