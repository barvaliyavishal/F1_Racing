# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using access keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.vishalformula1dl.dfs.core.windows.net",
    "ck1FWENS3epHiHtZ1gnAyW09hgADYZZ7PNX9UMoM3OvvYXLF7DR7wsoeRomrqbTqdogI88dRv==")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@vishalformula1dl.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@vishalformula1dl.dfs.core.windows.net/circuites.csv"))

# COMMAND ----------


