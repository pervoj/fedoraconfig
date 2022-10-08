from action_parts.repositories import actions as repositories
from action_parts.drivers import actions as drivers
from action_parts.sudo import actions as sudo
from action_parts.dnf import actions as dnf
from action_parts.installs import actions as installs

actions = []

# actions += repositories
# actions += drivers
actions += sudo
# actions += dnf
# actions += installs
