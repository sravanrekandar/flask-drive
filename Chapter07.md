# Flask-Drive Adding Navbar and page contents

You already have Jinja installed as a Flask dependency. but to add the lbrary explicitly, add the below text to ```requirements.txt```

```text
Jinja2==2.11.2
```

and install

```bash
pip install -r requirements.txt
```

## Preparing Navbar

```bash
touch templates/nav.html
```

Add the below contents to ```templates/nav.html```

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">Flask Drive</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item {% if title=='Home' %}active{% endif %}">
                <a class="nav-link" href="/">
                    Home <span class="sr-only">(current)</span>
                </a>
            </li>
            <li class="nav-item {% if title=='About' %}active{% endif %}">
                <a class="nav-link" href="/about">About Us</a>
            </li>
            <li class="nav-item {% if title=='Contact' %}active{% endif %}">
                <a class="nav-link" href="/contact">Contact Us</a>
            </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
    </div>
</nav>
```

### Things to notice

Example: [Jinja](https://jinja.palletsprojects.com/en/2.11.x/api/#basics) conditional expression

```bash
{% if 42 is prime %}
    42 is a prime number
{% else %}
    42 is not a prime number
{% endif %}
```

In ```nav.html```, For each of the menu items, we have a Jinja expressions

```html
<li class="nav-item {% if title=='Home' %}active{% endif %}">
    ....
</li>
```

Jinja expression is...

```html
{% if title=='Home' %}active{% endif %}
```

This means if the title value supplied by ```run.py``` matches Home, add this ```active``` text.

## Changing the page content

```bash
touch templates/about.html
```

Add the bellow contents

```html
<table class="table">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Handle</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
        </tr>
        <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
        </tr>
        <tr>
            <th scope="row">3</th>
            <td>Larry</td>
            <td>the Bird</td>
            <td>@twitter</td>
        </tr>
    </tbody>
</table>
```

## create Home template

```bash
touch templates/home.html
```

Add the below content

```html
<h1>Home Content</h1>
<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
    standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a
    type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing
    Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of
    Lorem Ipsum.</p>
```

### Not found page template

```bash
touch templates/not-found.html
```

```html
<div class="row">
    <div class="error-template">
      <h1>Oops!</h1>
      <h2>404 Not Found</h2>
      <div class="error-details">
    Sorry, an error has occured, Requested page not found!
      </div>
      <div class="error-actions">
    <a href="" class="btn btn-primary">
        <i class="icon-home icon-white"></i> Take Me Home </a>
    <a href="" class="btn btn-default">
        <i class="icon-envelope"></i> Contact Support </a>
      </div>
  </div>
    </div>
```

## create Contact template

```bash
touch templates/contact.html
```

Add the below content

```html
<!--Section: Contact v.2-->
<section class="mb-4">
    <!--Section description-->
    <p class="text-center w-responsive mx-auto mb-5">Do you have any questions? Please do not hesitate to contact us
        directly. Our team will come back to you within
        a matter of hours to help you.</p>

    <div class="row">

        <!--Grid column-->
        <div class="col-md-9 mb-md-0 mb-5">
            <form id="contact-form" name="contact-form" action="mail.php" method="POST">

                <!--Grid row-->
                <div class="row">

                    <!--Grid column-->
                    <div class="col-md-6">
                        <div class="md-form mb-0">
                            <input type="text" id="name" name="name" class="form-control">
                            <label for="name" class="">Your name</label>
                        </div>
                    </div>
                    <!--Grid column-->

                    <!--Grid column-->
                    <div class="col-md-6">
                        <div class="md-form mb-0">
                            <input type="text" id="email" name="email" class="form-control">
                            <label for="email" class="">Your email</label>
                        </div>
                    </div>
                    <!--Grid column-->

                </div>
                <!--Grid row-->

                <!--Grid row-->
                <div class="row">
                    <div class="col-md-12">
                        <div class="md-form mb-0">
                            <input type="text" id="subject" name="subject" class="form-control">
                            <label for="subject" class="">Subject</label>
                        </div>
                    </div>
                </div>
                <!--Grid row-->

                <!--Grid row-->
                <div class="row">

                    <!--Grid column-->
                    <div class="col-md-12">

                        <div class="md-form">
                            <textarea type="text" id="message" name="message" rows="2"
                                class="form-control md-textarea"></textarea>
                            <label for="message">Your message</label>
                        </div>

                    </div>
                </div>
                <!--Grid row-->

            </form>

            <div class="text-center text-md-left">
                <a class="btn btn-primary" onclick="document.getElementById('contact-form').submit();">Send</a>
            </div>
            <div class="status"></div>
        </div>
        <!--Grid column-->

        <!--Grid column-->
        <div class="col-md-3 text-center">
            <ul class="list-unstyled mb-0">
                <li><i class="fas fa-map-marker-alt fa-2x"></i>
                    <p>San Francisco, CA 94126, USA</p>
                </li>

                <li><i class="fas fa-phone mt-4 fa-2x"></i>
                    <p>+ 01 234 567 89</p>
                </li>

                <li><i class="fas fa-envelope mt-4 fa-2x"></i>
                    <p>contact@mdbootstrap.com</p>
                </li>
            </ul>
        </div>
        <!--Grid column-->

    </div>

</section>
<!--Section: Contact v.2-->
```

## Replace page content part in ```templates/page-template.html```

Old content

```html
<p>{{page_content}}</p>
```

New content
```html

```