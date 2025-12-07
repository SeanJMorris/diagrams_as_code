# this was another example from the website that introduced me to this library, (https://topdeveloperacademy.com/articles/top-tools-software-architecture-diagrams-software-architects-toolbox), which is a site made by the same guy who is teaching my software architecture course.

from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.network import ELB, Route53
from diagrams.aws.storage import S3
from diagrams.onprem.queue import Kafka
from diagrams.onprem.analytics import Spark
from diagrams.aws.integration import SNS

with Diagram("Example_2_E-Commerce_Scalable_System", show=False):
    # Route53 and Load Balancer
    dns = Route53("DNS")
    lb = ELB("Load Balancer")
    dns >> lb

    # Application Cluster
    with Cluster("Application Layer"):
        app_servers = [EC2("App Server 1"), EC2("App Server 2"), EC2("App Server N")]
        lb >> app_servers

    # Storage and Database
    with Cluster("Storage and Databases"):
        db = RDS("Primary Database")
        db_replica = RDS("Read Replica")
        db >> db_replica
        cache = Dynamodb("Session Store")
        static_assets = S3("Static Assets")

    app_servers >> db
    app_servers >> cache
    app_servers >> static_assets

    # Purchase Processing
    with Cluster("Purchase Pipeline"):
        purchase_lambda = Lambda("Process Purchases")
        kafka_topic = Kafka("Purchase Topic")
        purchase_lambda >> kafka_topic

    app_servers >> purchase_lambda

    # Recommendations System
    with Cluster("Recommendations Service"):
        recommender = Spark()
        recommender_db = Dynamodb("Recommendations DB")
        kafka_topic >> recommender >> recommender_db
