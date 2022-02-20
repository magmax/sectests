import os
import pytest

sec_reports = dict()


def pytest_report_teststatus(report, config):
    if "user_properties" not in dir(report):
        return
    if report.failed:
        global sec_reports
        d = {k: v for k, v in report.user_properties}
        if "title" in d:
            sec_reports[d["title"]] = d
    return


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.ensure_newline()
    terminalreporter.section("Security Report", sep="-", blue=True, bold=True)
    terminalreporter.ensure_newline()
    global sec_reports
    for name, report in sorted(
        sec_reports.items(), key=lambda x: x[1].get("code", "").split('.')
    ):
        code = report.get("code", "-----")
        impact = report.get("impact", 0)
        descr = report.get("description", "")
        terminalreporter.line(f"{code}: {name} (impact: {impact})")
        for line in descr.splitlines():
            terminalreporter.line(line)
        terminalreporter.line("--")
    terminalreporter.ensure_newline()
    impact_list = [x["impact"] for x in sec_reports.values() if "impact" in x]
    impact = sum(impact_list) if impact_list else 0
    terminalreporter.line(f"Score: {impact}")
