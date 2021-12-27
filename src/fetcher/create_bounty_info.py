from dataclasses import dataclass
from src.constants import CONFIG_LOCATION
from src.utils import load_yml
import logging
logger = logging.getLogger(__name__)

@dataclass
class BountyInfo:
    exchange: str
    symbol: str
    since: int
    to: int


def create_bounty_info(config_location=CONFIG_LOCATION) -> list[BountyInfo]:
    bounty_infos = load_yml(config_location)
    bounty_list = []
    
    for bounty_num, bounty_info in bounty_infos.items():
        bounty_list.append(BountyInfo(**bounty_info))
    logger.info(f'bounty_list: {bounty_infos}')
    return bounty_list
