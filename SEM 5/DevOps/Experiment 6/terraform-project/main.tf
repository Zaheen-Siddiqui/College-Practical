provider "aws" {
  region = "ap-south-1"
}

# Dynamically fetch the latest Amazon Linux 2 AMI for the region
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Create EC2 instance
resource "aws_instance" "demo" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  tags = {
    Name = "CLI-Terraform-EC2"
  }
}
