# Infrastructure

This directory contains infrastructure as code and deployment configurations.

## Structure

- `docker/` - Docker configurations
  - Dockerfiles for different services
  - docker-compose files for local development
- `kubernetes/` - Kubernetes manifests
  - Deployments, services, ingress configurations
  - ConfigMaps and secrets
- `terraform/` - Infrastructure provisioning
  - Cloud resource definitions (AWS/Azure/GCP)
  - Networking, databases, and compute resources

## Deployment

### Local Development
```bash
docker-compose up
```

### Kubernetes
```bash
kubectl apply -f kubernetes/
```

### Terraform
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

## Environments

- Development
- Staging
- Production
