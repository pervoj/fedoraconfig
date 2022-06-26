from action_parts.repositories import actions as repositories
from action_parts.dnf import actions as dnf

actions = []

actions += repositories
actions += dnf
