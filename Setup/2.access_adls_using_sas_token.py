# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using SAS Token
# MAGIC 1. Set the spark config for SAS Token
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.vishalformula1dl.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.vishalformula1dl.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.vishalformula1dl.dfs.core.windows.net", "sp=racwdlmeop&st=2023-03-24T23:26:30Z&se=2023-03-25T07:26:30Z&spr=https&sv=2021-12-02&sr=c&sig=5ZWiitJO41OjTfAbqqrXPXXyRiGb1%2FT6M0b1THc4fEc%3D")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@vishalformula1dl.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@vishalformula1dl.dfs.core.windows.net/circuites.csv"))

# COMMAND ----------


