# ***** TASK MANAGER FUNCTIONS ******

def user_exists (user):
    #checks if user exists
    user_exists = False
    with open ('user.txt', 'r+') as user_file:
        for line in user_file:
            line = line.split(', ')
            if line[0] == user:
                user_exists = True

    return user_exists



def user_reg (user, password, pass_confirmation):
    #This function allows the creation of a new user and adds it to the file user.txt
    
    while user_exists(user) == True:
        print("This user name already exsists.")
        user = input("Please create your user name: ")

    while password != pass_confirmation:
        print("Your password entries do not match, please try again.")
        password = input ("Please create a password: ")
        pass_confirmation = input ("Please confirm your password: ")

    with open('user.txt', 'a+') as user_file:
        line = user + ", " + password
        user_file.write("\n" + line)


def menu_display (user_name):
    #This function displays the menu and returns the menu option selected by the user
    
    if user_name == "admin":
        menu_options = input('''Please select one of the following options:
        r - register user
        a - add a task
        va - view all tasks
        vm - view my tasks
        s - statistics
        gr - generate reports
        e - exit\n''')
       
        
    else:
        menu_options = input('''Please select one of the following options:
        a - add a task
        va - view all tasks
        vm - view my tasks
        e - exit\n''')

    return menu_options

def add_task (user, title, task, due_date, current_date = "Today", is_completed = "No"):
    #This function creates a new task and adds it to the tasks.txt file
    #It automatically sets the current date as "Today" and the status as not completed

    with open('tasks.txt', 'a+') as tasks_file:
        tasks_file.write(f"\n{user}, {title}, {task}, {due_date}, {current_date}, {is_completed}")



def check_user ():
    #check if user selected to view or assign task exists
    pass



def view_all ():
    #This function displays all tasks in user-friendly manner
    with open('tasks.txt', 'r+') as tasks_file:
        for line in tasks_file:
            task_user, task_title, task, due_date, current_date, is_completed = line.split(", ")
            print(f''' The following task is assigned to:\t {task_user}
            \t{task_title}
            Task description:\t {task}
            Due date:\t {due_date}
            Date of assigment:\t {current_date}
            Completed:\t {is_completed}''')



def view_mine ():
    #This function prints the user's tasks in a user friendly way
     with open('tasks.txt', 'r+') as tasks_file:
        tasks = []
        for line in tasks_file:
          task_user, task_title, task, due_date, current_date, is_completed = line.split(", ")
          if user_name == task_user:
              
              task_title == line[1]
              task == line[2]
              due_date == line[3]
              current_date == line[4]
              is_completed == line[5]
              
              tasks.append(f'''Task name:\t {task_title}
            Task description:\t {task}
            Due date:\t {due_date}
            Date of assigment:\t {current_date}
            Completed:\t {is_completed}''')

        counter = 0
        for element in tasks:
            print(f"TASK ID: {counter}")
            print(element)
            counter = counter + 1



def read_tasks():
    #This function turns the tasks in the tasks file into a list of dictionaries
    #Each dictionary contains an element of the task identified with a same name key

    with open('tasks.txt', 'r+') as tasks_file:
        formatted_tasks = []
        for line in tasks_file:
            task_user, task_title, task, due_date, current_date, is_completed = line.split(", ")
            single_tasks = {'task_user': task_user, 'task_title': task_title, 'task': task, 'due_date': due_date, 'current_date': current_date, 'is_completed': is_completed}
            single_tasks["is_completed"] = is_completed.strip("\n")
            formatted_tasks.append(single_tasks)
        
    return formatted_tasks



def save_tasks(tasks):
    # a single task looks like
    # { 'task_user': task_user, 
    #   'task_title': task_title, 
    #   'task': task, 
    #   'due_date': due_date, 
    #   'current_date': current_date, 
    #   'is_completed': is_completed}

    #This function writes and saves new tasks
    with open('tasks.txt', 'w+') as tasks_file:
        for element in tasks:
            user = element['task_user']
            title = element['task_title']
            task = element['task']
            due_date = element['due_date']
            current_date = element['current_date']
            is_completed = element['is_completed']

            tasks_file.write(f"{user}, {title}, {task}, {due_date}, {current_date}, {is_completed}\n")


def user_tasks_reader(all_tasks, user):
    #This function returns all the tasks of a user and puts them in a list
    user_task_list = []
    for element in all_tasks:
        if element['task_user'] == user:
            user_task_list.append(element)

    return user_task_list




#  ******MAIN PROGRAM******


# Asking the user to enter their login details
user_name = ""
login = False

user_file = open('user.txt', 'r+')

   
while True:
    if login == False:
        user_file.seek(0) #This reads the file from the beginning in case a wrong user/password was inserted
        user_name = input("Please insert your user name: ")
        password_enter = input("Please insert your password: ")

        for line in user_file:
            valid_name, valid_pass = line.replace("\n", "").split(", ")

            if  user_name == valid_name and password_enter == valid_pass:
                login = True
            
        if login == True:
            print("Your login was successful.")
        else:
            print("You have not entered a valid name or password!")
    else:
        # Displaying task menu options to the user
        menu_options = menu_display (user_name)


        # The following code allows the user to create a new user

        if menu_options == "r":
            if user_name == "admin":

                user = input ("Please create your user name: ")
                password = input ("Please create a password: ")
                pass_confirmation = input ("Please confirm your password: ")

                user_reg(user, password, pass_confirmation)
                print("A new user and password have been created")

            else:
                print("You do not have access to this option, please select another option.")

        # The following code allows the user to create a new task and add it to the tasks file

        elif menu_options == "a":
            
            task_user = input("Which user do you want to assign the task to? ")
            task_title = input("What is the title of the task? ")
            task = input("Describe the task: ")
            due_date = input("Due date for the task to be complete: ")

            new_task = add_task(task_user, task_title, task, due_date)
            

        # The following code allows the user to read all tasks on the tasks file

        elif menu_options == "va":
            alltasks = view_all()



        # The following code allows the user to view the tasks that are assigned to their username

        elif menu_options == "vm":
        
            mytasks = view_mine() #This prints the user's tasks in a user friendly way
        
            all_tasks = read_tasks() #This returns all tasks within the task file in a list of dictionaires

            user_tasks = user_tasks_reader(all_tasks, user_name) #This returns a list of dictionaires with only the user's name


            task_no = int(input("Which task would you like to edit? \n Input the task ID number or -1 to go back to the main menu: "))

        
            if task_no != -1:
                is_completed = input("Has your task been completed? (yes/no)").lower()
            
                if is_completed == "yes":
                    selected_task = user_tasks[task_no]
                    selected_task["is_completed"] = "Yes"
                    print("Your task has been updated.")
                
            
                
                elif is_completed  == "no":
                    edit_date = input("Would you like to change the by date? (yes/no)").lower()
                    if edit_date != "no":
                        selected_task = user_tasks[task_no]
                        selected_task["due_date"] = input("New due date: ")
                        print("Your task has been updated.")

                    edit_user = input("Would you kike to change the user name to which this task is assigned to?").lower()
                    if edit_user != "no":
                        selected_task = user_tasks[task_no]
                        selected_task["task_user"] = input("User name for this task: ")
                        print("Your task has been updated")

            save_tasks(all_tasks) #This will re-write the tasks file with the intended change   



        #The follwing code allows the admin user to have access to the statistics page

        elif menu_options == "s":
            with open('user_overview.txt', 'r+') as user_stats_file:
                for line in user_stats_file:
                    print(line)
            
            print('\n')
            
            with open('task_overview.txt', 'r+') as task_overview:
                for line in task_overview:
                    print(line)


        #The following code allows the admin user to generate reporting documents
    

        elif menu_options == "gr":
            task_overview = open('task_overview.txt', 'w+')
            user_overview = open('user_overview.txt', 'w+')
        
            all_tasks = read_tasks()
            #a single task looks like
            # { 'task_user': task_user, 
            #   'task_title': task_title, 
            #   'task': task, 
            #   'due_date': due_date, 
            #   'current_date': current_date, 
            #   'is_completed': is_completed}

            total_tasks = 0
            complete_tasks = 0
            incomplete_tasks = 0
            overdue_checker = 0

            for element in all_tasks:
                total_tasks = total_tasks + 1
                
                if element['is_completed'] == "Yes":
                    complete_tasks = complete_tasks + 1
                elif element["is_completed"] == "No":
                    incomplete_tasks = incomplete_tasks +1
                elif element['due_date'] != "Today":
                    overdue_checker = overdue_checker +1
            
            percentage_incomplete = (incomplete_tasks/total_tasks)*100
            percentage_overdue = (overdue_checker/total_tasks)*100
            
            task_overview.write(f''' \t \t TASKS REPORT\n
            Total number of tasks:\t {total_tasks}
            Number of completed tasks:\t {complete_tasks}
            Number of tasks that are still incomplete:\t {incomplete_tasks}
            Number of tasks which are overdue:\t {overdue_checker}
            Percentage of incomplete tasks:\t {percentage_incomplete}%
            Percentafe of overdue tasks: \t {percentage_overdue}%''')

            user_file.seek(0)

            no_of_users = 0
            user_tasks_stats = {} #dictionairy of dictionaries with a user as a primary key and tasks counts second

            for line in user_file:
                no_of_users = no_of_users + 1
                line = line.split(', ')
                user_tasks_stats[line[0]] = {'task_count': 0, 'tasks_completed': 0, 'incomplete': 0 }

            user_overview.write(f'''Total number of users: {no_of_users}\nTotal number of tasks: {len(all_tasks)}\n\n''')

            for user in user_tasks_stats:
                user_tasks_list = user_tasks_reader(all_tasks, user)
                user_tasks_stats[user]['task_count'] = len(user_tasks_list)
                
                for task in user_tasks_list:
                    if task['is_completed'] == "Yes":
                        user_tasks_stats[user]['tasks_completed'] = user_tasks_stats[user]['tasks_completed'] + 1
                
                user_tasks_stats[user]['incomplete'] = user_tasks_stats[user]['task_count'] - user_tasks_stats[user]['tasks_completed']
                
                user_overview.write(f'''\t\tUser: {user}\n
                Tasks assigned to the user: {user_tasks_stats[user]['task_count']}
                Percentage of tasks assigned to the user: {((user_tasks_stats[user]['task_count'])/(len(all_tasks)))*100}%
                Percentange of tasks for this user that have been completed: {((user_tasks_stats[user]['tasks_completed'])/(user_tasks_stats[user]['task_count']))*100}%
                Percentage of tasks for this user that are not yet completed: {((user_tasks_stats[user]['incomplete'])/(user_tasks_stats[user]['task_count']))*100} % \n\n''')
                

            task_overview.close()
            user_overview.close()
        

        elif menu_options == "e":
            login = False

