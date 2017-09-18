import cloudpassage
import sys
from lib.api_session import ApiSession


class ServerController(ApiSession):
    def __init__(self):
        super(ServerController, self).__init__()
        self.srv = cloudpassage.Server(self.session)

    def show(self, server_id):
    	return self.srv.describe(server_id)


