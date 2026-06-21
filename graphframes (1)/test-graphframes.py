# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC select 
# MAGIC   cast(null as int   ) as system_id,
# MAGIC   cast(null as string) as person_id,
# MAGIC   cast(null as string) as first_name,
# MAGIC   cast(null as string) as surname,
# MAGIC   cast(null as string) as email,
# MAGIC   cast(null as string) as irn,
# MAGIC   cast(null as string) as alt_id_1,
# MAGIC   cast(null as string) as alt_id_2,
# MAGIC   cast(null as date  ) as dbo
# MAGIC where 1=0 union all
# MAGIC
# MAGIC select 1, "105", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", null , null  , "1995-02-24" union all
# MAGIC select 1, "111", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , null , null  , "1995-02-24" union all
# MAGIC select 1, "113", "Jonny"         , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", "111"  , null  , "1995-02-24"
# MAGIC
# MAGIC -- select 1, "101", "Shaun"         , "Ryan"    , "shaun.ryan@coh.com"        , "sr101", null  , null  , "1991-01-01" union all
# MAGIC -- select 1, "102", "Christopher"   , "Walen"   , "Christopher.Walen@coh.com" , "cw102", null  , null  , "1992-11-01" union all
# MAGIC -- select 1, "103", "Elizabeth"     , "Taylor"  , "Elizabeth.Taylor@coh.com"  , null   , null  , null  , "1993-08-01" union all
# MAGIC -- select 1, "104", "Daniel"        , "Pratt"   , "Daniel.Pratt@coh.com"      , null   , null  , null  , "1994-04-12" union all
# MAGIC -- select 1, "105", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", "205" , "305" , "1995-02-24" union all
# MAGIC -- select 1, "106", "Thomas"        , "Spencer" , "Thomas.Spencer@coh.com"    , null   , null  , null  , "1996-07-15" union all
# MAGIC -- select 1, "107", "Sandra"        , "Walker"  , "Sandra.Walker@coh.com"     , null   , null  , null  , "1997-10-05" union all
# MAGIC -- select 1, "108", "Suesan"        , "Berry"   , "Suesan.Berry@coh.com"      , null   , null  , null  , "1998-12-21" union all
# MAGIC -- select 1, "109", "Alerbert"      , "Tompson" , "Alerbert.Tompson@coh.com"  , null   , null  , null  , "1999-04-17" union all
# MAGIC -- select 1, "110", "Charlie"       , "Chase"   , "Charlie.Chase@coh.com"     , null   , null  , null  , "2000-05-19" union all
# MAGIC -- select 1, "111", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , "205" , "211" , "1995-02-24" union all
# MAGIC -- select 1, "113", "Jonny"         , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", null  , null  , "1995-02-24" union all
# MAGIC
# MAGIC -- select 2, "201", "Shaun"         , "Ryan"    , "shaun.ryan@coh.com"        , "sr101", null  , null  , "1991-01-01" union all
# MAGIC -- select 2, "202", "Christopher"   , "Walen"   , "Christopher.Walen@coh.com" , "cw102", null  , null  , "1992-11-01" union all
# MAGIC -- select 2, "203", "Elizabeth"     , "Taylor"  , "Elizabeth.Taylor@coh.com"  , null   , null  , null  , "1993-08-01" union all
# MAGIC -- select 2, "204", "Daniel"        , "Pratt"   , "Daniel.Pratt@coh.com"      , null   , null  , null  , "1994-04-12" union all
# MAGIC -- select 2, "205", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , "111" , "105" , "1995-02-24" union all
# MAGIC -- select 2, "206", "Thomas"        , "Spencer" , "Thomas.Spencer@coh.com"    , null   , null  , null  , "1996-07-15" union all
# MAGIC -- select 2, "207", "Sandra"        , "Walker"  , "Sandra.Walker@coh.com"     , null   , null  , null  , "1997-10-05" union all
# MAGIC -- select 2, "208", "Suesan"        , "Berry"   , "Suesan.Berry@coh.com"      , null   , null  , null  , "1998-12-21" union all
# MAGIC -- select 2, "209", "Alerbert"      , "Tompson" , "Alerbert.Tompson@coh.com"  , null   , null  , null  , "1999-04-17" union all
# MAGIC -- select 2, "210", "Charlie"       , "Chase"   , "Charlie.Chase@coh.com"     , null   , null  , null  , "2000-05-19" union all
# MAGIC -- select 2, "211", "Jon"           , "Moore"   , "Jonathan.Moore@coh.com"    , null   , "105" , "111" , "1995-02-24" union all
# MAGIC
# MAGIC -- select 3, "301", "Shaun"         , "Ryan"    , "shaun.ryan@coh.com"        , "sr101", null  , null  , "1991-01-01" union all
# MAGIC -- select 3, "302", "Christopher"   , "Walen"   , "Christopher.Walen@coh.com" , "cw102", null  , null  , "1992-11-01" union all
# MAGIC -- select 3, "303", "Elizabeth"     , "Taylor"  , "Elizabeth.Taylor@coh.com"  , null   , null  , null  , "1993-08-01" union all
# MAGIC -- select 3, "304", "Daniel"        , "Pratt"   , "Daniel.Pratt@coh.com"      , null   , null  , null  , "1994-04-12" union all
# MAGIC -- select 3, "305", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , "505" , "211" , "1995-02-24" union all
# MAGIC -- select 3, "306", "Thomas"        , "Spencer" , "Thomas.Spencer@coh.com"    , null   , null  , null  , "1996-07-15" union all
# MAGIC -- select 3, "307", "Sandra"        , "Walker"  , "Sandra.Walker@coh.com"     , null   , null  , null  , "1997-10-05" union all
# MAGIC -- select 3, "308", "Suesan"        , "Berry"   , "Suesan.Berry@coh.com"      , null   , null  , null  , "1998-12-21" union all
# MAGIC -- select 3, "309", "Alerbert"      , "Tompson" , "Alerbert.Tompson@coh.com"  , null   , null  , null  , "1999-04-17" union all
# MAGIC -- select 3, "310", "Charlie"       , "Chase"   , "Charlie.Chase@coh.com"     , null   , null  , null  , "2000-05-19" union all
# MAGIC
# MAGIC -- select 4, "401", "Shaun"         , "Ryan"    , "shaun.ryan@coh.com"        , "sr101", null  , null, "1991-01-01" union all
# MAGIC -- select 4, "402", "Christopher"   , "Walen"   , "Christopher.Walen@coh.com" , "cw102", null  , null, "1992-11-01" union all
# MAGIC -- select 4, "403", "Elizabeth"     , "Taylor"  , "Elizabeth.Taylor@coh.com"  , null   , null  , null, "1993-08-01" union all
# MAGIC -- select 4, "404", "Daniel"        , "Pratt"   , "Daniel.Pratt@coh.com"      , null   , null  , null, "1994-04-12" union all
# MAGIC -- select 4, "405", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , "111" , null, "1995-02-24" union all
# MAGIC -- select 4, "406", "Thomas"        , "Spencer" , "Thomas.Spencer@coh.com"    , null   , null  , null, "1996-07-15" union all
# MAGIC -- select 4, "407", "Sandra"        , "Walker"  , "Sandra.Walker@coh.com"     , null   , null  , null, "1997-10-05" union all
# MAGIC -- select 4, "408", "Suesan"        , "Berry"   , "Suesan.Berry@coh.com"      , null   , null  , null, "1998-12-21" union all
# MAGIC -- select 4, "409", "Alerbert"      , "Tompson" , "Alerbert.Tompson@coh.com"  , null   , null  , null, "1999-04-17" union all
# MAGIC -- select 4, "410", "Charlie"       , "Chase"   , "Charlie.Chase@coh.com"     , null   , null  , null, "2000-05-19" union all
# MAGIC
# MAGIC -- select 5, "501", "Shaun"         , "Ryan"    , "shaun.ryan@coh.com"        , "sr101", null, null  , "1991-01-01" union all
# MAGIC -- select 5, "502", "Christopher"   , "Walen"   , "Christopher.Walen@coh.com" , "cw102", null, null  , "1992-11-01" union all
# MAGIC -- select 5, "503", "Elizabeth"     , "Taylor"  , "Elizabeth.Taylor@coh.com"  , null   , null, null  , "1993-08-01" union all
# MAGIC -- select 5, "504", "Daniel"        , "Pratt"   , "Daniel.Pratt@coh.com"      , null   , null, null  , "1994-04-12" union all
# MAGIC -- select 5, "505", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , null, "405" , "1995-02-24" union all
# MAGIC -- select 5, "506", "Thomas"        , "Spencer" , "Thomas.Spencer@coh.com"    , null   , null, null  , "1996-07-15" union all
# MAGIC -- select 5, "507", "Sandra"        , "Walker"  , "Sandra.Walker@coh.com"     , null   , null, null  , "1997-10-05" union all
# MAGIC -- select 5, "508", "Suesan"        , "Berry"   , "Suesan.Berry@coh.com"      , null   , null, null  , "1998-12-21" union all
# MAGIC -- select 5, "509", "Alerbert"      , "Tompson" , "Alerbert.Tompson@coh.com"  , null   , null, null  , "1999-04-17" union all
# MAGIC -- select 5, "510", "Charlie"       , "Chase"   , "Charlie.Chase@coh.com"     , null   , null, null  , "2000-05-19"
# MAGIC

# COMMAND ----------

data = spark.sql("""
select 
  cast(null as int   ) as system_id,
  cast(null as string) as person_id,
  cast(null as string) as first_name,
  cast(null as string) as surname,
  cast(null as string) as email,
  cast(null as string) as irn,
  cast(null as string) as alt_id_1,
  cast(null as string) as alt_id_2,
  cast(null as date  ) as dbo
where 1=0 union all

select 1, "105", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", null , null  , "1995-02-24" union all
select 1, "111", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , null , null  , "1995-02-24" union all
select 1, "113", "Jonny"         , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", "111"  , null  , "1995-02-24"
""")

# COMMAND ----------

data = spark.sql("""
select 
  cast(null as int   ) as system_id,
  cast(null as string) as person_id,
  cast(null as string) as first_name,
  cast(null as string) as surname,
  cast(null as string) as email,
  cast(null as string) as irn,
  cast(null as string) as alt_id_1,
  cast(null as string) as alt_id_2,
  cast(null as date  ) as dbo
where 1=0 union all

select 1, "105", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", null , null  , "1995-02-24" union all
select 1, "111", "Jonathan"      , "Moore"   , "Jonathan.Moore@coh.com"    , null   , null , null  , "1995-02-24" union all
select 1, "113", "Jonny"         , "Moore"   , "Jonathan.Moore@coh.com"    , "jm105", "111"  , null  , "1995-02-24"
""")

# COMMAND ----------

# Create a Vertex DataFrame with unique ID column "id"

vertex = data.selectExpr(
  "person_id as id",
  "first_name"
)

vertex.display()

edge = spark.sql("""
  select
    a.person_id AS src,
    b.person_id AS dst,
    "is" as relationship
  from {df} a
  join {df} b on a.irn = b.irn and a.person_id <= b.person_id and a.person_id != b.person_id
  union
  select
    person_id AS src,
    alt_id_1 AS dst,
    "is" as relationship
  from {df}
  where alt_id_1 is not null
  --union
  --select
  --  person_id AS src,
  --  alt_id_2 AS dst,
  --  "alt_id_2" as relationship
  --from {df}
  --where alt_id_2 is not null

  --union
  --select
  --  irn AS src,
  --  person_id AS dst,
  --  "" as relationship
  --from {df}
  --where irn is not null
  --union
  --select
  --  alt_id_1 AS src,
  --  person_id AS dst,
  --  "" as relationship
  --from {df}
  --where alt_id_1 is not null
  --union
  --select
  --  alt_id_2 AS src,
  --  person_id AS dst,
  --  "" as relationship
  --from {df}
  --where alt_id_2 is not null
""", df=data)


edge.display()


# COMMAND ----------

from graphframes import GraphFrame
dbutils.fs.rm("/tmp/graphframes-example-connected-components", True)
sc.setCheckpointDir("/tmp/graphframes-example-connected-components")
graph = GraphFrame(vertex, edge)

# COMMAND ----------

result = graph.connectedComponents()
# graph.connectedComponents.setAlgorithm("graphx")

result.select("id", "component").orderBy("component").display()

# COMMAND ----------

from graphframes.examples import Graphs

g = Graphs(spark).friends()  # Get example graph

g.vertices.display()
g.edges.display()

dbutils.fs.rm('/Volumes/dev_hub/checkpoints/tmp', True)
sc.setCheckpointDir('/Volumes/dev_hub/checkpoints/tmp')

result = g.connectedComponents()
result.select("id", "component").orderBy("component").display()
