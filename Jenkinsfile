pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        bat 'docker build -t myflaskapp .'
      }
    }
    stage('Run Flask App'){
      steps{
        bat 'docker run -d -p 5000:5000 --name myflaskapp_c myflaskapp'
      }
    }
    stage('Testing'){
      steps{
        bat 'python test_app.py'
      }
    }
    stage('Docker images down'){
      steps{
        bat 'docker rm -f myflaskapp_c'
        bat 'docker rmi -f myflaskapp'
      }
    }
  }
}
