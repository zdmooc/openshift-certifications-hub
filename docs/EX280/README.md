# Guide de Préparation : EX280 - Red Hat Certified OpenShift Administrator

**Auteur : Zidane Djamal**

## Présentation de l'Examen

L'examen **EX280** (Red Hat Certified Specialist in OpenShift Administration) évalue les compétences nécessaires pour créer, configurer et gérer une plateforme d'applications cloud basée sur **Red Hat OpenShift Container Platform**. Il s'agit d'un examen pratique (hands-on) d'une durée de 3 heures, réalisé sur un cluster OpenShift réel.

Cet examen constitue l'un des deux prérequis pour obtenir le titre de **Red Hat Certified OpenShift Architect**.

## Objectifs de l'Examen

Les domaines évalués lors de l'examen EX280 couvrent les compétences suivantes :

| Domaine | Description |
|---|---|
| **Gestion du cluster OpenShift** | Utiliser la CLI et la console web, évaluer la santé du cluster, effectuer des tâches de maintenance courantes |
| **Déploiement d'applications** | Déployer des applications depuis des images, des templates, et des manifestes Kubernetes/OpenShift |
| **Gestion du stockage** | Configurer et gérer les Persistent Volumes et les Persistent Volume Claims |
| **Configuration du réseau** | Configurer les routes, les services, et les politiques réseau (NetworkPolicy) |
| **Sécurité et authentification** | Configurer l'authentification, les autorisations (RBAC), les Security Context Constraints (SCC) |
| **Gestion des ressources** | Configurer les quotas, les limites de ressources, et la mise à l'échelle automatique |
| **Surveillance et journalisation** | Surveiller les événements du cluster, gérer les alertes, consulter les journaux |

## Dépôts de Préparation Recommandés

### Ressources à Pertinence DIRECTE

Les dépôts suivants sont spécifiquement conçus pour préparer l'examen EX280 :

| Dépôt | Description | Priorité |
|---|---|---|
| [EX280-Ultimate-Guide](https://github.com/zdmooc/EX280-Ultimate-Guide) | Guide complet de 90 pages, 20 labs, 4 scénarios d'examen complets. C'est **LA ressource principale** pour cette certification. | 1 |
| [openshift-doc-map](https://github.com/zdmooc/openshift-doc-map) | Carte de navigation de la documentation officielle OpenShift, avec guides synthétiques et diagrammes d'architecture. | 2 |
| [rh-openshift-architect-lab](https://github.com/zdmooc/rh-openshift-architect-lab) | Espace de travail complet pour la préparation de la certification Architecte, organisé par certification (inclut EX280). | 3 |
| [openshift-networking-blueprints](https://github.com/zdmooc/openshift-networking-blueprints) | Blueprints réseau pour OpenShift : Ingress/Routes, NetworkPolicies, Egress, Services. | 4 |
| [openshift-security-policy-pack](https://github.com/zdmooc/openshift-security-policy-pack) | Politiques de sécurité prêtes à l'emploi : PSA, Kyverno, OPA Gatekeeper. | 5 |
| [openshift-sre-runbook](https://github.com/zdmooc/openshift-sre-runbook) | Runbooks SRE pour le diagnostic et la résolution d'incidents courants. | 6 |
| [k8s-openshift-cluster-factory](https://github.com/zdmooc/k8s-openshift-cluster-factory) | Framework pour construire et opérer des plateformes K8s/OpenShift à l'échelle industrielle. | 7 |
| [openshift-migration-framework](https://github.com/zdmooc/openshift-migration-framework) | Framework de migration vers OpenShift 4.x avec HA, sécurité PCI DSS, et DevSecOps. | 8 |
| [ca-gip-openstack-to-openshift-transformation-framework](https://github.com/zdmooc/ca-gip-openstack-to-openshift-transformation-framework) | Framework de transformation OpenStack vers OpenShift en contexte bancaire. | 9 |

### Ressources Complémentaires

| Dépôt | Description |
|---|---|
| [openshift-platform-bootstrap](https://github.com/zdmooc/openshift-platform-bootstrap) | Base reproductible pour initialiser un environnement OpenShift (namespaces, LimitRange, ResourceQuota, GitOps). |
| [openshift-platform-architect-portfolio](https://github.com/zdmooc/openshift-platform-architect-portfolio) | Portfolio d'architecte avec études de cas : landing zone GitOps, DevSecOps, SRE/Observabilité. |
| [openshift-sso-keycloak-patterns](https://github.com/zdmooc/openshift-sso-keycloak-patterns) | Patterns SSO avec Keycloak sur OpenShift : reverse-proxy OIDC, mappage de rôles. |
| [dynatrace-crc-lab](https://github.com/zdmooc/dynatrace-crc-lab) | Lab d'observabilité Dynatrace sur OpenShift Local (CRC). |

## Parcours d'Apprentissage Recommandé

Le parcours suivant est recommandé pour une préparation optimale à l'examen EX280 :

**Semaines 1-2 : Fondations**
- Clonez et étudiez `openshift-doc-map` pour comprendre la structure de la documentation officielle.
- Installez OpenShift Local (CRC) en suivant les instructions de `openshift-platform-bootstrap`.

**Semaines 3-6 : Étude Approfondie**
- Suivez le `EX280-Ultimate-Guide` chapitre par chapitre.
- Pratiquez chacun des 20 laboratoires inclus.

**Semaines 7-8 : Spécialisations**
- Approfondissez le réseau avec `openshift-networking-blueprints`.
- Renforcez la sécurité avec `openshift-security-policy-pack`.
- Pratiquez le troubleshooting avec `openshift-sre-runbook`.

**Semaine 9 : Examens Blancs**
- Réalisez les 4 scénarios d'examen complets du `EX280-Ultimate-Guide`.
- Identifiez vos lacunes et révisez les domaines faibles.

## Références

- [Page officielle de l'examen EX280](https://www.redhat.com/en/services/training/red-hat-certified-openshift-administrator-exam)
- [Documentation officielle OpenShift](https://docs.openshift.com/)
