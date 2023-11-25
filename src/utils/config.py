from yaml import full_load

class Config:

    @staticmethod
    def __get_config():
        with open('../settings.yml') as dump:
            return full_load(dump)

    @staticmethod
    def get_path(key: str) -> str:
        return Config.__get_config()['paths'][key]
    
    @staticmethod
    def get_setting_float(key: str) -> float:
        return float(Config.__get_config()['params'][key])

    @staticmethod
    def get_setting_int(key: str) -> int:
        return int(Config.__get_config()['params'][key])
    
    @staticmethod
    def get_setting_string(key: str) -> str:
        return Config.__get_config()['params'][key]