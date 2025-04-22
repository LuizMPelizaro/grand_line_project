from pyspark.sql.types import StructType, StructField, StringType, LongType

SCHEMA_QUOTE_LIST = StructType([
    StructField('raw_quote_list', StringType(), False),
    StructField('date_request', LongType(), False),
])