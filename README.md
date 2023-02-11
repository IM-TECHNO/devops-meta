
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

To run tests, run the following command : 

```bash
  cd TestCase
  python testcase_run.py
```


## Roadmap

- Additional browser support

- Fully automate Jenkins deployment


## Authors

- [@Pavithra Ragunathan (Trainer, Founder and Director of Metazord)](https://github.com/Pavithratrdev)

- [@Rahul(Student at Metazord)](https://www.github.com/IM-TECHNO)


## Support

For support, email raagulshiva@gmail.com .


## House of Metazord
![Logo](https://i.ibb.co/DQzNLqR/Metazord-Logo.png)

