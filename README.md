# smart-insole-fudan-turku

## Classifier

### To-Do

- More feature selection/generation methods (better features?)

- Testing features (Which ones are best? Some accuracy comparisons for classifiers)

- Building some different classifiers (Traditional machine learning + Deep learning)

- Unsupervised learning probably should be dropped. I think it wont give us good results.

- Taking a look at semi-supervised learning instead (Labeling mixed unlabeled data based on previous data for more training/testing data?)

- Some parameter tuning for the classifiers (avoiding overfitting and other bad things)

- Ensemble learning (combining results from different classifiers built earlier)

### Implemented

- Basic features from feature selection/generation

- Basic classifiers


## Webapp

### To-Do (see issues)

The web app should have the following features:

- login page [OK]
- registration page [OK]
- profile page [OK]

---

- upload session files.
- show in a table the data of a table file.
- Movesole csv file handling? (parsing it and adding the values to the database).
- show session files.
- edit, remove session files.

---

- same info and features as the report generated by the mobile app.
- It has a lot of charts.

---

- Integrating the classifier(s) - Interface.

---

- UI that allows the user to select the sessions file to send to the classifier.
- Prediction Results: Which results will be given to the users. It should refer the sessions files.
- List, edit, remove the predictions results.


---


### Django tutorial

https://www.youtube.com/watch?v=UmljXZIypDc

### Implemented
- Login and account management

### Django configuration

https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Requirements

```
certifi==2018.11.29
Django==2.1.7
django-crispy-forms==1.7.2
mysqlclient==1.4.2.post1
Pillow==6.0.0
pytz==2018.9
scikit-fuzzy==0.3.1
virtualenv==16.4.3
wincertstore==0.2
```

List dependencies
```
pip freeze > requirements.txt
```


Install depencencies
```
pip install -r requirements.txt
```

Actions will be similar to the one below:

Create a virtual environment $ python3 -m venv /path/to/new/virtual/env
Install packages using $pip install <package> command
Save all the packages in the file with $pip freeze > requirements.txt. Keep in mind that in this case, requirements.txt file will list all packages that have been installed in virtual environment, regardless of where they came from
Pin all the package versions. You should be pinning your dependencies, meaning every package should have a fixed version.
Add requirements.txt to the root directory of the project. Done.
Install project dependencies
When if you’re going to share the project with the rest of the world you will need to install dependencies by running $pip install -r requirements.txt

To find more information about individual packages from the requiements.txt you can use $pip show <packagename>. But how informative the output is?
	

### Info

There is already a template with charts and layout that we could use in our application. It is inside HTML folder. It has to be inegrated into Django project.

---
---
---


## Documentation(links)

1. (movesole - pediatric therapists ) https://www.theseus.fi/bitstream/handle/10024/143390/Manselius_Lauri.pdf?sequence=1&isAllowed=y

2. (usability) https://www.theseus.fi/bitstream/handle/10024/155327/Ylikulju_Marko.pdf?sequence=1&isAllowed=y

3. (insole - hardware) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3444133/


## Ground Rules

### Meetings

1.	Meetings will be held in English. If you don’t know a word, ask another member to help.
2.	Fixed meeting time:  Wednesdays. 14:30 – 16:00 at Agora.
3.	Working with the status report (15 mins) in each meeting.
4.	Each member informs asap, if he cannot attend the meeting.

### Communication

5.	We will use WeChat to keep everybody up-to-date with our project. 
	Each member will check out WeChat once per day.
6.	Inform the team and leader asap, if you cannot make a deadline, have troubles with a task given to you or a problem is coming up.
7.	On Tuesday, each member writes a message on WeChat asking doubts/questions or simply saying “no questions”.

### Norms

8.	We help each other. If you are stuck, ask your team members for help.
9.	To prevent escalation, we address conflicts early on, before we get frustrated.
10.	We use Trello to monitor the progress/milestones.

### Decision making

11.	Decisions will be made only after hearing the opinion of each relevant member.
12.	It is not acceptable to withhold your opinion (“whatever you all think…”) and then later be against the decision made.
