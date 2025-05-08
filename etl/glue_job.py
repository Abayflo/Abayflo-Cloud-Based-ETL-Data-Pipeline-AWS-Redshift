import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load data from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://your-bucket-name/sample_data.csv"]},
    format="csv",
    format_options={"withHeader": True}
)

# Transform
applymapping = ApplyMapping.apply(frame=datasource, mappings=[
    ("order_id", "string", "order_id", "int"),
    ("customer", "string", "customer", "string"),
    ("amount", "string", "amount", "double"),
    ("order_date", "string", "order_date", "timestamp")
])

# Load to Redshift
glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=applymapping,
    catalog_connection="your-redshift-connection",
    connection_options={"dbtable": "sales_orders", "database": "your_database"},
    redshift_tmp_dir="s3://your-temp-dir/temp/"
)

job.commit()
