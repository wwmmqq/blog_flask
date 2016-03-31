DEBUG = False
FLATPAGES_ROOT = 'blog/pages'
FLATPAGES_EXTENSION = '.md'


AUTHOR = u'Mao quan'
SITENAME = u'maoquan.com'
SITEURL = 'http://maoquan.com'
PAGE_PATHS = ['pages']
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'


# Make URLs clean
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'post_stats',
    'pelican_gist',
]

# Blogroll
LINKS =  None

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'themes/sl'

RELATIVE_URLS = True

#Navigation sections and relative URL:
SECTIONS = [
    ('about', ''),
    ('projects', 'projects'),
   	('Archive', 'archives.html'),
    # ('Tags', 'tags.html'),
]

DEFAULT_CATEGORY = 'uncategorized'
DATE_FORMAT = {
    'en': '%b %d, %Y'
}
DEFAULT_DATE_FORMAT = '%b %d, %Y'

TWITTER_USERNAME = 'myqway'
LINKEDIN_URL = 'http://www.linkedin.com/in/myqway/'
GITHUB_URL = 'http://github.com/wwmmqq'


MAIL_USERNAME = 'myqway'
MAIL_HOST = 'gmail.com'
