import sys
import os
from shutil import copy
from langdetect import detect_langs
from langdetect import PROFILES_DIRECTORY
from langdetect import LangDetectException


class E4ALangDetect(object):
    """Performs language detection with Python 3 package `langdetect`,
    mainly for the languages of the project: German, French, Luxembourgish, Romanian, Danish and English.
    I (radu@racai.ro) have generated and added Luxembourgish profile with code `lb`."""

    _recognized_lang_codes = {
        'en': 'English',
        'ro': 'Romanian',
        'lb': 'Luxembourgish',
        'fr': 'French',
        'de': 'German',
        'da': 'Danish'
    }

    def __init__(self, text: str):
        self._text = text

    def lang_id(self) -> str:
        """Main method of this class. Call this to get the language of `self._text`."""

        try:
            languages = detect_langs(self._text)
            
            # Detections are alreay sorted by language probability, from
            # the most probable to the lowest probable.
            for detection in languages:
                if detection.lang in E4ALangDetect._recognized_lang_codes:
                    return E4ALangDetect._recognized_lang_codes[detection.lang]
                # end if
            # end for

            if languages:
                return languages[0].lang
            # end if
        except LangDetectException:
            pass

        return 'Unknown'


# Copy the Luxembourgish profile file where it is supposed to be found.
_lb_profile_file = os.path.join(PROFILES_DIRECTORY, 'lb')

if not os.path.exists(_lb_profile_file):
    source_lb_file = os.path.join('profiles', 'lb')
    print("Copying profile file [{0}] to the profiles folder [{1}]".format(source_lb_file, PROFILES_DIRECTORY))
    copy(source_lb_file, PROFILES_DIRECTORY)
# end if
