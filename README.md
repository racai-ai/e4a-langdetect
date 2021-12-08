## Language identificator for Enrich4All
This is a Python 3 application and Docker container for language identification, based on the `langdetect` PyPI package to which we have added the Luxembourgish `lb` profile. It works for the languages of the project, namely German, French, Luxembourgish, Romanian, Danish and English. If text in other language is supplied, the ISO 639-1 language code is returned.

## Docker container
This repository was deployed in a Docker container available on [Docker Hub](https://hub.docker.com/r/raduion/e4alangdetect). Issue a `docker pull raduion/e4alangdetect:1.0` to get it.

## How to use
Test the installation (you have to `pip install pytest` first):

`pytest -v tests`

In Python 3:

```python
from enrichforall import E4ALangDetect

ld = E4ALangDetect('This is English. Got it or do you need more?')
assert ld.lang_id() == 'English'
```

With a GET request from the running Docker container:

`http://localhost:5000/langid?text=This%20is%20English.%20Got%20it%20or%20do%20you%20need%20more?`

with the following response:

```json
{
    "language": "English"
}
```
