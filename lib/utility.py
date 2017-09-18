

class Utility(object):
    def __init__(self, config):
        self.col = config.csv_columns

    def latest_findings(self, info):
        last_finding = info["findings"][-1]
        return last_finding["finding"]

    def parse_url(self, info):
        url = self.latest_findings(info)
        return url.split(".com")[-1]

    def strut_version(self, filepath):
        package = filepath.split("-")[-1]
        version = package.strip(".jar")
        return version

    def compare_strut_version(self, filepath):
        result = {}
        version = self.strut_version(filepath)

        result["file_path"] = filepath
        result["strut_version"] = version
        result["strut_package"] = False

        if '2.0.1' <= version <= '2.3.33':
            result["strut_package"] = True
            return result
        elif '2.5' <= version <= '2.5.10':
            result["strut_package"] = True
            return result
        return result

    def find_strut(self, findings):
        for f in findings["findings"]:
            if "struts" in f["file"]:
                return self.compare_strut_version(f["file"])

    def structure_report(self, srv_info, result):
        data = {
            self.col["agent_id"]: srv_info["id"],
            self.col["hostname"]: srv_info["hostname"],
        }
        data.update(result)
        return data