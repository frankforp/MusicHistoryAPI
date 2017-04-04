
MusicHistory-api
===============

## Description

This is a REST API to be used to house a collection of Music (Artists, Genres, Songs, and Albums)

## Installation

1.  Make sure you have Python 3.6.0 installed. See instructions for download here:
    https://www.python.org/downloads/

2.  Virtualenv is probably what you want to use during development, and if you have shell access to your production
    machines, you’ll probably want to use it there, too.

3.  Requirements.txt contains all the external dependencies for the api.

4.  Go into the project's root folder and follow the "How to Run" instructions below.

## Requirements
    * Django==1.10.5
    * djangorestframework==3.5.3

## How to Run

### MAC
Create a virtual environment
```
python -m venv venv
```
Activate the virtual environment
```
source venv/bin/activate
```
Install all dependencies in requirements.txt
```
pip install -r requirements.txt
```
To deactivate the virtual environment
```
deactivate
```

### WINDOWS
Install virtual env and wrapper
```
pip install virtualenvwrapper-win
```
Create a virtual environment
```
mkvirtualenv myproject
```
Activate the virtual environment
```
workon myproject
```
Install all dependencies in requirements.txt
```
pip install -r requirements.txt
```
To deactivate the virtual environment
```
deactivate
```

### After creating a virtualenv
Change into the MusicHistory directory
```
cd MusicHistory/
```
Run the migrations script to create the database
```
./manage.py migrate
```
Now, run the server
```
./manage.py runserver
```
> Performing system checks...<br><br>
> System check identified no issues (0 silenced).<br>
> Django version 1.10.5, using settings 'bangazon.settings'<br>
> Starting development server at http://127.0.0.1:8000/<br>
> Quit the server with CONTROL-C.<br>

Go to localhost in browser
```
http://127.0.0.1:8000/
```
To login as admin
```
username: admin
password: password123
```

## How to use

### Collections
```
* GET - http://127.0.0.1:8000/artists           returns all artists
* GET - http://127.0.0.1:8000/albums            returns all albums
* GET - http://127.0.0.1:8000/songs             returns all songs
* GET - http://127.0.0.1:8000/genres            returns all genres
```

### Members
```
* GET - http://127.0.0.1:8000/artists/<id>          returns an artist by id
* GET - http://127.0.0.1:8000/albums/<id>           returns an album by id
* GET - http://127.0.0.1:8000/songs/<id>            returns a song by id
* GET - http://127.0.0.1:8000/genres/<id>           returns a genre by id
```

| *Parameters* | *Valid Options* | *Description*              |
|------------|---------------|--------------------------|
| format     | json          | the data type to return. |

## Example
```
// http://127.0.0.1:8000/artists/1/?format=json

{
  "url": "http://127.0.0.1:8000/artists/1/?format=json",
  "ArtistName": "Milli Vanilli"
}
```

- [Nick Chemsak](https://github.com/nchemsak)

