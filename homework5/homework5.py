# 2.1 Vocabulary Review 

# 1. Git is a tool that allows you to track changes to your files locally while GitHub is a platform that hosts Git repositories and allows collaboration on software projects.

# 2. The terminal is the application that allows us to run shells while the command line is the area where you can input text such as commands.  

# 3. A local repository is a Git repository that stores project files, commit history, and branches locally. It contains the complete version history. The remote repository is also a git repository but it is hosted on a platform where multiple people can collaborate on one project.

# 4. Version Control allows you to track and manage changes to source code.

# 5. The staging area is where changes are gathered before they are fully committed. You are able to review work before finalizing it in the repository.

# 6. Git add is a command that adds your work to the staging area from the working directory.

# 7. Git commit takes your work from the staging area and saves it to your local repository.

# 8. Git push uploads everything from the local repository to a remote repository.

# 9. Git status is a command that allows you to check the status of your repository.

# 10. Git pull command is used to grab the newest chanbes from the remote repository.

# 11. Pwd stands for print working directory and it displays the entire path of your current working directory from the root directory. 

# 12. ls stands for list and it lists all the files and folders in your directory.

# 13. cd stands for change directory and it allows you to change the directory or folder you're in.

# 14. nano allows you to open a file in your terminal.

# 15. Touch allows you to make a file in a folder in your terminal.

# 16. The mv command is used to move or rename files and directories.

# 17. The rm command removes or deletes files and directories.

# 18. cat stands for concatenate and it displays the contents of a file.

# 2.2 A Directory Tree

# Questions

# 1. The pwd command will tell me what my current working directory is.

# 2. The ls command will list all the files in my current working directory.

# 3. The cd command: cd ../brianna_repo. To pull the latest changes: git pull.

# 4. cp homework.py ../judy_decal/homework/

# 5. cd ∼/python_decal/brianna_repo/homework/

# 6. nano homework.py

# 7. git add homework.py git commit - m "Finished this week's homework" git push

# 8. The commands to resolve this error and push my homework would be: git pull origin main and then git add . git commit -m "Fixed" and git push origin main. The error likely means that Judy forgot to pull changes she had made to her local repository before trying to git push. 

# 9. The absolute path that will allow me to move to Recents/ is ~/Recent/

# 2.3 Draw Your Directory Tree

# 3 Homework 3 Review

# 3.1 Data Types

def checkDataType(val):
	data_types = {
		int: 'int',
		float: 'float',
		bool: 'bool',
		str: 'str',
		list: 'list',
		dict: 'dict'
	}
	return data_types.get(type(val), 'unknown')

# 3.2 Conditionals

def evenOrOdd(number):
	if number % 2 == 0:
		return 'Even'
	else:
		return 'Odd'
# 4 Loops

def sumWithLoop(numbers):
	total = 0
	for num in numbers:
		total += num
	return total

# 5 Homework 4 Review

# 5.1 Lists

def duplicateList(lst):
	result = []
	for item in lst:
		result.append(item)
		result.append(item)
	return result

# 5.2 Debugging

# The error is the : after the function

def square(num):
	return num * num

# Favorite Function

def square(num):
	return num * num
print(square(2))
