pipeline {
  agent any
  triggers { pollSCM('* * * * *') }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t mon-app:${BUILD_NUMBER} -t mon-app:latest .'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker rm -f mon-app || true'
        sh 'docker run -d --name mon-app -p 5000:5000 --restart unless-stopped mon-app:latest'
      }
    }
  }
}
