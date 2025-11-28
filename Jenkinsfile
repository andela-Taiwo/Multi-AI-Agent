pipeline{
    agent any

    environment {
        SONAR_PROJECT_KEY = 'Multi-agent'
		SONAR_SCANNER_HOME = tool 'Sonarqube'
        AWS_REGION = 'eu-north-1'
        ECR_REGISTRY = '313901886195.dkr.ecr.eu-north-1.amazonaws.com'
        ECR_REPO = 'my_repo'
        IMAGE_TAG = 'latest'
	}

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/andela-Taiwo/Multi-AI-Agent.git']])
                }
            }
        }

    stage('SonarQube Analysis'){
			steps {
				withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
    					
					withSonarQubeEnv('sonarqube') {
    						sh """
						${SONAR_SCANNER_HOME}/bin/sonar-scanner \
						-Dsonar.projectKey=${SONAR_PROJECT_KEY} \
						-Dsonar.sources=. \
						-Dsonar.host.url=http://sonarqube-dind:9000 \
						-Dsonar.login=${SONAR_TOKEN}
						"""
					}
				}
			}
		}

    // stage('Build and Push Docker Image to ECR') {
    //         steps {
    //             withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-token']]) {
    //                 script {
    //                     def accountId = sh(script: "aws sts get-caller-identity --query Account --output text", returnStdout: true).trim()
    //                     def ecrUrl = "${accountId}.dkr.ecr.${env.AWS_REGION}.amazonaws.com/${env.ECR_REPO}"

    //                     sh """
    //                     aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ecrUrl}
    //                     docker build -t ${env.ECR_REPO}:${IMAGE_TAG} .
    //                     docker tag ${env.ECR_REPO}:${IMAGE_TAG} ${ecrUrl}:${IMAGE_TAG}
    //                     docker push ${ecrUrl}:${IMAGE_TAG}
    //                     """
    //                 }
    //             }
    //         }
    //     }
    stage('Build and Push Docker Image to ECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-credentials',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    script {
                        // Ensure Docker daemon is running (DinD)
                        sh 'ps aux | grep dockerd || dockerd &'
                        sleep 10
                        
                        // Login to ECR
                        sh """
                            aws ecr get-login-password --region ${AWS_REGION} | \
                            docker login --username AWS --password-stdin ${ECR_REGISTRY}
                        """
                        
                        // Build and push
                        sh """
                            docker build -t ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG} .
                            docker push ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }

    // stage('Deploy to ECS Fargate') {
    // steps {
    //     withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-token']]) {
    //         script {
    //             sh """
    //             aws ecs update-service \
    //               --cluster multi-ai-agent-cluster \
    //               --service multi-ai-agent-def-service-shqlo39p  \
    //               --force-new-deployment \
    //               --region ${AWS_REGION}
    //             """
    //             }
    //         }
    //     }
    //  }
        
    }
}