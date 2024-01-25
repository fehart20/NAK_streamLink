from nakStreamLink.read_config import StreamConfig

CONFIG_FILE = "config.ini"


def main():
    stream_config = StreamConfig(CONFIG_FILE)
    stream_config.create_config()


if __name__ == "__main__":
    main()
