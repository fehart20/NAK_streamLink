import configparser
import inquirer
import logging


class Config:

    def __init__(self, config_file: str) -> None:
        self.config_file: str = config_file
        self._config = configparser.ConfigParser()
        self._config.read(self.config_file)

    def save_config(self):
        self._config.set("settings.stream", "link", self.stream_link)
        self._config.set("settings.stream", "location", self.stream_location)

        with open(self.config_file, 'w') as cf:
            self._config.write(cf)
            logging.info("CONFIG - Saved new fields")


class StreamConfig(Config):

    def __init__(self, config_file) -> None:
        super().__init__(config_file)
        try:
            self.stream_link: str = self._config.get("settings.stream", "link")
            self.stream_location: str = self._config.get(
                "settings.stream", "location")
        except (configparser.NoOptionError, configparser.NoSectionError):
            logging.critical(f"CONFIG - Missing fields in {config_file}")
            self.create_config()

    def create_config(self):
        user_input_list = [
            inquirer.List(
                'stream_link',
                'Please choose a streaming location: ',
                choices=[
                    ('Nürtingen',
                     ('http://nactube.datagis.com/c/NAKNuertingen',
                      "Nürtingen")),
                    ('Metzingen', ('http://nactube.datagis.com/v/SIyvExJfyuM',
                                   'Metzingen')),
                    ('Münsingen', ('http://nactube.datagis.com/v/Q-MIeFojxsE',
                                   'Münsingen')),
                    ('Oberboihingen',
                     ('http://nactube.datagis.com/v/mpMCZzs7wFS',
                      'Oberboihingen')),
                    ('Aichtal', ('http://nactube.datagis.com/v/FQGmVQ-VqZy',
                                 'Aichtal')), ('Own location', '')
                ],
                default=['http://nactube.datagis.com/c/NAKNuertingen'])
        ]
        user_input = inquirer.prompt(user_input_list)

        if not user_input["stream_link"]:
            self.stream_link = input("Own link: ")
            self.stream_location = input("Own location: ")
            self.save_config()
            return

        self.stream_link = user_input["stream_link"][0]
        self.stream_location = user_input["stream_link"][1]
        self.save_config()
