# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

def main():

    file_label = "Sean's First Diagram"
    # File names automatically get renamed to lowercase with underscores instead of spaces as a png file.
    file_name = file_label.lower().replace(" ", "_") + ".png"

    print(f"The {file_name} diagram has been generated.")

    with Diagram("Sean's First Diagram", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")

if __name__ == "__main__":
    main()
