# task-checker

A program which allows an administrator to create a user, assign them tasks and keep track of all user's tasks. The user can then track their own task status and mark it as complete.


## Getting started

For this program to run you need to save it with the other two files: tasks.txt and user.txt. The user file already has a user: admin and password adm1n. The tasks file has two example tasks.

Use the python command followed by the name of the program to start the task-checker.
```
>python task_manager.py
Please Please insert your user name: admin
Please insert your password: adm1n
Your login was successful.
Please select one of the following options:
        r - register user
        a - add a task
        va - view all tasks
        vm - view my tasks
        s - statistics
        gr - generate reports
        e - exit
 ```
 
 ## How to use it
 
 To start with you will be loging in as an administrator using admin and adm1n as shown above. You then have the option of creating a new user by selecting __r- register a new user__. You can login as a new user by starting the program again. Admin is the only one that can create new users, so the menus will look different by loging in as a admin or as another user.
 
 ### Adding tasks
 
 When you select to add a task, some questions will pop to describe the task (example below). This will then be saved into the task file, to be viewed later.
 ```
 >a
Which user do you want to assign the task to? admin
What is the title of the task? Do admin stuff
Describe the task: Do what admin people do.
Due date for the task to be complete: 21/02/2021
```
After you finish, you will be taken to the main menu again.

### Viewing tasks

Selecting va will allow visualising all existing tasks and vm shows the tasks assigned to the user only.
The tasks are shown as per example below.

```
>va
 The following task is assigned to:      admin
                Register Users with taskManager.py
            Task description:    Use taskManager.py to add the usernames and passwords for all team members that will be using this program.
            Due date:    10 Oct 2019
            Date of assigment:   20 Oct 2019
            Completed:   No
```

### Generating reports and viewing statistics

Generating reports will create two new documents: one with information regarding the users and another one with descriptive data about the tasks.
__Only after these documents have been generated you can view the statistics information on screen.__
An example of the statistics option is shown below:

s
Total number of users: 1

Total number of tasks: 2

```
>s

                User: admin



                Tasks assigned to the user: 2

                Percentage of tasks assigned to the user: 100.0%

                Percentange of tasks for this user that have been completed: 0.0%

                Percentage of tasks for this user that are not yet completed: 100.0 %





                 TASKS REPORT



            Total number of tasks:       2

            Number of completed tasks:   0

            Number of tasks that are still incomplete:   2

            Number of tasks which are overdue:   0

            Percentage of incomplete tasks:      100.0%

            Percentafe of overdue tasks:         0.0%


 ```
 
 ### Exit
 
 Pressing exit will take you to the login screen again.
 
 
 
