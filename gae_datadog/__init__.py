from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder
vendor.add('lib')

from datadog import initialize, ThreadStats
import sync

config = sync.app.config

initialize(api_key=config['DATADOG_API_KEY'])

t_stats = ThreadStats()
t_stats.start(flush_in_thread=False)

from integration import app as application
