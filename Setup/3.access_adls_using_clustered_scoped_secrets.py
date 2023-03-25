# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using Cluster Scoped Credentials
# MAGIC 1. Edit Spark Config in Cluster Configurations
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@vishalformula1dl.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@vishalformula1dl.dfs.core.windows.net/circuites.csv"))

# COMMAND ----------


