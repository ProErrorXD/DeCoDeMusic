
import html
from pyrogram import __version__ as pyrover
from ProMusic import __version__
from sys import version_info
import re

__version__ = "{version_info[0]}.{version_info[1]}"


class LangsFormatMap(dict):
    def __getitem__(self, key):
        if key not in self:
            return self.__missing__(key)
        self.used.append(key)
        if type(self.get(key)) == str:
            return html.escape(self.get(key)) if self.escape_html else self.get(key)
        else:
            return self.get(key)

    def __missing__(self, key):
        if self.debug:
            print(f'Key "{key}" is missing on the string "{self.string}", language "{self.code}"')
        return '{' + key + '}'


class LangString(str):
    def __call__(self, **kwargs):
        mapping = LangsFormatMap(**kwargs)
        mapping.escape_html = self.escape_html
        mapping.string = self.key
        mapping.code = self.code
        mapping.debug = self.debug
        mapping.used = []
        formatted = self.format_map(mapping)

        not_used = [key for key in kwargs.keys() if key not in mapping.used]
        if self.debug and len(not_used):
            for key in not_used:
                print(
                    f'The parameter "{key}" was passed to the string "{self.key}" (language "{self.code}") but was not used')
            print('')
        return formatted


class Langs:
    strings = {}
    escape_html = False
    available = []
    code = 'en'
    debug = True

    def __init__(self, strings={}, escape_html=False, debug=True, **kwargs):
        self.strings = strings
        self.escape_html = escape_html

        if not kwargs and not strings:
            raise ValueError(
                'Pass the language codes and their objects (dictionaries containing the strings) as keyword arguments (language=dict)')

        for language_code, strings_object in kwargs.items():
            self.strings[language_code] = strings_object
            self.strings[language_code].update({'LANGUAGE_CODE': language_code})

        # self.strings = {'en':{'start':'Hi {name}!'}}
        self.available = list(self.strings.keys())
        self.code = 'en' if 'en' in self.available else self.available[0]
        self.debug = debug

    def __getattr__(self, key):
        try:
            result = self.strings[self.code][key]
        except:
            result = key
        obj = LangString(result)
        obj.escape_html = self.escape_html
        obj.key = key
        obj.code = self.code
        obj.debug = self.debug
        return obj

    def normalize_code(self, language_code):
        only_az = re.sub('[^a-z]', '', (language_code or ''))
        return only_az.lower()

    def get_language(self, language_code):
        clean_lang_code = self.normalize_code(language_code) or 'en'

        lang_copy = Langs(strings=self.strings, escape_html=self.escape_html)
        if clean_lang_code in lang_copy.available:
            lang_copy.code = clean_lang_code
        elif clean_lang_code[:2] in lang_copy.available:
            lang_copy.code = clean_lang_code[:2]
        return lang_copy

    def getLanguage(self, *args, **kwargs):
        print("Langs.getLanguage is deprecated and will be removed soon. Use Langs.get_language instead")
        return self.get_language(*args, **kwargs)










from Basiclanguage import language

get_string = langs.get_string
reload_strings = langs.reload_strings
get_languages = langs.get_languages
get_language = langs.get_language


