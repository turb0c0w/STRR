from unittest import mock
from strr_api.common.flags import Flags


def test_flag_values(app):
    flag_name = 'OPS_LOGGER_LEVEL_FLAG'
    flag_value = 'ERROR'
    with mock.patch.object(Flags, 'value', return_value=flag_value):
        assert Flags.value(flag_name) == flag_value
