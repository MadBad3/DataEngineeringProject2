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
        scripts{
          if(env.BRANCH_NAME == 'web_interface'){
            bat 'python test_app.py'
          }else if(env.BRANCH_NAME == 'develop'){
            echo "test of develop branch"
          }else if(env.BRANCH_NAME == 'release'){
            input "proceed with deployment to live?"
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        scripts{
          if(env.BRANCH_NAME != 'master'){
            bat 'docker rm -f myflaskapp_c'
            bat 'docker rmi -f myflaskapp'
          }
        }
      }
    }
  }
}


