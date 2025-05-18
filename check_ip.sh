#!/bin/bash

CYAN='\e[1;96m'
WHITE='\e[1;97m'
NC='\e[0m'

show_whois() {
  echo -e "\n${CYAN}🧾 WHOIS simulado...${NC}"
  echo "NetName: EXAMPLE-NET"
  echo "OrgName: Example Org"
  echo "Country: US"
  echo "Abuse Contact: abuse@example.com"
}

echo -e "${CYAN}========== WHOIS CHECK ==========${NC}"
read -p "🔎 Ingresa la IP a consultar: " ip
echo -e "${WHITE}IP ingresada:${NC} $ip"

show_whois "$ip"
