# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope = 'formula1-scope')

# COMMAND ----------

vishalformula1dl_account_key = dbutils.secrets.get(scope = 'formula1-scope', key='vishalformula1dl-key')

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.vishalformula1dl.dfs.core.windows.net", vishalformula1dl_account_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@vishalformula1dl.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@vishalformula1dl.dfs.core.windows.net/circuites.csv"))

# COMMAND ----------


