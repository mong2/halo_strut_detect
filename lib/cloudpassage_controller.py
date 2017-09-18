import cloudpassage
from lib.api_session import ApiSession

class CloudPassageController(ApiSession):
	def __init__(self):
		super(CloudPassageController, self).__init__()
		self.halo = cloudpassage.HttpHelper(self.session)

	def finding_details(self, findind_url):
		return self.halo.get(findind_url)