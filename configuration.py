"""
Contains features for load settings
"""
import os
import json
from dataclasses import dataclass
from environs import Env


@dataclass()
class Paths:
    data: str
    style: str


@dataclass
class Config:
    paths: Paths
    button_links_dict: dict


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    project_path = os.path.dirname((os.path.abspath(__file__)))
    # load configuration from file
    return Config(
        paths=Paths(data=project_path + env.str('DATA_PATH'),
                    style=project_path + env.str('STYLE_PATH'),),
        button_links_dict=env.dict('BUTTON_LINKS', subcast_values=str)
    )
