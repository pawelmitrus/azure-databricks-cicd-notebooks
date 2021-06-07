// Databricks notebook source
dbutils.widgets.text("notebook", dbutils.notebook.getContext().notebookPath.get)

// COMMAND ----------

val notebook_path = dbutils.widgets.get("notebook") + "/../../ingestion"

// COMMAND ----------

val result = dbutils.notebook.run(notebook_path, 600, Map("sourcePath" -> "/databricks-datasets/flights/departuredelays.csv", "targetPath" -> "/tmp/fact_departuredelays"))

// COMMAND ----------

val df = spark.read.format("delta").load("/tmp/fact_departuredelays")

// COMMAND ----------

val row = df.orderBy("datetime").first
assert(row.getValuesMap[Any](Array("delay", "distance", "origin", "destination")) == Map("delay" -> -8, "distance" -> 2024, "origin" -> "LAX", "destination" -> "PBI"))