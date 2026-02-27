import yaml, os
from appium.options.android import UiAutomator2Options


class Capability:

    @staticmethod
    def get_android_options(app_name):
        path = os.path.join(os.path.dirname(__file__), '../config/env_config.yaml')
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
            
        options = UiAutomator2Options()
        app_data = config['apps'].get(app_name)
        
        if not app_data:
            raise ValueError(f"App '{app_name}' not found in env_config.yaml! Check your keys.")

        # Mapping YAML values to Appium Options
        options.device_name = config['device']
        options.app_package = app_data['package']
        options.app_activity = app_data['activity']
        
        # Stability flags
        options.no_reset = True
        options.ensure_webviews_have_pages = True
        
        return options, config['server'], app_data['package']
