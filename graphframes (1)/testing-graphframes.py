# Databricks notebook source
spark.conf.get("spark.databricks.optimizer.adaptive.enabled")

# COMMAND ----------

# spark.conf.set("spark.graphframes.connectedComponents.algorithm", "graphx")
spark.conf.set("spark.graphframes.connectedComponents.algorithm", "graphframes")
spark.conf.set("spark.graphframes.useLabelsAsComponents", "true")
spark.conf.set("spark.databricks.optimizer.adaptive.enabled", False)



# COMMAND ----------


spark.sql("""
create table if not exists unified.test.friend (
  id string not null,
  name string not null,
  age int not null
)""")

spark.sql("""
create table if not exists unified.test.friend_relationship (
  `src` string not null,
  `dst` string not null,
  `relationship` string not null
)""")

spark.sql("""
  select 
    cast(null as string   ) as id,
    cast(null as string) as name,
    cast(null as int) as age
  where 1=0 union all

  select "a", "Alice"   , 34 union all
  select "b", "Bob"     , 36 union all
  select "c", "Charlie" , 30 union all
  select "d", "David"   , 29  union all
  select "e", "Esther"  , 32 union all
  select "f", "Fanny"   , 36 union all
  select "g", "Gabby"   , 60  
""").write.mode("overwrite").saveAsTable("unified.test.friend")

spark.createDataFrame([
    ("a", "b", "friend"),
    ("b", "c", "follow"),
    ("c", "b", "follow"),
    ("f", "c", "follow"),
    ("e", "f", "follow"),
    ("e", "d", "friend"),
    ("d", "a", "friend"),
    ("a", "e", "friend")], 
    ["src", "dst", "relationship"]
).write.mode("overwrite").saveAsTable("unified.test.friend_relationship")

from graphframes import GraphFrame

vertex = spark.sql("""
  select id, name, age
  from unified.test.friend
""")
vertex.display()

edge = spark.sql("""
  select src, dst, relationship
  from unified.test.friend_relationship
""")
edge.display()

 
dbutils.fs.rm("/tmp/graphframes-example-connected-components", True)
sc.setCheckpointDir("/tmp/graphframes-example-connected-components")

graph = GraphFrame(vertex, edge)
result = graph.connectedComponents()
result.select("id", "component").orderBy("component").display()

# COMMAND ----------

from graphframes import GraphFrame

spark.conf.set("spark.graphframes.connectedComponents.algorithm", "graphframes")

vertex = spark.sql("""
select 
  cast(null as string   ) as id,
  cast(null as string) as name,
  cast(null as int) as age
where 1=0 union all

select "a", "Alice"   , 34 union all
select "b", "Bob"     , 36 union all
select "c", "Charlie" , 30 union all
select "d", "David"   , 29  union all
select "e", "Esther"  , 32 union all
select "f", "Fanny"   , 36 union all
select "g", "Gabby"   , 60  

""")
vertex.display()

edge = spark.createDataFrame([
    ("a", "b", "friend"),
    ("b", "c", "follow"),
    ("c", "b", "follow"),
    ("f", "c", "follow"),
    ("e", "f", "follow"),
    ("e", "d", "friend"),
    ("d", "a", "friend"),
    ("a", "e", "friend")], 
    ["src", "dst", "relationship"])
edge.display()


dbutils.fs.rm("/tmp/graphframes-example-connected-components", True)
sc.setCheckpointDir("/tmp/graphframes-example-connected-components")

graph = GraphFrame(vertex, edge)
result = graph.connectedComponents()
result.select("id", "component").orderBy("component").display()

# COMMAND ----------

from graphframes import GraphFrame

spark.conf.set("spark.graphframes.connectedComponents.algorithm", "graphx")

vertex = spark.sql("""
select 
  cast(null as string   ) as id,
  cast(null as string) as name,
  cast(null as int) as age
where 1=0 union all

select "a", "Alice"   , 34 union all
select "b", "Bob"     , 36 union all
select "c", "Charlie" , 30 union all
select "d", "David"   , 29  union all
select "e", "Esther"  , 32 union all
select "f", "Fanny"   , 36 union all
select "g", "Gabby"   , 60  

""")
vertex.display()

edge = spark.createDataFrame([
    ("a", "b", "friend"),
    ("b", "c", "follow"),
    ("c", "b", "follow"),
    ("f", "c", "follow"),
    ("e", "f", "follow"),
    ("e", "d", "friend"),
    ("d", "a", "friend"),
    ("a", "e", "friend")], 
    ["src", "dst", "relationship"])
edge.display()


dbutils.fs.rm("/tmp/graphframes-example-connected-components", True)
sc.setCheckpointDir("/tmp/graphframes-example-connected-components")

graph = GraphFrame(vertex, edge)
result = graph.connectedComponents()
result.select("id", "component").orderBy("component").display()

# COMMAND ----------



spark.conf.set("spark.graphframes.connectedComponents.algorithm", "graphx")

vertex = spark.createDataFrame([
    ("a", "Alice", 34),
    ("b", "Bob", 36),
    ("c", "Charlie", 30),
    ("d", "David", 29),
    ("e", "Esther", 32),
    ("f", "Fanny", 36),
    ("g", "Gabby", 60)],
    ["id", "name", "age"])
vertex.display()


edge = spark.createDataFrame([
    ("a", "b", "friend"),
    ("b", "c", "follow"),
    ("c", "b", "follow"),
    ("f", "c", "follow"),
    ("e", "f", "follow"),
    ("e", "d", "friend"),
    ("d", "a", "friend"),
    ("a", "e", "friend")], 
    ["src", "dst", "relationship"])
edge.display()


dbutils.fs.rm("/tmp/graphframes-example-connected-components", True)
sc.setCheckpointDir("/tmp/graphframes-example-connected-components")

graph = GraphFrame(vertex, edge)
result = graph.connectedComponents()
result.select("id", "component").orderBy("component").display()

# COMMAND ----------

# This example graph also comes with the GraphFrames package.
from graphframes.examples import Graphs
spark.conf.set("spark.graphframes.connectedComponents.algorithm", "graphx")

dbutils.fs.rm("/tmp/graphframes-example-connected-components", True)
sc.setCheckpointDir("/tmp/graphframes-example-connected-components")

same_g = Graphs(spark).friends()

result = same_g.connectedComponents()
result.select("id", "component").orderBy("component").display()
