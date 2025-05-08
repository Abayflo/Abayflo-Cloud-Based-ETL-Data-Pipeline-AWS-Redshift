provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "etl_data" {
  bucket = "your-etl-data-bucket"
  force_destroy = true
}

resource "aws_redshift_cluster" "redshift_cluster" {
  cluster_identifier = "etl-redshift-cluster"
  node_type           = "dc2.large"
  master_username     = "admin"
  master_password     = "YourStrongPassword123"
  cluster_type        = "single-node"
  publicly_accessible = true

  tags = {
    Name = "ETL Redshift Cluster"
  }
}
