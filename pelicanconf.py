AUTHOR = 'Kale Miller'
SITENAME = 'blog.kalemiller.com'
SITEURL = 'https://blog.kalemiller.com'

PATH = 'content'

TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = 'en'
THEME = ".theme"

USE_FOLDER_AS_CATEGORY = True
OUTPUT_RETENTION = ["CNAME"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme-required config
LINKS = (
    ('LinkedIn', 'https://linkedin.com/in/kalelewismiller'),
    ('Twitter', 'https://twitter.com/KaleLewisMiller'),
    ('Github', 'https://github.com/kmiller96'),
)
SOCIAL = (
    ('linkedin', 'https://linkedin.com/in/kalelewismiller'),
    ('github', 'https://github.com/kmiller96'),
    ('twitter', 'https://twitter.com/KaleLewisMiller'),
)

SITEDESCRIPTION = "Musings on code, life, and everything else."
DISPLAY_SUMMARY = True
DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 8

FAVICON = 'images/favicon.png'
STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/.htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'},
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
