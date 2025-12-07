# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def main():
    print("Hello from diagrams-as-code!")

    with Diagram("Web Service", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")

if __name__ == "__main__":
    main()
