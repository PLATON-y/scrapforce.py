#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
scrapforce.py

Copyright (C) 2024 par Platon-y

Ce programme est un logiciel libre : vous pouvez le redistribuer et/ou le modifier
sous les termes de la Licence Publique Générale GNU publiée par
la Free Software Foundation, soit la version 3 de la Licence, soit
(selon votre choix) toute version ultérieure.

Ce programme est distribué dans l'espoir qu'il sera utile,
mais SANS AUCUNE GARANTIE ; sans même la garantie implicite de
MARCHANDABILITÉ ou D'ADÉQUATION À UN USAGE PARTICULIER. Voir le
Licence Publique Générale GNU pour plus de détails.

Vous devriez avoir reçu une copie de la Licence Publique Générale GNU
avec ce programme. Si ce n'est pas le cas, consultez <https://www.gnu.org/licenses/>.
"""

import socket
from concurrent.futures import ThreadPoolExecutor
import requests
import re
import time
import logging
import argparse
from requests.exceptions import RequestException
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

logging.basicConfig(level=logging.INFO, format=f'{bcolors.OKGREEN}%(asctime)s - %(levelname)s - %(message)s{bcolors.ENDC}')

parser = argparse.ArgumentParser(description='Outil de scraping avancé et de scan de port')
parser.add_argument('--url', type=str, help='URL de la page à scraper', default='')
parser.add_argument('--ip', type=str, help='Adresse IP à scanner', default='')
parser.add_argument('--start_port', type=int, help='Port de début pour le scan', default=1)
parser.add_argument('--end_port', type=int, help='Port de fin pour le scan', default=65535)
parser.add_argument('--proxy', type=str, help='Proxy à utiliser (format: http://user:pass@proxy:port)', default='')
args = parser.parse_args()

proxies = {'http': args.proxy, 'https': args.proxy} if args.proxy else None

def fetch_url(url):
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        logging.error(f"{bcolors.FAIL}Erreur lors de la requête {url}: {e}{bcolors.ENDC}")
        return None

def scrape(url):
    page_content = fetch_url(url)
    if page_content:
        links = re.findall(r'href="(http[s]?://[^"]+)"', page_content)
        for link in links:
            logging.info(f"{bcolors.OKBLUE}Lien trouvé : {link}{bcolors.ENDC}")

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                logging.info(f"{bcolors.HEADER}Port {port} est ouvert sur {ip}.{bcolors.ENDC}")
    except socket.error as e:
        logging.error(f"{bcolors.FAIL}Erreur de connexion à {ip} sur le port {port}: {e}{bcolors.ENDC}")

def print_help():
    print("""
Nom du Script: Outil de scraping avancé et de scan de port

Usage: 
    python scrapforce.py --url [URL] --ip [IP] --start_port [DEBUT] --end_port [FIN] --proxy [PROXY]

Options:
    --url        URL de la page à scraper.
    --ip         Adresse IP à scanner.
    --start_port Port de début pour le scan.
    --end_port   Port de fin pour le scan.
    --proxy      Proxy à utiliser (format: http://user:pass@proxy:port).

À propos:
    Ce script est un outil de scraping web et de scan de port conçu pour aider dans les tâches de cybersécurité. 
    Il utilise le multithreading pour améliorer l'efficacité et intègre des fonctionnalités avancées comme le support de proxy et une gestion robuste des erreurs.
    """)

def main():
    if '--help' in sys.argv or '--about' in sys.argv:
        print_help()
    else:
        if args.url:
            scrape(args.url)
        if args.ip:
            with ThreadPoolExecutor(max_workers=50) as executor:
                for port in range(args.start_port, args.end_port + 1):
                    executor.submit(scan_port, args.ip, port)

if __name__ == '__main__':
    main()
