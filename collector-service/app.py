from scheduler import start_scheduler
import yaml


def load_config():
    with open('config.yaml') as f:
        return yaml.safe_load(f)


if __name__ == '__main__':
    config = load_config()
    start_scheduler(config)