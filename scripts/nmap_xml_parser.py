#!/usr/bin/env python3
"""Summarize Nmap XML output from an authorized lab scan."""

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_scan(path: Path):
    root = ET.parse(path).getroot()
    hosts = []
    for host in root.findall("host"):
        address_node = host.find("address")
        address = address_node.get("addr") if address_node is not None else "unknown"
        ports = []
        for port in host.findall("./ports/port"):
            state = port.find("state")
            if state is None or state.get("state") != "open":
                continue
            service = port.find("service")
            ports.append({
                "port": int(port.get("portid")),
                "protocol": port.get("protocol"),
                "service": service.get("name", "unknown") if service is not None else "unknown",
                "product": service.get("product", "") if service is not None else "",
                "version": service.get("version", "") if service is not None else "",
            })
        hosts.append({"address": address, "open_ports": ports})
    return hosts


def review_notes(hosts):
    notes = []
    for host in hosts:
        for service in host["open_ports"]:
            port = service["port"]
            if port in {21, 23}:
                notes.append({"host": host["address"], "port": port, "note": "Legacy clear-text service; verify necessity and restrict or replace in the lab."})
            elif port in {80, 8080}:
                notes.append({"host": host["address"], "port": port, "note": "Web service discovered; review manually with an authorized web-testing proxy."})
            elif port == 22:
                notes.append({"host": host["address"], "port": port, "note": "SSH exposed; verify intended access controls and configuration."})
    return notes


def main():
    parser = argparse.ArgumentParser(description="Parse Nmap XML from an authorized lab scan")
    parser.add_argument("xml_file", type=Path)
    args = parser.parse_args()
    hosts = parse_scan(args.xml_file)
    print(json.dumps({"hosts": hosts, "review_notes": review_notes(hosts)}, indent=2))


if __name__ == "__main__":
    main()
