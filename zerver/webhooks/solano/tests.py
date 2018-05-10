# -*- coding: utf-8 -*-
import urllib

from zerver.lib.test_classes import WebhookTestCase

class SolanoHookTests(WebhookTestCase):
    STREAM_NAME = 'solano labs'
    URL_TEMPLATE = u"/api/v1/external/solano?api_key={api_key}&stream={stream}"
    FIXTURE_DIR_NAME = 'solano'

    def test_solano_message_001(self) -> None:
        """
        Build notifications are generated by Solano Labs after build completes.
        """
        expected_topic = u'build update'
        expected_message = (u"Author: solano-ci[bot]@users.noreply.github.com\n"
                            u"Commit: [5f438401eb7cc7268cbc28438bfa70bb99f48a03]"
                            u"(github.com/fazerlicourice7/solano/commit/5f438401eb7cc7268"
                            u"cbc28438bfa70bb99f48a03)\nBuild status: failed :thumbs_down:\n"
                            u"[Build Log](https://ci.solanolabs.com:443/reports/3316175)")

        self.send_and_test_stream_message('build_001', expected_topic, expected_message,
                                          content_type="application/x-www-form-urlencoded")

    def test_solano_message_002(self) -> None:
        """
        Build notifications are generated by Solano Labs after build completes.
        """
        expected_topic = u'build update'
        expected_message = (u"Author: Unknown\nCommit: [5d0b92e26448a9e91db794bfed4b8c3556eabc4e]"
                            u"(bitbucket.org/fazerlicourice7/test/commits/5d0b92e26448a9e91db794bfed"
                            u"4b8c3556eabc4e)\nBuild status: failed :thumbs_down:\n"
                            u"[Build Log](https://ci.solanolabs.com:443/reports/3316723)")

        self.send_and_test_stream_message('build_002', expected_topic, expected_message,
                                          content_type="application/x-www-form-urlencoded")

    def test_solano_message_received(self) -> None:
        """
        Build notifications are generated by Solano Labs after build completes.
        """
        expected_topic = u'build update'
        expected_message = (u"Author: solano-ci[bot]@users.noreply.github.com\n"
                            u"Commit: [191d34f9da8ff7279b051cd68e44223253e18408]"
                            u"(github.com/anirudhjain75/scipy/commit/191d34f9da8ff7279b051cd"
                            u"68e44223253e18408)\nBuild status: running :arrows_counterclockwise:\n"
                            u"[Build Log](https://ci.solanolabs.com:443/reports/3317799)")

        self.send_and_test_stream_message('received', expected_topic, expected_message,
                                          content_type="application/x-www-form-urlencoded")

    def test_solano_test_message(self) -> None:
        expected_topic = u'build update'
        expected_message = "Solano webhook set up correctly"

        self.send_and_test_stream_message('test', expected_topic, expected_message,
                                          content_type="application/x-www-form-urlencoded")

    def get_body(self, fixture_name: str) -> str:
        return self.webhook_fixture_data(self.FIXTURE_DIR_NAME, fixture_name, file_type="json")
