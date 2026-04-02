# Guide de Préparation : EX288 - Red Hat Certified OpenShift Application Developer

**Auteur : Zidane Djamal**

## Présentation de l'Examen

L'examen **EX288** (Red Hat Certified Specialist in OpenShift Application Development) évalue la capacité à déployer des applications existantes dans un environnement **Red Hat OpenShift Container Platform**. Il s'agit d'un examen pratique (hands-on) d'une durée de 3 heures, axé sur le développement, le déploiement et la gestion d'applications cloud-natives.

Cet examen constitue l'un des deux prérequis (avec l'EX280) pour obtenir le titre de **Red Hat Certified OpenShift Architect**.

## Objectifs de l'Examen

Les domaines évalués lors de l'examen EX288 couvrent les compétences suivantes :

| Domaine | Description |
|---|---|
| **Déploiement d'applications** | Déployer des applications depuis des images de conteneurs, des templates, et des manifestes |
| **Gestion des builds** | Configurer et gérer les processus de build (Source-to-Image, Dockerfile, etc.) |
| **Gestion de la configuration** | Utiliser ConfigMaps, Secrets, et variables d'environnement |
| **Troubleshooting** | Diagnostiquer et résoudre les problèmes d'applications déployées |
| **Personnalisation des images** | Créer et personnaliser des images de conteneurs pour OpenShift |
| **Helm et Kustomize** | Déployer et gérer des applications avec Helm charts et Kustomize overlays |
| **Pipelines CI/CD** | Configurer et utiliser des pipelines de déploiement continu |

## Dépôts de Préparation Recommandés

### Ressources à Pertinence DIRECTE

| Dépôt | Description | Priorité |
|---|---|---|
| [openshift-appdev-skills-path](https://github.com/zdmooc/openshift-appdev-skills-path) | Programme d'apprentissage complet structuré comme un chemin de compétences (DO188, DO288, EX188, EX288). **Point de départ idéal.** | 1 |
| [bpce-natixis-gitops-openshift-quarkus-lab](https://github.com/zdmooc/bpce-natixis-gitops-openshift-quarkus-lab) | Lab complet Java/Quarkus sur OpenShift avec GitOps de bout en bout (GitHub Actions, GitLab, Jenkins, Argo CD). | 2 |
| [openshift-cicd-blueprints](https://github.com/zdmooc/openshift-cicd-blueprints) | Modèles CI/CD pour OpenShift : Tekton pipelines, Jenkins, intégration GitOps. | 3 |
| [helm-openshift-roadmap](https://github.com/zdmooc/helm-openshift-roadmap) | Feuille de route Helm 3 sur OpenShift 4.x, du débutant à l'expert. | 4 |
| [openshift-products-definition](https://github.com/zdmooc/openshift-products-definition) | Guide pratique de déploiement GitOps avec Argo CD sur OpenShift Local (CRC). | 5 |
| [openshift-gitops-standard-6files](https://github.com/zdmooc/openshift-gitops-standard-6files) | Standard de gestion de configurations via GitOps avec Kustomize et Argo CD. | 6 |
| [openshift-reference-apps](https://github.com/zdmooc/openshift-reference-apps) | Applications de référence prêtes pour le GitOps (Helm, Kustomize) sur OpenShift. | 7 |
| [openshift-event-driven-lab](https://github.com/zdmooc/openshift-event-driven-lab) | Lab d'architecture événementielle avec Kafka/Redpanda et GitOps sur OpenShift. | 8 |
| [kafka-data-engineer-kafkaops-topic-service-crc](https://github.com/zdmooc/kafka-data-engineer-kafkaops-topic-service-crc) | Projet complet Kafka sur OpenShift Local : Strimzi, FastAPI, Ansible. | 9 |

### Ressources Complémentaires

| Dépôt | Description |
|---|---|
| [helm-masterclass](https://github.com/zdmooc/helm-masterclass) | Masterclass Helm avec 50 démonstrations pratiques pour Kubernetes DevOps. |
| [my-helm-charts](https://github.com/zdmooc/my-helm-charts) | Exemple pratique de chart Helm pour OpenShift. |
| [openshift-doc-map](https://github.com/zdmooc/openshift-doc-map) | Carte de navigation de la documentation officielle OpenShift. |

## Parcours d'Apprentissage Recommandé

**Semaines 1-2 : Fondations Conteneurs**
- Si vous n'êtes pas familier avec les conteneurs, commencez par `docker-podman-complete-masterclass`.
- Installez OpenShift Local (CRC) pour votre environnement de lab.

**Semaines 3-5 : Parcours de Compétences**
- Suivez le programme structuré de `openshift-appdev-skills-path` (DO188 puis DO288).
- Pratiquez les examens blancs EX188 et EX288 inclus.

**Semaines 6-7 : Helm, Kustomize & GitOps**
- Maîtrisez Helm avec `helm-openshift-roadmap`.
- Apprenez les standards GitOps avec `openshift-gitops-standard-6files`.

**Semaine 8 : Projet Intégrateur**
- Réalisez le lab complet `bpce-natixis-gitops-openshift-quarkus-lab` de bout en bout.
- Ce projet couvre la création d'application, les tests, le packaging, le CI/CD et le déploiement GitOps.

**Semaine 9 : Révision et Examen Blanc**
- Révisez les domaines faibles identifiés.
- Refaites les exercices pratiques les plus complexes.

## Références

- [Page officielle de l'examen EX288](https://www.redhat.com/en/services/training/ex288-red-hat-certified-openshift-application-developer-exam)
- [Documentation officielle OpenShift](https://docs.openshift.com/)
