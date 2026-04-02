# Feuille de Route vers le Red Hat Certified OpenShift Architect

**Auteur : Zidane Djamal**

Ce document présente la feuille de route complète pour atteindre le titre de **Red Hat Certified OpenShift Architect**, en s'appuyant sur les ressources disponibles dans ce portfolio.

---

## Vue d'Ensemble du Parcours

```
                    ┌─────────────────────────────────────┐
                    │  Red Hat Certified OpenShift         │
                    │  Architect                           │
                    │  (EX280 ou EX288 + 5 spécialisations)│
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────┴──────────────────────┐
                    │                                      │
           ┌────────┴────────┐              ┌─────────────┴──────────┐
           │    EX280        │              │       EX288            │
           │  Administration │              │  App Development       │
           └────────┬────────┘              └─────────────┬──────────┘
                    │                                      │
           ┌────────┴────────┐              ┌─────────────┴──────────┐
           │  Fondamentaux   │              │   Fondamentaux         │
           │  K8s + Réseau   │              │   Conteneurs + CI/CD   │
           └─────────────────┘              └────────────────────────┘
```

---

## Phase 1 : Fondamentaux (Mois 1-2)

L'objectif de cette phase est de bâtir des bases solides en conteneurisation et en Kubernetes.

| Semaine | Activité | Dépôt |
|---|---|---|
| 1-2 | Maîtriser Docker et Podman | [docker-podman-complete-masterclass](https://github.com/zdmooc/docker-podman-complete-masterclass) |
| 3-4 | Comprendre Kubernetes en profondeur | [demystifions-kubernetes](https://github.com/zdmooc/demystifions-kubernetes) |
| 5-6 | Déploiement Kubernetes multi-cloud | [kubernetes-the-hard-way-multicloud](https://github.com/zdmooc/kubernetes-the-hard-way-multicloud) |
| 7-8 | Maîtriser Helm 3 | [helm-masterclass](https://github.com/zdmooc/helm-masterclass) |

---

## Phase 2 : Certification EX280 - Administration (Mois 3-5)

| Semaine | Activité | Dépôt |
|---|---|---|
| 1-2 | Cartographier la documentation officielle | [openshift-doc-map](https://github.com/zdmooc/openshift-doc-map) |
| 2-3 | Initialiser l'environnement de lab | [openshift-platform-bootstrap](https://github.com/zdmooc/openshift-platform-bootstrap) |
| 3-6 | Suivre le guide EX280 (20 labs) | [EX280-Ultimate-Guide](https://github.com/zdmooc/EX280-Ultimate-Guide) |
| 7 | Approfondir le réseau | [openshift-networking-blueprints](https://github.com/zdmooc/openshift-networking-blueprints) |
| 8 | Approfondir la sécurité | [openshift-security-policy-pack](https://github.com/zdmooc/openshift-security-policy-pack) |
| 9 | Pratiquer le troubleshooting | [openshift-sre-runbook](https://github.com/zdmooc/openshift-sre-runbook) |
| 10-11 | Examens blancs et révisions | [EX280-Ultimate-Guide](https://github.com/zdmooc/EX280-Ultimate-Guide) |
| 12 | **Passer l'examen EX280** | - |

---

## Phase 3 : Certification EX288 - Développement (Mois 6-8)

| Semaine | Activité | Dépôt |
|---|---|---|
| 1-3 | Suivre le parcours de compétences | [openshift-appdev-skills-path](https://github.com/zdmooc/openshift-appdev-skills-path) |
| 4-5 | Maîtriser Helm sur OpenShift | [helm-openshift-roadmap](https://github.com/zdmooc/helm-openshift-roadmap) |
| 6-7 | Maîtriser les pipelines CI/CD | [openshift-cicd-blueprints](https://github.com/zdmooc/openshift-cicd-blueprints) |
| 8-9 | Projet intégrateur Quarkus + GitOps | [bpce-natixis-gitops-openshift-quarkus-lab](https://github.com/zdmooc/bpce-natixis-gitops-openshift-quarkus-lab) |
| 10-11 | Examens blancs et révisions | [openshift-appdev-skills-path](https://github.com/zdmooc/openshift-appdev-skills-path) |
| 12 | **Passer l'examen EX288** | - |

---

## Phase 4 : Expertise GitOps & ArgoCD (Mois 9-11)

| Semaine | Activité | Dépôt |
|---|---|---|
| 1-2 | Cours fondamental ArgoCD | [ArgoCD-Complete-Master-Course](https://github.com/zdmooc/ArgoCD-Complete-Master-Course) |
| 3-6 | Masterclass ArgoCD (8 semaines condensées) | [argocd-complete-masterclass](https://github.com/zdmooc/argocd-complete-masterclass) |
| 7-9 | Pack expert production-grade | [argocd-expert-pack](https://github.com/zdmooc/argocd-expert-pack) |
| 10 | Standard GitOps 6 fichiers | [openshift-gitops-standard-6files](https://github.com/zdmooc/openshift-gitops-standard-6files) |
| 11-12 | Déployer une plateforme GitOps complète | [gitops-platform](https://github.com/zdmooc/gitops-platform) |

---

## Phase 5 : Spécialisations & Architecture (Mois 12-24)

Cette phase couvre l'obtention des 5 certifications de spécialisation nécessaires pour le titre d'Architecte.

| Activité | Dépôt |
|---|---|
| Étudier le parcours Architecte complet | [rh-openshift-architect-lab](https://github.com/zdmooc/rh-openshift-architect-lab) |
| Construire le portfolio d'architecte | [openshift-platform-architect-portfolio](https://github.com/zdmooc/openshift-platform-architect-portfolio) |
| Pratiquer les migrations | [openshift-migration-framework](https://github.com/zdmooc/openshift-migration-framework) |
| Pratiquer les transformations | [ca-gip-openstack-to-openshift-transformation-framework](https://github.com/zdmooc/ca-gip-openstack-to-openshift-transformation-framework) |
| Maîtriser la sécurité SSO | [openshift-sso-keycloak-patterns](https://github.com/zdmooc/openshift-sso-keycloak-patterns) |
| Maîtriser l'observabilité | [dynatrace-crc-lab](https://github.com/zdmooc/dynatrace-crc-lab) |
| Maîtriser l'event-driven | [openshift-event-driven-lab](https://github.com/zdmooc/openshift-event-driven-lab) |
| Maîtriser Kafka sur OpenShift | [kafka-data-engineer-kafkaops-topic-service-crc](https://github.com/zdmooc/kafka-data-engineer-kafkaops-topic-service-crc) |
| Opérer des clusters industriels | [k8s-openshift-cluster-factory](https://github.com/zdmooc/k8s-openshift-cluster-factory) |

---

## Récapitulatif : 35 Dépôts, 1 Objectif

Ce portfolio de **35 dépôts** couvre l'intégralité du parcours vers le titre de Red Hat Certified OpenShift Architect. Chaque dépôt a été conçu comme un laboratoire pratique, reproductible et documenté, permettant un apprentissage autonome et progressif.

---

*Feuille de route maintenue par Zidane Djamal.*
