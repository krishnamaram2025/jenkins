"""
This module is intended to check Jenkins server version
"""
import jenkinsapi
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    """
    This function is intended to get server instance
    """
    jenkins_url = 'http://18.207.240.57:8080/'
    # The below line is to authenticate Jenkins server
    server = Jenkins(jenkins_url, username='akhil', password='')
    print("server", server)
    return server

if __name__ == '__main__':
    gf = get_server_instance()
    jenkins_server_version = gf.version
    print (jenkins_server_version)
