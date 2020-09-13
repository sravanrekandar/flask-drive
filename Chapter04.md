# Flask-Drive Chapter 04: Deploying the app in cloud

So far you are running your application in your machine. This is not servable to others. Meaning, if you want another person to access your application, you need to deploy the application on to a cloud environment and make it available thorough a [URL](https://en.wikipedia.org/wiki/URL).

## Cloud providers

There are many cloud providers in the market. Naming a few below. You can explore and take advantage of the free resources they provide for learning purposes.

_Reference Article: [What are cloud providers](https://www.redhat.com/en/topics/cloud-computing/what-are-cloud-providers)_

- [AWS](https://aws.amazon.com/)
- [Azure](https://azure.microsoft.com/)
- [GCP - Google Cloud Platform](https://cloud.google.com/gcp)
- [Heroku](https://dashboard.heroku.com/) __WE will use this in this tutorial__
- [Digital Ocean](https://try.digitalocean.com/developerbrand)
- And there are many more. You can search on Google and find out the available options

For this tutorial, we will deploy our apps on [Heroku](https://dashboard.heroku.com/).

## Working on Heroku

- Create a free account on Heroku
- The UI might change time to time. Explore the pricing options, and other beginner tutorials on Heroku
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) on your machine

*_CLI: Command Line Interface_*

### Verify your installation

```bash
$ heroku --version
heroku/7.0.0 (darwin-x64) node-v8.0.0
```

### Heroku Login from your command line

```bash
$ heroku login
heroku: Press any key to open up the browser to login or q to exit
 ›   Warning: If browser does not open, visit
 ›   https://cli-auth.heroku.com/auth/browser/***
heroku: Waiting for login...
Logging in... done
Logged in as me@example.com
```

### Creating an application on heroku

_[Reference Article](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote)_

#### View the existing remote connections in your app

```bash
$ cd flask-drive
$ git remote -v
origin https://github.com/sravanrekandar/flask-drive.git (fetch)
origin https://github.com/sravanrekandar/flask-drive.git (push)
```

As you see here, I have one remote (Which is stored in a remote cloud location): [https://github.com/sravanrekandar/flask-drive.git](https://github.com/sravanrekandar/flask-drive.git). If you are following the previous tutorials, you must see your github repo when you execute the command.

### Staging and Prod applications

We will create two applications

- **Staging**: Few call it as _Non Prod_. We use this application for our development and testing purposes. We do not share the url of this application with the end users. If things break here, it is fine. Because we want to know the bugs and fix them.
- **Prod** Production application: This is where your application finally deployed before sharing it to users. If things break here, you will loose business. Thats why When your are confident of the application on Staging, you will push it to production

### Other strategies to test and deployment

Based on the complexity of the application, business and the team, you can organise the environments as below. We are not creating all the below in this tutorial, it is given for your reference.

- **Dev** Development Environment. The most recent code of your application runs here
- **Test** The most recent working version of your code runs here
- **UAT** User Acceptance Testing. You want some of your _selected users_ to test the application. You will use this environment for User Acceptance Testing.
- **Prod** Production. This is what you share to your customers

### Creating Staging application

Let us call our staging app **sravan-flask-drive-staging**. Feel free to replace my name with yours.

Goto [Heroku Dashboard](https://dashboard.heroku.com/apps) and create and app called **sravan-flask-drive-staging**

Let us connect the remote app (remotely deployed in cloud) to our local flask-drive app

```bash
$ heroku git:remote -a sravan-flask-drive-staging
set git remote heroku to https://git.heroku.com/sravan-flask-drive-staging.git
```

```bash
git remote -v
heroku  https://git.heroku.com/sravan-flask-drive-staging.git (fetch)
heroku  https://git.heroku.com/sravan-flask-drive-staging.git (push)
origin  https://github.com/sravanrekandar/flask-drive.git (fetch)
origin  https://github.com/sravanrekandar/flask-drive.git (push)
```

The name of the connection is heroku. We will have a conflict when we connect another (prod) environment from heroku.

In order to keep both the staging and prod remote connections separate, let us rename the connection from **heroku** to  **heroku-staging**

```bash
$ git remote rename heroku heroku-staging
```

```bash
git remote -v
heroku-staging  https://git.heroku.com/sravan-flask-drive-staging.git (fetch)
heroku-staging  https://git.heroku.com/sravan-flask-drive-staging.git (push)
origin  https://github.com/sravanrekandar/flask-drive.git (fetch)
origin  https://github.com/sravanrekandar/flask-drive.git (push)
```

### Creating Prod application

Let us call our staging app **sravan-flask-drive-prod**. Feel free to replace my name with yours.

Goto [Heroku Dashboard](https://dashboard.heroku.com/apps) and create and app called **sravan-flask-drive-prod**

Let us connect the remote app (remotely deployed in cloud) to our local flask-drive app

```bash
$ heroku git:remote -a sravan-flask-drive-prod
set git remote heroku to https://git.heroku.com/sravan-flask-drive-prod.git
```

```bash
$ heroku    https://git.heroku.com/sravan-flask-drive-prod.git (fetch)
heroku  https://git.heroku.com/sravan-flask-drive-prod.git (push)
heroku-staging  https://git.heroku.com/sravan-flask-drive-staging.git (fetch)
heroku-staging  https://git.heroku.com/sravan-flask-drive-staging.git (push)
origin  https://github.com/sravanrekandar/flask-drive.git (fetch)
origin  https://github.com/sravanrekandar/flask-drive.git (push)
```

Rename the connection **heroku** to **heroku-prod**

```bash
$ git remote rename heroku heroku-prod
```

```bash
git remote -v
heroku-prod https://git.heroku.com/sravan-flask-drive-prod.git (fetch)
heroku-prod https://git.heroku.com/sravan-flask-drive-prod.git (push)
heroku-staging https://git.heroku.com/sravan-flask-drive-staging.git (fetch)
heroku-staging https://git.heroku.com/sravan-flask-drive-staging.git (push)
origin https://github.com/sravanrekandar/flask-drive.git (fetch)
origin https://github.com/sravanrekandar/flask-drive.git (push)
```
