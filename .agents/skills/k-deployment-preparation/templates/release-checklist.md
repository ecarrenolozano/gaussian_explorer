# Release Checklist

## Artifact and Approval

- [ ] Exact release candidate identified
- [ ] Automated testing evidence is current
- [ ] Stakeholder acceptance is current
- [ ] Architecture version is current
- [ ] Target environment is named

## Architecture and Deployment Scope

- [ ] arc42 deployment view reviewed or not-applicable reason recorded
- [ ] Relevant runtime, concepts, quality scenarios, risks, and decisions reviewed
- [ ] Architecture containers mapped to actual deployable artifacts or resources
- [ ] Data stores, brokers, caches, workers, and external integrations identified

## Preparation

- [ ] Access and permissions verified
- [ ] Configuration sources verified
- [ ] Secret references verified without exposing values
- [ ] Migrations and compatibility reviewed
- [ ] Backups and prerequisites verified
- [ ] Deployment order and pause conditions approved

## Verification and Recovery

- [ ] Health checks defined
- [ ] Monitoring and observation window defined
- [ ] Rollback or forward-recovery plan verified
- [ ] Communication and escalation paths defined

## Approval

- [ ] Plan version approved for the exact artifact and environment
- [ ] Accepted risks have owners and authorized approvers
