# Flask-Drive Chapter 05: Templates

We had coded the html strings in app.py. If we want to add more content, our python files will jack up with HTML code.

We will separate the HTML code to ```templates/``` folder

Create a folder called ```templates``` and create the template files.

```bash
(env) $ mkdir templates
(env) $ touch templates/page-content.html
```

## Templates/page-template.html

Copy the [Bootstrap starter template](https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template) and add two variable expressions

1. title : ```{{title}}```
2. page_content : ```{{page_content}}```

We will use these variables in ```app/run.py```

```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

    <title>{{title}}</title>
</head>

<body>
    <div class="container">
        <h1>{{title}}</h1>
        <p>{{page_content}}</p>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous">
    </script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
        integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
        integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous">
    </script>
</body>

</html>
```

## app/run.py

```python
import os
from flask import Flask, render_template

template_dir = os.path.abspath('templates')
app = Flask(
    __name__,
    template_folder=template_dir
)


@app.route("/")
@app.route("/home/")
def home():
    """Home Page."""
    return render_template(
        'page-template.html',
        title="Home",
        page_content="Welcome to Home Page"
    )


@app.route("/about/")
def about():
    """About Page."""
    return render_template(
        'page-template.html',
        title="About",
        page_content="About us content goes here"
    )


@app.route("/contact/")
def contact():
    """Contact Page."""
    return render_template(
        'page-template.html',
        title="Contact",
        page_content="Contact us content goes here"
    )


@app.errorhandler(404)
def page_not_found(e):
    """Not Found Page."""
    return render_template(
        'page-template.html',
        title="Not Found",
        page_content="Seems you are lost. Go back to home page"
    )


if __name__ == "__main__":
    app.run()
```

## Check the below links to see the templates in action

- [http://127.0.0.1:8085/home/](http://127.0.0.1:8085/home/)
- [http://127.0.0.1:8085/about/](http://127.0.0.1:8085/about/)
- [http://127.0.0.1:8085/some-route/](http://127.0.0.1:8085/some-route/)

Under the hood, flask uses a template library called [Jinja](https://palletsprojects.com/p/jinja/)