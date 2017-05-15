# [Image Mirror][imageMirror] [![Build Status](https://travis-ci.org/Trajanson/Image-Mirror.svg?branch=master)](https://travis-ci.org/Trajanson/Image-Mirror)
## By [The Data Incubator][theDataIncubator]

[Image Mirror][imageMirror] is a demonstration of a number of technologies in the Python [Flask][flask] ecosystem deployed via use of [Virtualenv][virtualenv], [Gunicorn][gunicorn], [Heroku][heroku], [Travis CI][travis], [Docker][docker], and Flask's native [Werkzeug testing client][werkzeug].

Image Mirror was developed using the [pep8][pep8] linter.

## Setup
######  Install Docker
Docker is not critically necessary to use ImageMirror. However, containerization is a recommended best practice.
- [For Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac?tab=description)
- [For Ubuntu](https://store.docker.com/editions/community/docker-ce-server-ubuntu)
- [For Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows?tab=description)

## Travis CI & Continuous Deployment
> “Continuous Integration doesn’t get rid of bugs, but it does make them dramatically easier to find and remove.”
<br/> - Martin Fowler, author and friend of that Kent Beck guy

[Travis][travis] is an easy to use build tool that smoothes the cycles of production development and deployment through its application of self-testing builds and automated deployment in a stable production environment.

This repository has been connected to Travis, so any accepted pull request will be tested and deployed to Heroku, if declared a passing build.

Using Travis is built in and is as easy as `$ git push`

![travisCIRepositorySwitch]

## Use of the App

Image Mirror takes a permissible upload file (within the set of ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'] files) and directly pipes the uploaded file back to the user.
#####  Landing Page
![landingPage]

#####  Piped Image Page
![loadedImage]

#####  Flash Error
Handy flash messages are available to users who encounter errors when using the application.
![handyError]

## Directions for Further Development

##### To run the app locally via Docker:
This option is convenient in that the Dockerfile installs an immediately-ready-for-use development environment.
- `$ chmod +x ./app.sh`
- `$ ./app.sh`

##### To run the app locally without Docker:
- `$ python run.py`

##### To use the linter:
- `$ pep8 --first <file_name_for_linting>`


##### Adding Code:
- `$ pip install -r requirements.txt && source app/bin/activate`
- Edit relevant files
- `$ deactivate && git push && open "https://image-mirror.herokuapp.com/"`


## Technologies Used
* [Docker][docker]
* [Flask][flask]
* [Gunicorn WSGI HTTP Server][gunicorn]
* [Heroku][heroku]
* [Pep8 Python Linter][pep8]
* [Travis CI][travis]
* [Virtualenv][virtualenv]
* [Werkzeug][werkzeug]

[landingPage]: ./docs/landing_page.png
[travisCIRepositorySwitch]: ./docs/travis_ci.png
[loadedImage]: ./docs/loaded_image.png
[handyError]: ./docs/handy_error.png

[imageMirror]: https://image-mirror.herokuapp.com/
[theDataIncubator]: https://www.thedataincubator.com/


[docker]: https://www.docker.com/
[flask]: http://flask.pocoo.org/
[gunicorn]: http://gunicorn.org/
[heroku]: https://www.heroku.com/
[pep8]: https://pep8.readthedocs.io/en/release-1.7.x/
[travis]: https://travis-ci.org/
[virtualenv]: http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
[Werkzeug]: http://werkzeug.pocoo.org/docs/0.12/test/
