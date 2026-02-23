from pyspark.sql import SparkSession

print("Starting Spark Supply Chain Analysis...\n")

# Start spark
spark = SparkSession.builder.appName("SupplyChain").getOrCreate()

# Load data
df = spark.read.csv("orders.csv", header=True, inferSchema=True)

print("Dataset loaded in Spark!\n")

# Show data
df.show()

# Supplier performance
print("Average delivery time by supplier:")
df.groupBy("supplier_id").avg("delivery_days").show()

# Product demand
print("Total quantity sold by product:")
df.groupBy("product_id").sum("quantity").show()

# Revenue by warehouse
print("Revenue by warehouse:")
df.groupBy("warehouse_id").sum("cost").show()

print("Spark Analysis Complete!")