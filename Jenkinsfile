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
        script{
          if(env.BRANCH_NAME == 'web_interface'){
            bat 'python unit_tests.py'
          }else if(env.BRANCH_NAME == 'develop'){
	    bat 'pythom stress_tests.py'
          }else if(env.BRANCH_NAME == 'release'){
            input "proceed with deployment to live?"
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if(env.BRANCH_NAME != 'master'){
            bat 'docker rm -f myflaskapp_c'
            bat 'docker rmi -f myflaskapp'
          }
        }
      }
    }
  }
}

