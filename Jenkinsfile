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
        sh 'docker run -d --name mon-app -p 5000:80 --restart unless-stopped mon-app:latest'
        sh 'docker rm -f nginx-exporter || true'
        sh 'docker run -d --name nginx-exporter --add-host=host.docker.internal:host-gateway -p 9113:9113 --restart unless-stopped nginx/nginx-prometheus-exporter:latest --nginx.scrape-uri=http://host.docker.internal:5000/stub_status'
      }
    }
  }
}
