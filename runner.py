#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib
import logging
import sys


class StrutReport():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.issue = lib.IssueController()
        self.halo = lib.CloudPassageController()
        self.srv = lib.ServerController()
        self.csv_writer = lib.CsvWriter(self.config)
        self.utility = lib.Utility(self.config)
        self.csv_columns = self.config.csv_columns

    def matched_issues(self):
        return self.issue.list_all(status="active",
                                   policy_id=self.config.policy_id)

    def get_finding_url(self):
        urls = []
        for i in self.matched_issues():
            issue_info = self.issue.show(i["id"])
            finding_endpoint = self.utility.parse_url(issue_info)
            urls.append((i["agent_id"],finding_endpoint))
        return urls

    def gather_data(self, srv_id, result):
        srv_info = self.srv.show(srv_id)
        issue_dict = self.utility.structure_report(srv_info, result)
        self.csv_writer.write(self.csv_columns.values(), issue_dict)

    def run(self):
        for srv_id, url in self.get_finding_url():
            findings = self.halo.finding_details(url)
            result = self.utility.find_strut(findings)
            if result["strut_package"]:
                self.gather_data(srv_id, result)

def main():
    sys.stdout = lib.Logger(logging.info)
    sys.stderr = lib.Logger(logging.warning)
    halo_sr = StrutReport()
    halo_sr.run()
if __name__ == "__main__":
    main()

