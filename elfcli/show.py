import logging

from cliff.command import Command


class Sections(Command):

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info("showing available sections")
