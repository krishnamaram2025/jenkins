import jenkinsapi
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://44.200.182.151:8080/'
    server = Jenkins(jenkins_url, username='akhil', password='123')
    return server

if __name__ == '__main__':
    print (get_server_instance().version)
