import json
import os

with open('/home/ubuntu/analyze_openshift_repos.json', 'r') as f:
    data = json.load(f)

repos = data['results']

# Filter out empty or non-relevant repos
valid_repos = [r['output'] for r in repos if 'output' in r and r['output'].get('pertinence') in ['DIRECTE', 'COMPLEMENTAIRE', 'INDIRECTE']]

def get_relevance_score(repo):
    p = repo.get('pertinence', '')
    if p == 'DIRECTE': return 1
    if p == 'COMPLEMENTAIRE': return 2
    return 3

valid_repos.sort(key=lambda x: (get_relevance_score(x), x['repo_name']))

# Group by target certification
certs_map = {
    'EX280': [],
    'EX288': [],
    'GitOps_ArgoCD': [],
    'Architecture_SRE': [],
    'Fondamentaux_K8s': []
}

for repo in valid_repos:
    certs = repo.get('certifications_ciblees', '').upper()
    name = repo['repo_name'].lower()
    domaines = repo.get('domaines_couverts', '').lower()
    
    added = False
    
    if 'EX280' in certs or 'DO280' in certs:
        certs_map['EX280'].append(repo)
        added = True
        
    if 'EX288' in certs or 'DO288' in certs:
        certs_map['EX288'].append(repo)
        added = True
        
    if 'argocd' in name or 'gitops' in name or 'argocd' in domaines or 'gitops' in domaines:
        certs_map['GitOps_ArgoCD'].append(repo)
        added = True
        
    if 'architect' in name or 'sre' in name or 'sre' in domaines or 'architecture' in domaines:
        certs_map['Architecture_SRE'].append(repo)
        added = True
        
    if not added:
        certs_map['Fondamentaux_K8s'].append(repo)

readme_content = """# OpenShift Certifications Hub

Bienvenue sur le **OpenShift Certifications Hub**, le dépôt centralisateur de toutes les ressources créées et maintenues par **Zidane Djamal** pour la préparation aux certifications Red Hat OpenShift et technologies cloud-natives associées.

Ce dépôt a pour objectif de vous guider à travers l'écosystème riche de laboratoires pratiques, de frameworks d'architecture, et de guides de révision disponibles sur mon profil GitHub.

## 🎯 À propos de l'Auteur

**Zidane Djamal**  
*Architecte Cloud & DevOps | Expert OpenShift & Kubernetes*

Ce portfolio est le fruit de plusieurs années d'expérience terrain et d'ingénierie de plateforme sur les technologies Red Hat, Kubernetes et l'écosystème Cloud-Native.

---

## 🗺️ Parcours de Certification Red Hat OpenShift

Le programme de certification Red Hat OpenShift est structuré autour de deux piliers fondamentaux, menant au titre ultime d'Architecte :

1. **Les Fondations (Prérequis pour l'Architecte) :**
   - **EX280** : Red Hat Certified OpenShift Administrator
   - **EX288** : Red Hat Certified OpenShift Application Developer

2. **Red Hat Certified OpenShift Architect :**
   S'obtient en détenant l'une des certifications fondamentales (EX280 ou EX288) **ET** 5 certifications de spécialisation parmi une liste définie (ex: API Management, ServiceMesh, Quarkus, Event-Driven/Kafka, OpenShift Virtualization, etc.).

---

## 📚 Catalogue des Ressources par Domaine

"""

sections = [
    ('EX280', '🛡️ Administration OpenShift (EX280)', 'Ressources dédiées à la gestion, configuration et sécurisation des clusters OpenShift.'),
    ('EX288', '💻 Développement d\'Applications OpenShift (EX288)', 'Ressources pour le déploiement, la gestion et l\'optimisation d\'applications cloud-natives.'),
    ('GitOps_ArgoCD', '🔄 GitOps & Déploiement Continu (ArgoCD)', 'Pratiques avancées de GitOps, indispensables pour les environnements OpenShift modernes.'),
    ('Architecture_SRE', '🏛️ Architecture & Site Reliability Engineering (SRE)', 'Frameworks de migration, blueprints réseau et runbooks d\'exploitation.'),
    ('Fondamentaux_K8s', '🐳 Fondamentaux Kubernetes & Conteneurs', 'Bases essentielles (Docker, Podman, Kubernetes The Hard Way) pour maîtriser l\'écosystème.')
]

for key, title, desc in sections:
    repo_list = certs_map.get(key, [])
    if not repo_list:
        continue
        
    readme_content += f"### {title}\n\n"
    readme_content += f"{desc}\n\n"
    
    readme_content += "| Dépôt | Pertinence | Description Rapide |\n"
    readme_content += "|---|---|---|\n"
    
    seen = set()
    for repo in repo_list:
        if repo['repo_name'] in seen:
            continue
        seen.add(repo['repo_name'])
        
        name = repo['repo_name']
        url = repo['repo_url']
        pertinence = repo['pertinence']
        summary = repo.get('summary', '').replace('\n', ' ')
        # Truncate summary if too long for the table
        if len(summary) > 150:
            summary = summary[:147] + "..."
            
        readme_content += f"| [{name}]({url}) | **{pertinence}** | {summary} |\n"
    
    readme_content += "\n"

readme_content += """## 🚀 Comment utiliser ces ressources ?

1. **Identifiez votre objectif actuel** : Visez-vous l'administration (EX280), le développement (EX288), ou une spécialisation (GitOps, SRE) ?
2. **Consultez les dépôts `DIRECTE`** : Commencez par les guides ultimes et les parcours de compétences.
   - Pour EX280 : Démarrez avec `EX280-Ultimate-Guide`
   - Pour EX288 : Démarrez avec `openshift-appdev-skills-path`
   - Pour l'Architecture : Explorez `rh-openshift-architect-lab`
3. **Pratiquez avec les Labs** : La plupart des dépôts sont conçus comme des laboratoires "hands-on" (CRC, Kind, ou cluster réel). Clonez-les et exécutez les exercices.
4. **Explorez les ressources complémentaires** : Approfondissez avec les dépôts sur ArgoCD, Helm, ou la sécurité.

---
*Dépôt généré automatiquement pour centraliser le portfolio de Zidane Djamal.*
"""

with open('/home/ubuntu/openshift-certifications-hub/README.md', 'w') as f:
    f.write(readme_content)

print("README.md généré avec succès.")
