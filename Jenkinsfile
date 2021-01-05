pipeline {
  agent {
    docker {
      label 'dockerhost-label'
      image 'python:3.8-buster'
      args '-u root'
    }
  }
  stages {

    stage ('Install dependencies') {
    
      steps {
        sh '''
          pip install pytest-testinfra paramiko
        '''
      }
    }

    stage ('pytest') {
      steps {
          sshagent(credentials : ['vagrant-id']) {
            sh '''
              pytest --disable-warnings --hosts=lab --ssh-config=./ssh_config test_service.py
            '''
          }
      }
    }

  } 

  post { 
    always { 
      cleanWs()
    }
  }

}
