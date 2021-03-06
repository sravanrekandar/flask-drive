- [Flask-Drive Chapter 01: Create basic application and upload to github](Chapter01.md#flask-drive-chapter-01-create-basic-application-and-upload-to-github)
  - [Create a directory for your experiment](Chapter01.md#create-a-directory-for-your-experiment)
  - [Initiate Git repository](Chapter01.md#initiate-git-repository)
  - [```touch``` command to create files in unix based systems](Chapter01.md#touch-command-to-create-files-in-unix-based-systems)
  - [```type``` command to create files in windows](Chapter01.md#type-command-to-create-files-in-windows)
  - [Create README.md and enter some text in the file](Chapter01.md#create-readmemd-and-enter-some-text-in-the-file)
  - [Check the available files in your folder(aka directory)](Chapter01.md#check-the-available-files-in-your-folderaka-directory)
    - [list all contents with details](Chapter01.md#list-all-contents-with-details)
    - [list all files/folders](Chapter01.md#list-all-filesfolders)
    - [list on the file names in multiple lines](Chapter01.md#list-on-the-file-names-in-multiple-lines)
    - [List the contents of .git/](Chapter01.md#list-the-contents-of-git)
  - [Committing the changes](Chapter01.md#committing-the-changes)
    - [Check the status of your git repo](Chapter01.md#check-the-status-of-your-git-repo)
    - [Stage the changes to commit](Chapter01.md#stage-the-changes-to-commit)
    - [Commit the staged changes with a message](Chapter01.md#commit-the-staged-changes-with-a-message)
  - [Track the progress with ```git log``` command](Chapter01.md#track-the-progress-with-git-log-command)
  - [Create Python Virtual Environment](Chapter01.md#create-python-virtual-environment)
    - [Check python version](Chapter01.md#check-python-version)
    - [Create a virtual environment](Chapter01.md#create-a-virtual-environment)
      - [Using python's native _venv_](Chapter01.md#using-pythons-native-venv)
      - [Using pip's _virtualenv_ for python < 3.3](Chapter01.md#using-pips-virtualenv-for-python--33)
    - [Environment folder](Chapter01.md#environment-folder)
  - [Activating the virtual environment](Chapter01.md#activating-the-virtual-environment)
    - [For unix based OS](Chapter01.md#for-unix-based-os)
    - [For windows OS](Chapter01.md#for-windows-os)
    - [Deactivating environment](Chapter01.md#deactivating-environment)
  - [Preventing git to track the environment folder](Chapter01.md#preventing-git-to-track-the-environment-folder)
    - [Add ```.gitignore``` file](Chapter01.md#add-gitignore-file)
    - [Checking the repo status](Chapter01.md#checking-the-repo-status)
    - [Stage and Commit the changes](Chapter01.md#stage-and-commit-the-changes)
  - [Enhancing .gitignore](Chapter01.md#enhancing-gitignore)
  - [Install Flask dependency](Chapter01.md#install-flask-dependency)
    - [Getting the installed package list](Chapter01.md#getting-the-installed-package-list)
    - [Writing the dependency modules list the ```requirements.txt```](Chapter01.md#writing-the-dependency-modules-list-the-requirementstxt)
  - [Starting Flask script](Chapter01.md#starting-flask-script)
  - [Start Flask server app](Chapter01.md#start-flask-server-app)
    - [Using the flask app in a browsers](Chapter01.md#using-the-flask-app-in-a-browsers)
  - [Creating Github repository](Chapter01.md#creating-github-repository)
  - [Connecting remote to out local repo](Chapter01.md#connecting-remote-to-out-local-repo)
  - [Pushing your changes to remote repo](Chapter01.md#pushing-your-changes-to-remote-repo)
  - [Deleting the local repository and fetching from github](Chapter01.md#deleting-the-local-repository-and-fetching-from-github)
    - [Deactivate before you come out of the folder](Chapter01.md#deactivate-before-you-come-out-of-the-folder)
    - [Delete the folder](Chapter01.md#delete-the-folder)
    - [Cloning the cloud repository to your local machine](Chapter01.md#cloning-the-cloud-repository-to-your-local-machine)
  - [Creating virtual environment with name 'env'](Chapter01.md#creating-virtual-environment-with-name-env)
  - [Install dependencies with requirements.txt](Chapter01.md#install-dependencies-with-requirementstxt)
  - [Starting the application](Chapter01.md#starting-the-application)
- [Flask-Drive Chapter 02: Flask App routes - Serving HTML pages](Chapter02.md#flask-drive-chapter-02-flask-app-routes---serving-html-pages)
  - [Explanation: Two routes in this app](Chapter02.md#explanation-two-routes-in-this-app)
  - [Serving HTML pages with header](Chapter02.md#serving-html-pages-with-header)
    - [HTML: Hyper Text Markup language](Chapter02.md#html-hyper-text-markup-language)
      - [About page](Chapter02.md#about-page)
      - [Contact Page (Not found)](Chapter02.md#contact-page-not-found)
    - [Code explanation - Route aliases](Chapter02.md#code-explanation---route-aliases)
  - [Adding Contact Page and Not found page with Header.](Chapter02.md#adding-contact-page-and-not-found-page-with-header)
    - [Contact pge is handled now](Chapter02.md#contact-pge-is-handled-now)
    - [Not found is also handled nicely](Chapter02.md#not-found-is-also-handled-nicely)
- [Flask-Drive Chapter 03: Automating Development: Auto Reload Using Flask](Chapter03.md#flask-drive-chapter-03-automating-development-auto-reload-using-flask)
  - [Setting environmental variables](Chapter03.md#setting-environmental-variables)
    - [For Unix based systems](Chapter03.md#for-unix-based-systems)
    - [For windows](Chapter03.md#for-windows)
    - [Starting the app](Chapter03.md#starting-the-app)
    - [Making changes in Home Page contents](Chapter03.md#making-changes-in-home-page-contents)
  - [Keeping the app start commands in a file (Unix Systems)](Chapter03.md#keeping-the-app-start-commands-in-a-file-unix-systems)
    - [Enabling the file to get executed](Chapter03.md#enabling-the-file-to-get-executed)
    - [Run the app using the start script](Chapter03.md#run-the-app-using-the-start-script)
  - [Keeping the app start commands in a file (Windows)](Chapter03.md#keeping-the-app-start-commands-in-a-file-windows)
    - [Run the app using the start script (Windows)](Chapter03.md#run-the-app-using-the-start-script-windows)
  - [Sequence of steps in automated script](Chapter03.md#sequence-of-steps-in-automated-script)
- [Flask-Drive Chapter 04: Deploying the python app in heroku cloud](Chapter04.md#flask-drive-chapter-04-deploying-the-python-app-in-heroku-cloud)
  - [Cloud providers](Chapter04.md#cloud-providers)
  - [Working on Heroku](Chapter04.md#working-on-heroku)
    - [Verify your installation](Chapter04.md#verify-your-installation)
    - [Heroku Login from your command line](Chapter04.md#heroku-login-from-your-command-line)
    - [Creating an application on heroku](Chapter04.md#creating-an-application-on-heroku)
    - [Staging and Prod applications](Chapter04.md#staging-and-prod-applications)
    - [Other strategies to test and deployment](Chapter04.md#other-strategies-to-test-and-deployment)
      - [View the existing remote connections in your app](Chapter04.md#view-the-existing-remote-connections-in-your-app)
    - [Creating Staging application](Chapter04.md#creating-staging-application)
    - [Creating Prod application](Chapter04.md#creating-prod-application)
    - [Pushing your local changes to Heroku Staging App](Chapter04.md#pushing-your-local-changes-to-heroku-staging-app)
      - [Output logs](Chapter04.md#output-logs)
    - [Configuring deployment scripts](Chapter04.md#configuring-deployment-scripts)
      - [Install GUnicorn module](Chapter04.md#install-gunicorn-module)
      - [Create few files required for configuration](Chapter04.md#create-few-files-required-for-configuration)
        - [For windows users](Chapter04.md#for-windows-users)
      - [Test the setup locally](Chapter04.md#test-the-setup-locally)
      - [Test the setup locally on windows](Chapter04.md#test-the-setup-locally-on-windows)
        - [Output](Chapter04.md#output)
      - [Deploy the changes to heroku staging](Chapter04.md#deploy-the-changes-to-heroku-staging)
        - [output logs](Chapter04.md#output-logs1)
      - [Open the deployed app](Chapter04.md#open-the-deployed-app)
      - [Deploy the changes to heroku prod](Chapter04.md#deploy-the-changes-to-heroku-prod)
    - [Commit the changes to github](Chapter04.md#commit-the-changes-to-github)
- [Flask-Drive Chapter 05: Cleanup environment](Chapter05.md#flask-drive-chapter-05-cleanup-environment)
  - [Cleaning up requirements.txt](Chapter05.md#cleaning-up-requirementstxt)
  - [Adding logging to start_dev.sh](Chapter05.md#adding-logging-to-startdevsh)
- [Flask-Drive Chapter 05: Templates](Chapter06.md#flask-drive-chapter-05-templates)
  - [Templates/page-template.html](Chapter06.md#templatespage-templatehtml)
  - [app/run.py](Chapter06.md#apprunpy)
  - [Check the below links to see the templates in action](Chapter06.md#check-the-below-links-to-see-the-templates-in-action)
