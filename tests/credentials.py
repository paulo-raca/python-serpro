from typing import Mapping

from pytest import xfail

CREDENTIALS = {"consumer_key": ..., "consumer_secret": ...}


def serpro_credentials() -> Mapping[str, str]:
    if CREDENTIALS["consumer_key"] == ... or CREDENTIALS["consumer_secret"] == ...:
        raise xfail("Missing Serpro credentials")
    return CREDENTIALS
