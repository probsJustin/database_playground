variable "region" {
  default = "us-east-2"
}

variable "applicationName" {
  default = "databaseApplication"
}

variable "userName" {
  default = "justinshagerty@gmail.com"
}

variable "image" {
  default = "ami-089a545a9ed9893b6"
}

variable "instanceType" {
  default = "t2.medium"
}

variable "key_pair_name" {
  default = "Deployment-Key-Pair"
}