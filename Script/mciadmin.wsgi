import os, sys
sys.path.append('C:\Python26\Lib\site-packages\pywin32_system32')
sys.path.append('C:\Python26\Lib\site-packages\win32\libs')
sys.path.append('C:\Python26\Lib\site-packages\win32\lib')
sys.path.append('C:\Django\Workspace\MobileInsuranceAdmin')

os.environ['DJANGO_SETTINGS_MODULE'] = 'MobileInsuranceAdmin.settings'

import django.core.handlers.wsgi
import pywintypes

application = django.core.handlers.wsgi.WSGIHandler()
