class IcebergTableCreator:
    def __init__(self, spark, path_warehouse):
        self.spark = spark
        self.path_warehouse = path_warehouse

    def create_table(self, schema, partition_cols=None):
        partition_clause = ""
        if partition_cols:
            partition_clause = f"PARTITIONED  BY ({','.join(partition_cols)})"

        schema_sql = ",\n ".join([f"{field.name} {self.__convert_type(field.dataType)}" for field in schema.fields])

        create_sql = f"""
        CREATE TABLE IF NOT EXISTS {self.path_warehouse} (
            {schema_sql}
            )
            USING ICEBERG
            {partition_clause}
        """
        self.spark.sql(create_sql)

    def __convert_type(self, data_type):
        mapping = {
            "IntegerType": "INT",
            "LongType": "BIGINT",
            "StringType": "STRING",
            "TimestampType": "TIMESTAMP",
            "DoubleType": "DOUBLE",
            "FloatType": "FLOAT",
            "BooleanType": "BOOLEAN",
            "DateType": "DATE"
        }
        return mapping.get(data_type.__class__.__name__, "STRING")


class IcebergTableUpdater:
    def __init__(self, spark, full_path_warehouse):
        self.spark = spark
        self.full_path_warehouse = full_path_warehouse

    def upsert(self, df, key_columns: list):
        """
        Realiza um upsert (merge) dos dados do DataFrame para a tabela Iceberg.

        Args:
            df (DataFrame): DataFrame com os dados a serem upsertados
            key_columns (list): colunas que definem a chave para o merge
        """
        temp_view = "temp_upsert_view"
        df.createOrReplaceTempView(temp_view)

        # Clauses
        columns = df.columns
        on_clause = " AND ".join([f"target.{col} = source.{col}" for col in key_columns])
        update_clause = ", ".join([f"{col} = source.{col}" for col in df.columns if col not in key_columns])
        insert_columns = ", ".join(columns)
        insert_values = ", ".join([f"source.{col}" for col in columns])

        # SQL de merge
        merge_sql = f"""
        MERGE INTO {self.full_path_warehouse} AS target
        USING {temp_view} AS source
        ON {on_clause}
        WHEN MATCHED THEN UPDATE SET {update_clause}
        WHEN NOT MATCHED THEN INSERT ({insert_columns}) VALUES ({insert_values})
        """

        self.spark.sql(merge_sql)
