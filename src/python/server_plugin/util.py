import enum


class Privileges(enum.Enum):
    PRIV_NONE          = 0
    PRIV_PLAYER        = 1
    PRIV_SUPPORTER     = 2
    PRIV_MODERATOR     = 3
    PRIV_OPERATOR      = 4
    PRIV_ADMINISTRATOR = 5
    PRIV_DEVELOPER     = 6
    PRIV_CREATOR       = 7
    PRIV_MAX           = 8
    PRIV_START         = 1
    PRIV_ELEVATED      = 3
    PRIV_LAST          = 7
    PRIV_TYPE          = 0xFF
    PRIV_LOCAL         = 1<<8
