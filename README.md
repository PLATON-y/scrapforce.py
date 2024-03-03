ScrapForce.py
À propos de ScrapForce

scrapforce.py est un outil avancé de scraping web et de scan de port écrit en Python. Conçu pour assister dans les tâches de cybersécurité, il permet aux utilisateurs de récupérer le contenu des pages web et d'identifier les ports ouverts sur une adresse IP spécifiée. Ce programme utilise le multithreading pour améliorer l'efficacité et intègre des fonctionnalités avancées comme le support de proxy et une gestion robuste des erreurs.
Fonctionnalités

    Scraping Web : Extraire les liens d'une page web spécifiée.
    Scan de Port : Identifier les ports ouverts sur une adresse IP.
    Support Proxy : Effectuer des requêtes via un proxy spécifié.
    Multithreading : Utilisation de threads pour accélérer le scan de port.

Installation

    Assurez-vous que Python 3 est installé sur votre système.
    Clonez ce dépôt ou téléchargez le script scrapforce.py.
    Installez les dépendances nécessaires via pip :

    pip install requests

Utilisation

Utilisez le script en ligne de commande avec les options suivantes :

python scrapforce.py --url [URL] --ip [IP] --start_port [DEBUT] --end_port [FIN] --proxy [PROXY]

Options :

    --url : URL de la page à scraper.
    --ip : Adresse IP à scanner.
    --start_port : Port de début pour le scan.
    --end_port : Port de fin pour le scan.
    --proxy : Proxy à utiliser (format: http://user:pass@proxy:port).

Avertissements Légaux et Éthiques

En utilisant scrapforce.py, vous acceptez de le faire de manière éthique et conforme à toutes les lois et régulations locales applicables. Le scraping de sites web et le scan de ports peuvent être soumis à des restrictions légales dans certaines juridictions, et il est de la responsabilité de l'utilisateur de s'assurer que leur utilisation de cet outil ne viole pas ces restrictions.

Nous déclinons toute responsabilité pour l'utilisation abusive de cet outil ou pour tout dommage qui pourrait survenir de son utilisation. Cet outil est fourni "tel quel", sans garantie d'aucune sorte.

Contribuer

Nous accueillons les contributions sous forme de suggestions, de corrections de bugs ou de nouvelles fonctionnalités. Veuillez soumettre vos contributions via des pull requests ou des issues sur la plateforme de gestion de code source utilisée pour ce projet.
Licence

Ce projet est distribué sous la Licence Publique Générale GNU, version 3 (GPLv3). Voir le fichier LICENSE pour plus de détails.
