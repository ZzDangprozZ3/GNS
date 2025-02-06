from gns3fy import Gns3Connector, Project, Node
import telnetlib
import time
import json

# Connect to GNS3
server = Gns3Connector("http://localhost:3080")
project_name = "Automation_Network"
project = Project(name=project_name, connector=server)
project.get()

# Assurer le projet est ouvert
if project.status != "opened":
    project.open()


with open('routers_data.json', 'r') as file:
    data = json.load(file)

def start_router(router_name):
    router = next((node for node in project.nodes if node.name == router_name), None)  # Search and parcourir for all the nodes we have in projet
    if not router:
        print(f"Cant find {router_name} in {project_name}.")
        return None

    if router.status != "started":
        print(f"Starting {router_name}...")
        router.start()
        time.sleep(5)  # just wait for it to setting up
    else:
        print(f"Router {router_name} is already running.")
    return router

def send_telnet_commands(tn, commands):
    for cmd in commands:
        tn.write(f"{cmd}\r\n".encode("utf-8"))
        time.sleep(0.1)  # Wait router execute

def configure_router(node):
    router_name = node.name
    console_port = node.console

    # Verifier Router dans intent file
    if router_name not in data["Routers"]:
        print(f"{router_name} is not configured in intent file.")
        return

    try:
        # Connexion à Telnet
        tn = telnetlib.Telnet(node.console_host, console_port)
        print(f"Connexion {router_name} passed!")
        for i in range(3):
            tn.write("\r\n".encode("utf-8"))
            time.sleep(0.5)
        time.sleep(1)
        # Activer IPV6
        send_telnet_commands(tn, [
            "end",
            "configure terminal",
            "ipv6 unicast-routing",
            "end"
        ])

        # Configuration adresse IPV6
        for interface, details in data["Routers"][router_name]["Interfaces"].items():
            send_telnet_commands(tn, [
                "configure terminal",
                f"interface {interface}",
                "ipv6 enable",
                f"ipv6 address {details['IP']}/{details['Mask']}",
                "no shutdown",
                "end"
            ])

        # Protocoles
        for protocol, settings in data["Routers"][router_name]["Protocols"].items():
            if protocol == "RIP":
                configure_rip(tn, settings)
            elif protocol == "OSPF":
                configure_ospf(tn, settings, data["Routers"][router_name]["Router ID"])
            elif protocol == "BGP":
                configure_bgp(tn, settings, data["Routers"][router_name]["AS"], data["Routers"][router_name]["Router ID"])

        tn.close()
    except Exception as e:
        print(f"Error when configure {router_name}: {e}")

def configure_rip(tn, settings):
    send_telnet_commands(tn, [
        "configure terminal",
        f"ipv6 router rip {settings['Name']}",
        "redistribute connected",
        "end"
    ])

    for interface in settings["Interfaces"]:
        send_telnet_commands(tn, [
            "configure terminal",
            f"interface {interface}",
            f"ipv6 rip {settings['Name']} enable",
            "end"
        ])

    if "Redistribute" in settings:                 # For each router connecting directly with another AS, must redistribute bgp and connected
        send_telnet_commands(tn, [
            "configure terminal",
            f"ipv6 router rip {settings['Name']}"
        ] + [f"redistribute {r}" for r in settings["Redistribute"]] + ["end"])

def configure_ospf(tn, settings, router_id):        # Same as RIP
    send_telnet_commands(tn, [
        "configure terminal",
        f"ipv6 router ospf {settings['Name']}",
        f"router-id {router_id}",
        "end"
    ])

    for interface in settings["Interfaces"]:
        send_telnet_commands(tn, [
            "configure terminal",
            f"interface {interface}",
            f"ipv6 ospf {settings['Name']} area {settings['Area']}",
            "end"
        ])

    if "Redistribute" in settings:
        send_telnet_commands(tn, [
            "configure terminal",
            f"ipv6 router ospf {settings['Name']}"
        ] + [f"redistribute {r}" for r in settings["Redistribute"]] + ["end"])

def configure_bgp(tn, settings, as_number, router_id):
    send_telnet_commands(tn, [
        "configure terminal",
        f"router bgp {as_number}",
        "no bgp default ipv4-unicast",
        f"bgp router-id {router_id}"
    ])

    # Neighbors configurations
    for neighbor, remote_as in settings["Neighbors"].items():
        commands = []
        commands.append(f"neighbor {neighbor} remote-as {remote_as}")
        commands.append("address-family ipv6 unicast")
        commands.append(f"neighbor {neighbor} activate")
        if remote_as ==  as_number:
            commands.append(f"neighbor {neighbor} update-source loop 0")
        commands.append("exit")
        send_telnet_commands(tn, commands)


    # Advertising
    if "Advertise" in settings:
        send_telnet_commands(tn, ["address-family ipv6 unicast"] + [f"network {net}" for net in settings["Advertise"]] + ["end"])

# Process
for node in project.nodes:
    start_router(node.name)
    configure_router(node)
