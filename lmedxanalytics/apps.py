"""
lmedxanalytics Django application initialization.
"""

from django.apps import AppConfig

# try:
#     from openedx.core.djangoapps.plugins.constants import (
#         ProjectType, SettingsType, PluginURLs, PluginSettings
#     )
#     PLATFORM_PLUGIN_SUPPORT = True
# except ImportError:
#     # pre-hawthorn
#     PLATFORM_PLUGIN_SUPPORT = False
    
# if PLATFORM_PLUGIN_SUPPORT:
#     def production_settings_name():
#         return getattr(SettingsType, 'PRODUCTION')


class LmedxanalyticsConfig(AppConfig):
    """
    Configuration for the lmedxanalytics Django application.
    """

    name = 'lmedxanalytics'
    # verbose_name = 'Lmedxanalytics'
    # if PLATFORM_PLUGIN_SUPPORT:
    #     plugin_app = {
    #         PluginURLs.CONFIG: {
    #             ProjectType.LMS: {
    #                 PluginURLs.NAMESPACE: u'lmedxanalytics',
    #                 PluginURLs.REGEX: u'^lmedxanalytics/',
    #             }
    #         },

    #         PluginSettings.CONFIG: {
    #             ProjectType.LMS: {
    #                 production_settings_name(): {
    #                     PluginSettings.RELATIVE_PATH: u'settings.lms_production',
    #                 },
    #             }
    #         },
    #     }
