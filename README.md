## vision-writer-py

![Oberon](https://avatars0.githubusercontent.com/u/45834871?s=400&u=44d9c2a8ef57254d90a4127fd0b1fdb6f705be9b&v=4)

Made with love from Oberon Studios

### About

Vision Writer is a PDF to Txt converter, build using Google Cloud Vision API. It is implemented in Python, using Flask framework to bootstrap api. 

### Architecture and app flow

![Diagram](https://yuml.me/diagram/scruffy/class/[note:%20Vision%20Writer%7Bbg:cornsilk%7D],[user]-%3E[Py%20Server],[Py%20Server]-%3E[Vision%20API],[Vision%20API]-%3E[Py%20Server],[Py%20Server]-%3E[User])

First, user submits post request to Flask server with pdf as a payload. Server converts pdf to jpg(multiple pages), and sends converted pictures to Google Cloud Vision API, page by page. On return, server extracts text data, and writes it to a text file, appedning page after page. Name of the txt file, is SHA1 hash of current timestamp. Finally, server responsd with txt file as attachment.

***

### Build with:

- Flask (Python)
- Google Cloud Vision API

***

## Documentation

### Prereqs

- Python 3.5.x or newer
- Google Cloud account with Cloud Vision API enabled [Read more](https://cloud.google.com/vision/)

### Installation

First, follow [this](https://cloud.google.com/vision/docs/quickstart-client-libraries) guide to get your Google credentials, and save them in root directory as config.json

Configure virtual environment (In this example, I am using [Virtualenv](https://virtualenv.pypa.io/en/stable/), but you are free to do it your own way)

First, check Python version installed

On Linux, one of the possible ways is to enter <code>$ /usr/bin/python</code> in your terminal and hit <code>Tab</code> key twice

This would show all the available vesrsions 

```
python             python3            python3.6m         python3m
python2            python3.6          python3.6m-config  python3m-config
python2.7          python3.6-config   python3-config     
```

Now, create environment with desired version of Python specified, as <code>--python=PY_VERSION</code> (Note: Django 2.x.. requres Python 3.x.. version!) 

```
$ virtualenv MY_ENV --python=python3.6
```

Activate your environment, and install dependencies

Note: If your environment name differs from <code>MY_ENV</code>, you would have to use <code>source YOUR_ENV_NAME/bin/activate</code> as first command

```
$ source activate &&  pip install -r requirements_dev.txt
```

### Run

Set flask server file, and google config file locations as env variables 
```
export FLASK_APP=server.py
export GOOGLE_APPLICATION_CREDENTIALS="<path>/config.json"
```
For permanent affect, make sure to add this two lines to your ~/.bash_profile

Finally, you are ready to launch your app (-p 3000 option is for custom port number)
```
flask run -h localhost -p 3000
```
***