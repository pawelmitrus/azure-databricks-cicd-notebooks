// Databricks notebook source
dbutils.widgets.text("notebook", dbutils.notebook.getContext().notebookPath.get)

// COMMAND ----------

val notebook_path = dbutils.widgets.get("notebook") + "/../ingestion_test"

// COMMAND ----------

dbutils.notebook.run(notebook_path, 600)