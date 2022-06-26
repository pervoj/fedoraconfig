from action_parts.repositories import actions as repositories
from action_parts.dnf import actions as dnf
from action_parts.installs import actions as installs

actions = []

actions += repositories
actions += dnf
actions += installs
