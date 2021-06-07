# Databricks notebook source
dbutils.widgets.text('sourcePath', '')
dbutils.widgets.text('targetPath', '')

sourcePath = dbutils.widgets.get('sourcePath')
targetPath = dbutils.widgets.get('targetPath')

# COMMAND ----------

#sourcePath = '/databricks-datasets/flights/departuredelays.csv'
#targetPath = '/tmp/fact_departuredelays'

# COMMAND ----------

from pyspark.sql.functions import col
from pyspark.sql.types import TimestampType, DateType
import json

try:
  df = spark.read.format('csv')\
          .option('header', True)\
          .option('inferSchema', True)\
          .load(sourcePath)

  df.withColumn("datetime", col("date").cast(TimestampType()))\
    .withColumn("date", col("date").cast(TimestampType()).cast(DateType()))\
    .write.format('delta').mode('overwrite')\
    .save(targetPath)
except:
  dbutils.notebook.exit(json.dumps({
    "status": "FAILED",
    "message": "Could not process and save dataset!"
  }))

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC --select * from delta.`/tmp/fact_departuredelays`

# COMMAND ----------

import json

dbutils.notebook.exit(json.dumps({
  "status": "OK",
  "targetPath": targetPath
}))